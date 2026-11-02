from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen,Request
from html.parser import HTMLParser
from hashlib import sha256
import json,re,datetime
W=Path('/workspace/freeze-closure-268-20261102');D=W/'primary-documents';D.mkdir(exist_ok=True)
BASE='https://learn.microsoft.com/en-us/'
S={
'env':'dotnet/api/system.environment.getenvironmentvariable?view=net-10.0',
'posix-env':'https://pubs.opengroup.org/onlinepubs/9799919799/functions/getenv.html',
'win-env':'windows/win32/procthread/environment-variables',
'iis-appcmd':'iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe',
'iis-case':'iis/web-development-reference/native-code-api-reference/iapphostpropertyschema-iscasesensitive-property',
'iis-attribute':'dotnet/api/microsoft.web.administration.configurationattributeschemacollection.item?view=iis-dotnet',
'iis-config':'iis/get-started/planning-your-iis-architecture/introduction-to-applicationhostconfig',
'iis-section':'openspecs/windows_protocols/mc-iisa/b8ca90fd-7c8c-4e8f-9ecc-3ecf640db266',
'ps-case':'powershell/module/microsoft.powershell.core/about/about_case-sensitivity?view=powershell-7.6',
'ps-modules':'powershell/module/microsoft.powershell.core/import-module?view=powershell-7.6',
'ps-select':'powershell/module/microsoft.powershell.utility/select-object?view=powershell-7.6',
'win-files':'windows/wsl/case-sensitivity',
'win-paths':'windows/win32/fileio/naming-a-file',
'sid':'windows/win32/api/securitybaseapi/nf-securitybaseapi-equalsid',
'sid-strings':'windows/win32/secauthz/sid-strings',
'sid-parse':'windows/win32/api/sddl/nf-sddl-convertstringsidtosidw',
'account':'windows/win32/api/winbase/nf-winbase-lookupaccountnamew',
'registry':'windows/win32/sysinfo/structure-of-the-registry',
'registry-value':'dotnet/api/microsoft.win32.registry.getvalue?view=net-10.0',
'ntuser':'windows/win32/sysinfo/registry-hives',
'service':'windows/win32/api/winsvc/nf-winsvc-openservicew',
'rights':'windows/win32/secauthz/privilege-constants',
'account-rights':'windows/win32/secauthz/account-rights-constants',
'wmi-path':'windows/win32/wmisdk/describing-the-location-of-a-wmi-object',
'wmi-query':'openspecs/windows_protocols/ms-wmi/6c8a38f4-4ee1-47cb-99f1-b42718a575ce',
'wmi-grammar':'openspecs/windows_protocols/ms-wmi/cf0410f3-541f-477a-848f-9133a1272725',
'wua':'windows/win32/api/wuapi/nf-wuapi-iupdatesearcher-search',
'wua-superseded':'windows/win32/api/wuapi/nf-wuapi-iupdatesearcher-get_includepotentiallysupersededupdates',
}
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip:self.parts.append(d)
def get(pair):
 key,path=pair;url=path if path.startswith('http') else BASE+path
 try:
  raw=urlopen(Request(url,headers={'User-Agent':'SCAP-NG-contract-research/0.4'}),timeout=25).read();p=Text();p.feed(raw.decode());text=re.sub(r'\s+',' ',' '.join(p.parts));(D/(key+'.txt')).write_text(text);(D/(key+'.html')).write_bytes(raw)
  return {'id':key,'url':url,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':sha256(raw).hexdigest(),'bytes':len(raw),'status':'retrieved'}
 except Exception as e:return {'id':key,'url':url,'status':'failed','error':str(e)}
rows=list(ThreadPoolExecutor(max_workers=8).map(get,S.items()));(W/'source-receipts.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['id'],r['status'],r.get('error',''),flush=True)
