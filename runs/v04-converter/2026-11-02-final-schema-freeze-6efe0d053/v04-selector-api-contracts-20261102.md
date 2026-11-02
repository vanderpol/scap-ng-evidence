# Final selector/API case contracts — Decision22 (#255/#269)

This packet closes the15 previously undocumented capabilities using32 pinned primary/source references and42 individually inventoried fields. It documents language/API contracts, not executed scanner behavior. The authoritative machine catalog is [selector-api-contracts.json](../../schema/v0.4.0/selector-api-contracts.json). The prior dated UNPROVED ledger is preserved as historical evidence.

## Scope and binding rules

Object selection uses each capability’s named API/identity namespace. Collected `require` values independently use case-sensitive `equals` or explicit `case_insensitive_equals`. Canonical enums are exact authored tokens; numeric, SID, GUID and version identities are not universal string-folding operations. No universal case flag, lowercasing pass, implicit cast, alias, default or synthetic Item is introduced.

A conditional contract is complete only when it names the authority that decides behavior and the context a provider must obtain. Filesystem directory/API rules and IIS property schemas are intentionally contextual. A provider that cannot establish that context must diagnose the acquisition limitation; it cannot guess a match or turn failed acquisition into absence. No target execution or API acceptance of undocumented alternate spellings is claimed.

The separate catalog is used to add descriptions to generated Object fields, without changing their accepted shapes or any of the100 source mappings/frozen fingerprints. The compiler retains the authored values verbatim. Existing source OVAL operation/provenance remains preserved; it is not relabeled as native runtime equivalence.

## Boundaries that matter

- IIS: `IsCaseSensitive` governs a property **value**, not every path/name component. The MWA attribute-schema name indexer documents insensitive lookup; this is not evidence for whole-expression folding in AppCmd. Section paths use registered canonical names and the selected API grammar. Undocumented alias tolerance remains unpromised. Extensible schemas are a measured runtime dependency, not a guessed global rule.
- PowerShell: command/parameter/non-dictionary member names differ from dictionary keys, arbitrary parameter values, calculated selection data and module filesystem paths. Canonical native verb enums remain exact.
- SID: Windows SID parsing and structural identity differ from account-name lookup. No assumption that lowercase `s`, SDDL aliases or localized names are accepted in place of the supplied SID. The native text remains preserved.
- WMI/WUA: the acquisition input is an embedded API language. Its grammar and string comparison rules apply inside that expression; they do not change the meaning of native collected-value `equals`.
- All selectors with operators other than API identity lookup retain their explicit existing operator semantics. A provider must enumerate/filter faithfully or report inability; API lookup must not silently replace a regex, ordered comparison or source-specific operation.

## Per-capability inventory and examples

### independent.environmentvariable

Platform: Windows, Unix-like platforms with process-environment access.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| pid | selector; numeric_identity. Numeric identity; letter case does not apply. Preserve declared integer/null meaning; do not stringify or invent a process. | `42` —  Select process identity 42 in the selected target context. | `"42"` —  A text operand is not an integer selector; no implicit conversion. |
| name | selector; platform_environment. Windows environment names compare insensitively; Unix-like environment names compare sensitively. A selected-process namespace and supplied platform must be known. Preserve bytes/spelling and values. | `"PATH"` — Unix target with PATH set Select PATH; Windows Path may also identify it. | `"path"` — Unix target has PATH but not path No matching name; do not transplant Windows casing. Access failure is an error, not this absence. |

