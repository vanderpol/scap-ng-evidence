"""Read-only preservation and executable rejection; never run a release body."""
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]


class EvidencePublicationBoundary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = Path(os.environ['SCAP_NG_PUBLICATION_GATE_ROOT'])
        spec = importlib.util.spec_from_file_location('audit', cls.gate / 'scripts/audit_publication_paths.py')
        cls.audit = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.audit)
        cls.pin = json.loads((ROOT / 'docs/issue40/preservation.json').read_text())

    def test_full65_release_fails_closed_before_download_and_preserves_original_body(self):
        doc = yaml.load((ROOT / '.github/workflows/publish-v04-human-review.yml').read_text(), Loader=yaml.BaseLoader)
        steps = doc['jobs']['publish']['steps']
        self.assertEqual(steps[0]['uses'], 'vanderpol/scap-ng-tools/.github/actions/configure-gate@' + self.pin['gate_commit'])
        self.assertEqual(steps[1]['run'], self.audit.DENY_PRELUDE)
        remaining = steps[2:]
        self.assertTrue(remaining[-1]['run'].startswith(self.audit.DENY_PRELUDE))
        remaining[-1]['run'] = remaining[-1]['run'][len(self.audit.DENY_PRELUDE):]
        doc['jobs']['publish']['steps'] = remaining
        actual = sha256(json.dumps(doc, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        self.assertEqual(actual, self.pin['baseline_workflow_ast_sha256'])
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / 'must-not-publish'
            proc = subprocess.run(['bash', '-c', self.audit.DENY_PRELUDE + 'printf bypass > "$PUB_MARKER"'],
                                  capture_output=True, text=True,
                                  env=dict(os.environ, SCAPNG_PUBLICATION_GATE_SRC=str(self.gate / 'src'), PUB_MARKER=str(marker)))
            self.assertNotEqual(proc.returncode, 0)
            self.assertFalse(marker.exists())
            self.assertIn('legacy direct publication is blocked', proc.stderr)

    def test_every_current_main_publication_sink_is_guarded_in_the_proposal(self):
        report = self.audit.inventory(ROOT, 'vanderpol/scap-ng-evidence', self.pin['gate_commit'])
        self.assertEqual(report['unprotected_workflow_sinks'], 0)
        actual = [r for r in report['workflow_sinks'] if r['kind'] != 'helper']
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0]['status'], 'DIRECT_PUBLICATION_DENIED')

    def test_historical_65_payload_proof_trees_are_identical(self):
        for folder, expected in self.pin['historical_trees'].items():
            actual = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD:' + folder], text=True).strip()
            self.assertEqual(actual, expected, folder)
        changed = subprocess.check_output(['git', '-C', str(ROOT), 'diff', '--name-only', '--',
                                            'runs', 'manifests', 'summaries'], text=True)
        self.assertEqual(changed, '')


if __name__ == '__main__':
    unittest.main(verbosity=2)
