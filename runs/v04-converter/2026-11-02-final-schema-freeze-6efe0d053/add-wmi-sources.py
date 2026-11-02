exec(open('/workspace/freeze-closure-268-20261102/research.py').read().split('rows=list(')[0])
S={
'wmi-identity':'archive/msdn-magazine/2000/may/windows-management-instrumentation-administering-windows-and-applications-across-your-enterprise',
'wmi-interface':'openspecs/windows_protocols/ms-wmi/7a50647a-5311-41c2-8f4f-83bcfb497877',
'wmi-path-rules':'windows/win32/wmisdk/wmi-object-path-requirements'}
rows=list(ThreadPoolExecutor(max_workers=3).map(get,S.items()));(W/'wmi-source-receipts.json').write_text(json.dumps(rows,indent=2)+'\n');print([(r['id'],r['status']) for r in rows])