Context and exceptions: Name lookup follows the target platform, not the scanner host or PowerShell wildcard behavior. A remote process requires an actual provider; the caller environment is not a substitute.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [env](https://learn.microsoft.com/en-us/dotnet/api/system.environment.getenvironmentvariable?view=net-10.0), [posix-env](https://pubs.opengroup.org/onlinepubs/9799919799/functions/getenv.html), [win-env](https://learn.microsoft.com/en-us/windows/win32/procthread/environment-variables).

### windows.appcmd

Platform: Windows with IIS/AppCmd and selected configuration schema.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| identifier_type | selector; canonical_enum. Use the exact native enum token in the mapping. Case variations are not native aliases. The backend maps documented constants to API arguments without rewriting authored values. | `"Site"` —  Exact declared enum member is accepted. | `"site"` —  Undeclared casing is rejected by the native enum contract. |
| identifier | selector; iis_schema_identity. Resolve the selected Site, VDir or Apppool namespace using IIS configuration key schema/API identity. Property-value casing follows that key property IsCaseSensitive; do not impose a Windows-wide insensitive rule. For listconfig Webserver, null means the already permitted server context. | `"Default Web Site"` — exact configured Site identity Select that configured site. | `"default web site"` — selected identity property schema IsCaseSensitive=true Does not match the mixed-case property. With false, the API may match; obtain the actual schema, never guess. |
| parameter | selector; iis_property_expression. Interpret the setting-location expression using the selected IIS/AppCmd schema. Property names, collection expressions and quoted key values are different components. MWA attribute-schema name lookup is documented insensitive; embedded key values use their own IsCaseSensitive. Preserve the full expression; no whole-string fold or filesystem rule. | `"processModel.identityType"` — Apppool setting supported by installed schema Resolve the named property; returned value casing is not inferred from its name. | `"processModel.notAProperty"` —  Unsupported property is an acquisition diagnostic, not a fabricated empty setting. |

Context and exceptions: IIS extension/property schemas can set IsCaseSensitive independently. A virtual directory/configuration path is not a physical filesystem path. Documentation for the MWA attribute-name indexer does not prove that every AppCmd alias or section-path casing is accepted. Use the actual selected API grammar.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [iis-appcmd](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe), [iis-attribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.web.administration.configurationattributeschemacollection.item?view=iis-dotnet), [iis-case](https://learn.microsoft.com/en-us/iis/web-development-reference/native-code-api-reference/iapphostpropertyschema-iscasesensitive-property), [iis-config](https://learn.microsoft.com/en-us/iis/get-started/planning-your-iis-architecture/introduction-to-applicationhostconfig).

### windows.appcmdlistconfig

Platform: Windows with IIS/AppCmd and selected configuration schema.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| identifier_type | selector; canonical_enum. Use the exact native enum token in the mapping. Case variations are not native aliases. The backend maps documented constants to API arguments without rewriting authored values. | `"Site"` —  Exact declared enum member is accepted. | `"site"` —  Undeclared casing is rejected by the native enum contract. |
| identifier | selector; iis_schema_identity. Resolve the selected Site, VDir or Apppool namespace using IIS configuration key schema/API identity. Property-value casing follows that key property IsCaseSensitive; do not impose a Windows-wide insensitive rule. For listconfig Webserver, null means the already permitted server context. | `"Default Web Site"` — exact configured Site identity Select that configured site. | `"default web site"` — selected identity property schema IsCaseSensitive=true Does not match the mixed-case property. With false, the API may match; obtain the actual schema, never guess. |
| parameter | selector; iis_property_expression. Interpret the setting-location expression using the selected IIS/AppCmd schema. Property names, collection expressions and quoted key values are different components. MWA attribute-schema name lookup is documented insensitive; embedded key values use their own IsCaseSensitive. Preserve the full expression; no whole-string fold or filesystem rule. | `"processModel.identityType"` — Apppool setting supported by installed schema Resolve the named property; returned value casing is not inferred from its name. | `"processModel.notAProperty"` —  Unsupported property is an acquisition diagnostic, not a fabricated empty setting. |
| section | selector; iis_section_path. Resolve a registered section path through IIS configuration API at the selected scope, preserving exact authored spelling. No universal case-insensitive alias for section paths is documented here: use registered canonical names. Unsupported section/path is an API error; do not reinterpret section syntax as a field comparison. | `"system.webServer/security/authentication/anonymousAuthentication"` —  Resolve the registered section at the selected IIS scope. | `"system.webServer/notASection"` —  Unsupported section produces an API diagnostic, not an absent collected value. |

Context and exceptions: IIS extension/property schemas can set IsCaseSensitive independently. A virtual directory/configuration path is not a physical filesystem path. Documentation for the MWA attribute-name indexer does not prove that every AppCmd alias or section-path casing is accepted. Use the actual selected API grammar.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [iis-appcmd](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe), [iis-attribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.web.administration.configurationattributeschemacollection.item?view=iis-dotnet), [iis-case](https://learn.microsoft.com/en-us/iis/web-development-reference/native-code-api-reference/iapphostpropertyschema-iscasesensitive-property), [iis-config](https://learn.microsoft.com/en-us/iis/get-started/planning-your-iis-architecture/introduction-to-applicationhostconfig), [iis-section](https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-iisa/b8ca90fd-7c8c-4e8f-9ecc-3ecf640db266).

### windows.cmdlet

Platform: Windows PowerShell/PowerShell on Windows with the selected module.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| module_name | acquisition_parameter; powershell_module_identity. PowerShell module/command names are insensitive where PowerShell defines them. Preserve canonical native verb enum spelling, which remains exact in YAML. Module filesystem discovery must honor target path rules. Null module_name leaves that existing source constraint unconstrained, never selects a fallback. | `"Microsoft.PowerShell.Management"` —  Resolve the supplied declared module/cmdlet name in its target session. | `"Missing.Module"` —  Wrong native verb enum case rejects; otherwise a missing command/module is an acquisition error. |
| verb | acquisition_parameter; powershell_command_identity. PowerShell module/command names are insensitive where PowerShell defines them. Preserve canonical native verb enum spelling, which remains exact in YAML. Module filesystem discovery must honor target path rules. Null module_name leaves that existing source constraint unconstrained, never selects a fallback. | `"Get"` —  Resolve the supplied declared module/cmdlet name in its target session. | `"get"` —  Wrong native verb enum case rejects; otherwise a missing command/module is an acquisition error. |
| noun | acquisition_parameter; powershell_command_identity. PowerShell module/command names are insensitive where PowerShell defines them. Preserve canonical native verb enum spelling, which remains exact in YAML. Module filesystem discovery must honor target path rules. Null module_name leaves that existing source constraint unconstrained, never selects a fallback. | `"Item"` —  Resolve the supplied declared module/cmdlet name in its target session. | `"NoSuchNativeCmdlet"` —  Wrong native verb enum case rejects; otherwise a missing command/module is an acquisition error. |
| module_id | acquisition_parameter; guid_identity. A supplied module GUID constrains module identity, not culture-sensitive text. Preserve its lexical form and let the documented module specification parse/resolve it; null retains the existing unconstrained meaning. Do not invent a module from an invalid GUID. | `"00000000-0000-0000-0000-000000000001"` —  Select only a module with that GUID if one is installed. | `"00000000-0000-0000-0000-000000000002"` —  A distinct GUID is not the same module, irrespective of letter casing. |
| module_version | acquisition_parameter; version_identity. The existing version domain applies, not string casing or lexicographic order; preserve explicit lexical version and null unconstrained meaning. Do not infer case rules for filenames or rewrite version operands. | `"1.2.3"` —  Constrain the selected module using the existing version specification. | `"latest"` —  Not a native lexical version; compiler rejects without conversion. |
| parameters | acquisition_parameter; powershell_record_context. Treat record member names as named cmdlet parameters for parameters, and selected output property names for select. PowerShell parameter names/non-dictionary members are insensitive; arbitrary nested dictionary keys, calculated expressions and parameter values are opaque cmdlet/provider data and retain their own comparer. Null means no supplied record, not implicit arguments. | `{"fields": {"Name": {"equals": "Example", "selection_match": "every"}}}` — a named parameter or non-dictionary output property Bind the name under the documented PowerShell name semantics; preserve its value exactly. | `{"Key": "value", "key": "other"}` — nested case-sensitive dictionary value Do not collapse distinct data keys or lowercase values. Schema shape still follows the existing object-record definition. |
| select | acquisition_parameter; powershell_record_context. Treat record member names as named cmdlet parameters for parameters, and selected output property names for select. PowerShell parameter names/non-dictionary members are insensitive; arbitrary nested dictionary keys, calculated expressions and parameter values are opaque cmdlet/provider data and retain their own comparer. Null means no supplied record, not implicit arguments. | `{"fields": {"Name": {"equals": "Example", "selection_match": "every"}}}` — a named parameter or non-dictionary output property Bind the name under the documented PowerShell name semantics; preserve its value exactly. | `{"Key": "value", "key": "other"}` — nested case-sensitive dictionary value Do not collapse distinct data keys or lowercase values. Schema shape still follows the existing object-record definition. |

Context and exceptions: Command discovery does not include arbitrary ExternalScript/Application names. Module file lookup follows filesystem rules; non-dictionary member access differs from dictionary key access. Cmdlet parameter values and dynamic/calculated selection data have their own cmdlet/provider semantics, not PowerShell name semantics.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [ps-case](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_case-sensitivity?view=powershell-7.6), [ps-modules](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module?view=powershell-7.6), [ps-select](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-object?view=powershell-7.6).

### windows.fileeffectiverights

Platform: Windows filesystem and security APIs.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| full_path | selector; filesystem_context. Resolve each path component under its containing directory, filesystem and selected Windows API case rules. Inspect effective per-directory case sensitivity; never lowercase paths. Null name selects a directory only where the existing schema permits. | `"C:\\Data\\Policy.txt"` — case-sensitive containing directory, exact stored spelling Exact spelling selects the existing target. | `"C:\\Data\\policy.txt"` — case-sensitive parent and only the mixed-case target exists The differently cased component does not identify that target. An insensitive parent can instead resolve it. |
| directory | selector; filesystem_context. Resolve each path component under its containing directory, filesystem and selected Windows API case rules. Inspect effective per-directory case sensitivity; never lowercase paths. Null name selects a directory only where the existing schema permits. | `"C:\\Data"` — case-sensitive containing directory, exact stored spelling Exact spelling selects the existing target. | `"C:\\data"` — case-sensitive parent and only the mixed-case target exists The differently cased component does not identify that target. An insensitive parent can instead resolve it. |
| name | selector; filesystem_context. Resolve each path component under its containing directory, filesystem and selected Windows API case rules. Inspect effective per-directory case sensitivity; never lowercase paths. Null name selects a directory only where the existing schema permits. | `"Policy.txt"` — case-sensitive containing directory, exact stored spelling Exact spelling selects the existing target. | `"policy.txt"` — case-sensitive parent and only the mixed-case target exists The differently cased component does not identify that target. An insensitive parent can instead resolve it. |
| trustee_sid | selector; sid_identity. Use valid SID identity in the Windows SID namespace, with API parsing and exact SID structure equality. Preserve authored text. Do not infer account-name case semantics, accept arbitrary aliases, or promise that lowercase s is valid. | `"S-1-5-32-544"` —  Select the SID for built-in Administrators, independent of localized display name. | `"S-1-5-32-545"` —  A different RID denotes a different SID; casing cannot equate the two. |
| filesystem | acquisition_parameter; canonical_enum. Explicit existing filesystem scope all/local/same is an exact native enum. It limits the search boundary independently of recursion and per-component case rules. No omitted runtime default is supplied. | `"all"` —  Use the explicit all-filesystem search boundary. | `"ALL"` —  Reject the undeclared native enum casing. |

Context and exceptions: SMB/remote filesystems and filesystem namespaces can differ; a directory flag alone is not a substitute for API semantics. Effective rights depend on the actual security descriptor/token; a localized trustee name is not a SID.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [native-acquisition](https://github.com/vanderpol/scap-ng/blob/606ffe1cf/schema/v0.4.0/capability-common.schema.json), [sid](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-equalsid), [sid-parse](https://learn.microsoft.com/en-us/windows/win32/api/sddl/nf-sddl-convertstringsidtosidw), [sid-strings](https://learn.microsoft.com/en-us/windows/win32/secauthz/sid-strings), [win-files](https://learn.microsoft.com/en-us/windows/wsl/case-sensitivity), [win-paths](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file).

### windows.group_sid

Platform: Windows security/account APIs.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| group_sid | selector; sid_identity. Use valid SID identity in the Windows SID namespace, with API parsing and exact SID structure equality. Preserve authored text. Do not infer account-name case semantics, accept arbitrary aliases, or promise that lowercase s is valid. | `"S-1-5-32-544"` —  Select the SID for built-in Administrators, independent of localized display name. | `"S-1-5-32-545"` —  A different RID denotes a different SID; casing cannot equate the two. |

Context and exceptions: SID structure identity is independent from account display-name spelling or localization. Unresolved SID/account lookup and denied access must be diagnosed, not fabricated as absent accounts.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [sid](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-equalsid), [sid-parse](https://learn.microsoft.com/en-us/windows/win32/api/sddl/nf-sddl-convertstringsidtosidw), [sid-strings](https://learn.microsoft.com/en-us/windows/win32/secauthz/sid-strings).

### windows.sid_sid

Platform: Windows security/account APIs.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| trustee_sid | selector; sid_identity. Use valid SID identity in the Windows SID namespace, with API parsing and exact SID structure equality. Preserve authored text. Do not infer account-name case semantics, accept arbitrary aliases, or promise that lowercase s is valid. | `"S-1-5-32-544"` —  Select the SID for built-in Administrators, independent of localized display name. | `"S-1-5-32-545"` —  A different RID denotes a different SID; casing cannot equate the two. |
| include_group | acquisition_parameter; boolean_control. Include matching groups in the acquired account population. It is an explicit Boolean, not a case policy or hidden runtime default. | `true` —  Explicitly enable the documented acquisition behavior. | `"true"` —  A string is not the Boolean; no truthy conversion or omitted default. |
| resolve_group | acquisition_parameter; boolean_control. Recursively resolve group membership only when explicitly requested. It is an explicit Boolean, not a case policy or hidden runtime default. | `true` —  Explicitly enable the documented acquisition behavior. | `"true"` —  A string is not the Boolean; no truthy conversion or omitted default. |

Context and exceptions: SID structure identity is independent from account display-name spelling or localization. Unresolved SID/account lookup and denied access must be diagnosed, not fabricated as absent accounts.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [account](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-lookupaccountnamew), [oval-windows](https://github.com/vanderpol/scap-ng/blob/606ffe1cf/third_party/scap-1.4-schemas/oval_5.12.3/windows-definitions-schema.xsd), [sid](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-equalsid), [sid-parse](https://learn.microsoft.com/en-us/windows/win32/api/sddl/nf-sddl-convertstringsidtosidw), [sid-strings](https://learn.microsoft.com/en-us/windows/win32/secauthz/sid-strings).

### windows.user_sid

Platform: Windows security/account APIs.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| user_sid | selector; sid_identity. Use valid SID identity in the Windows SID namespace, with API parsing and exact SID structure equality. Preserve authored text. Do not infer account-name case semantics, accept arbitrary aliases, or promise that lowercase s is valid. | `"S-1-5-32-544"` —  Select the SID for built-in Administrators, independent of localized display name. | `"S-1-5-32-545"` —  A different RID denotes a different SID; casing cannot equate the two. |

Context and exceptions: SID structure identity is independent from account display-name spelling or localization. Unresolved SID/account lookup and denied access must be diagnosed, not fabricated as absent accounts.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [sid](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-equalsid), [sid-parse](https://learn.microsoft.com/en-us/windows/win32/api/sddl/nf-sddl-convertstringsidtosidw), [sid-strings](https://learn.microsoft.com/en-us/windows/win32/secauthz/sid-strings).

### windows.ntuser

Platform: Windows loaded/offline NTUSER.DAT profile hives.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| key | selector; registry_identity. Registry key/value-name identity is case-insensitive in the Registry API. Preserve spelling and registry view. Empty value name requests the default value; null name/key is structural only where already allowed, not a wildcard. | `"Software\\Vendor"` —  Resolves the same key/value identity as its lower-case spelling in the same hive/view. | `"Software\\Other"` —  Different name selects a different identity; failed access cannot establish absence. |
| name | selector; registry_identity. Registry key/value-name identity is case-insensitive in the Registry API. Preserve spelling and registry view. Empty value name requests the default value; null name/key is structural only where already allowed, not a wildcard. | `"Setting"` —  Resolves the same key/value identity as its lower-case spelling in the same hive/view. | `"OtherSetting"` —  Different name selects a different identity; failed access cannot establish absence. |
| include_default | acquisition_parameter; boolean_control. Include the local Default user profile hive only when explicitly enabled. It is an explicit Boolean, not a case policy or hidden runtime default. | `true` —  Explicitly enable the documented acquisition behavior. | `"true"` —  A string is not the Boolean; no truthy conversion or omitted default. |
| item_creation | acquisition_parameter; canonical_enum. Use exact existing key_and_name_exist/every_ntuser tokens. These choose the source acquisition population; they do not authorize fabricated Items or make failed hive reads into absence. | `"key_and_name_exist"` —  Use the already specified source population policy. | `"KEY_AND_NAME_EXIST"` —  No case alias; reject the undeclared enum token. |

Context and exceptions: Registry key/value identity remains insensitive even if the backing profile path is case-sensitive. Default-user profile inclusion and key/name versus every-ntuser population policy are independent explicit controls. Unavailable/locked hive or denied profile access is collection failure, not proven missing key/value.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [ntuser](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives), [oval-windows](https://github.com/vanderpol/scap-ng/blob/606ffe1cf/third_party/scap-1.4-schemas/oval_5.12.3/windows-definitions-schema.xsd), [registry](https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry), [registry-value](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.registry.getvalue?view=net-10.0).

### windows.regkeyeffectiverights

Platform: Windows Registry and security APIs.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| hive | selector; canonical_enum. Use the exact native enum token in the mapping. Case variations are not native aliases. The backend maps documented constants to API arguments without rewriting authored values. | `"local_machine"` —  Exact declared enum member is accepted. | `"local_machine"` —  Undeclared casing is rejected by the native enum contract. |
| key | selector; registry_identity. Registry key/value-name identity is case-insensitive in the Registry API. Preserve spelling and registry view. Empty value name requests the default value; null name/key is structural only where already allowed, not a wildcard. | `"Software\\Vendor"` —  Resolves the same key/value identity as its lower-case spelling in the same hive/view. | `"Software\\Other"` —  Different name selects a different identity; failed access cannot establish absence. |
| trustee_sid | selector; sid_identity. Use valid SID identity in the Windows SID namespace, with API parsing and exact SID structure equality. Preserve authored text. Do not infer account-name case semantics, accept arbitrary aliases, or promise that lowercase s is valid. | `"S-1-5-32-544"` —  Select the SID for built-in Administrators, independent of localized display name. | `"S-1-5-32-545"` —  A different RID denotes a different SID; casing cannot equate the two. |

Context and exceptions: Hive identity uses exact native enum tokens; registry view is independent of path casing. Unresolvable trustee or inaccessible security descriptor is an error.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [registry](https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry), [registry-value](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.registry.getvalue?view=net-10.0), [sid](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-equalsid), [sid-parse](https://learn.microsoft.com/en-us/windows/win32/api/sddl/nf-sddl-convertstringsidtosidw), [sid-strings](https://learn.microsoft.com/en-us/windows/win32/secauthz/sid-strings).

### windows.service

Platform: Windows Service Control Manager.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| service_name | selector; scm_identity. SCM service-name comparison is insensitive while preserving original spelling. Resolve the service key through SCM, not the service display name. | `"Spooler"` —  Identifies the same SCM key as spooler. | `"Print Spooler"` —  A display name is not a substitute for service_name; no hidden conversion. |

Context and exceptions: service_name is the SCM key, not display_name or an executable filesystem path.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [service](https://learn.microsoft.com/en-us/windows/win32/api/winsvc/nf-winsvc-openservicew).

### windows.sid

Platform: Windows account/security authority.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| trustee_name | selector; windows_account_identity. Windows trustee-name identity is insensitive as documented in the pinned OVAL source for LookupAccountName-style resolution. Resolve in the target authority/domain and preserve spelling; do not use an unrelated host account or a generic Unicode casefold surrogate. | `"CONTOSO\\Alice"` —  Select the same target account identity as contoso\alice. | `"OTHER\\Alice"` —  A different authority can identify a different principal; case folding does not erase domain context. |
| include_group | acquisition_parameter; boolean_control. Include matching groups only when explicitly enabled. It is an explicit Boolean, not a case policy or hidden runtime default. | `true` —  Explicitly enable the documented acquisition behavior. | `"true"` —  A string is not the Boolean; no truthy conversion or omitted default. |
| resolve_group | acquisition_parameter; boolean_control. Recursively resolve groups only when explicitly enabled. It is an explicit Boolean, not a case policy or hidden runtime default. | `true` —  Explicitly enable the documented acquisition behavior. | `"true"` —  A string is not the Boolean; no truthy conversion or omitted default. |

Context and exceptions: Use qualified domain/computer trustee names to avoid ambiguous isolated lookups. Account names, SID identity and returned display-name comparisons are separate.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [account](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-lookupaccountnamew), [oval-windows](https://github.com/vanderpol/scap-ng/blob/606ffe1cf/third_party/scap-1.4-schemas/oval_5.12.3/windows-definitions-schema.xsd).

### windows.userright

Platform: Windows LSA policy/security APIs.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| userright | selector; canonical_enum. Use the exact native enum token in the mapping. Case variations are not native aliases. The backend maps documented constants to API arguments without rewriting authored values. | `"SE_BACKUP_NAME"` —  Exact declared enum member is accepted. | `"se_backup_name"` —  Undeclared casing is rejected by the native enum contract. |

Context and exceptions: Native SE_*_NAME catalog tokens identify documented privilege/logon-right constants; localized display labels and API Se... strings are not interchangeable authored aliases. Do not infer a common arbitrary-string case rule from the underlying privilege lookup function.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [account-rights](https://learn.microsoft.com/en-us/windows/win32/secauthz/account-rights-constants), [oval-windows](https://github.com/vanderpol/scap-ng/blob/606ffe1cf/third_party/scap-1.4-schemas/oval_5.12.3/windows-definitions-schema.xsd), [rights](https://learn.microsoft.com/en-us/windows/win32/secauthz/privilege-constants).

### windows.wmi.query

Platform: Windows WMI WQL in the explicitly supplied namespace.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| namespace | acquisition_parameter; wmi_namespace_identity. Use the Windows WMI namespace/object-path namespace through the WMI API, preserving authored text and server scope; namespace names are insensitive in Windows WMI, not filesystem paths. Do not assume generic CIM or non-Windows query engines share this contract. | `"ROOT\\CIMV2"` —  The Windows WMI namespace identity is the same as root\cimv2. | `"root\\OtherNamespace"` —  Different namespace is not an alias; unavailable namespace is diagnosed. |
| query | acquisition_parameter; wql_grammar. Pass WQL as a query language expression without whole-query case rewriting. Windows WQL names/keywords and documented string relation comparisons are insensitive; preserve quoted text, escaping, typed operands and operator grammar. Result require record fields retain their own explicit collected-value comparisons. | `"SELECT Name FROM Win32_Process WHERE Name = 'notepad.exe'"` —  Use WQL string comparison behavior, not native require.equals behavior. | `"SELECT Name FROM Win32_Process WHERE ProcessId = 'not-a-number'"` —  Invalid type/operator/query is an API diagnostic, not absence. |

Context and exceptions: WQL is not a general SQL engine and does not support arbitrary cross-namespace expressions. A provider requiring undocumented casing is a provider conformance defect, not a new native case switch. An unavailable namespace/provider/query failure is an error, not an empty result or a fabricated record.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [wmi-grammar](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wmi/cf0410f3-541f-477a-848f-9133a1272725), [wmi-interface](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wmi/7a50647a-5311-41c2-8f4f-83bcfb497877), [wmi-path](https://learn.microsoft.com/en-us/windows/win32/wmisdk/describing-the-location-of-a-wmi-object), [wmi-path-rules](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-object-path-requirements), [wmi-query](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wmi/6c8a38f4-4ee1-47cb-99f1-b42718a575ce).

### windows.wuaupdatesearcher

Platform: Windows Update Agent Search API.

| Field | Role / case contract | Positive example | Negative / boundary example |
| --- | --- | --- | --- |
| search_criteria | selector; wua_criteria_grammar. Interpret as the Windows Update Search criteria language. Its string comparisons are insensitive unless the supported criterion specifies otherwise; respect the documented Boolean grammar and escaping. Preserve the whole expression and do not lowercase it or apply native field.equals to query source text. | `"Type='Software' and IsInstalled=0"` —  Apply WUA criterion semantics; Software/software compare under its documented string rule. | `"IsInstalled=0 and (IsHidden=0 or Type='Software')"` —  Nested OR violates documented criteria grammar; return a query diagnostic, not no updates. |
| include_superseded_updates | acquisition_parameter; boolean_control. Control whether potentially superseded matching updates are included. It is an explicit Boolean, not a case policy or hidden runtime default. | `true` —  Explicitly enable the documented acquisition behavior. | `"true"` —  A string is not the Boolean; no truthy conversion or omitted default. |

Context and exceptions: Criteria expression strings are not arbitrary SQL and property-specific restrictions remain in force. Search service selection/permissions and available update catalog affect population, not case semantics.

Object Set/filters and optional traversal keep existing explicit schema semantics. Traversal depth/kind do not change per-component identity. object_title and capability are identity/presentation, not case controls. Generic for_each preserves its existing explicit binding/expansion contract; it is not an identifier case flag. Optional traversal max_depth and platform recurse enums remain literal controls, never a path-name comparison.

References: [oval-windows](https://github.com/vanderpol/scap-ng/blob/606ffe1cf/third_party/scap-1.4-schemas/oval_5.12.3/windows-definitions-schema.xsd), [wua](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nf-wuapi-iupdatesearcher-search), [wua-superseded](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nf-wuapi-iupdatesearcher-get_includepotentiallysupersededupdates).

## Verification and remaining limits

The independent contract auditor derives fields from both mappings and generated Object schemas, validates source receipts and explicit per-field context, and detects missing selectors/parameters, wrong roles, broken provenance, generic SID folding and incomplete examples. Eight focused tests include a15-capability authoring/compiler integration fixture, negative native enum/Boolean/version/universal-flag cases, and mutation tests. Examples describe expected **contract** behavior; they are not fabricated API test results.

Actual Windows/Unix provider execution, permissions, remote process enumeration, IIS schema discovery, PowerShell invocation, WMI provider conformance and WUA catalogs remain runtime qualification. Their absence does not invent another language vote. Unknown undocumented aliases are not approved behavior; no scanner may infer them. Native Result A, explicit Input-presence guards, compatible datatypes and all prior proofs remain unchanged.
