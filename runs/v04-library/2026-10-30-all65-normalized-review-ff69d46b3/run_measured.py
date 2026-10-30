import json
from pathlib import Path
import resource
import runpy
import sys
import time

output=Path(sys.argv[1]);command=sys.argv[2:];sys.argv=command
sys.path.insert(0,str(Path(command[0]).resolve().parent))
started=time.perf_counter();code=0
try:runpy.run_path(command[0],run_name='__main__')
except SystemExit as error:code=error.code or 0
finally:
    output.write_text(json.dumps({'seconds':time.perf_counter()-started,
        'peak_rss_kib_linux':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'exit_code':code,'command':command},indent=2)+'\n')
raise SystemExit(code)
