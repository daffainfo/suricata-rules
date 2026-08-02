# Suricata Rules

This repository contains a large collection of rules for the Suricata intrusion detection system (IDS). Suricata is an open-source network IDS that can detect a wide range of threats, including malware, exploits, and other malicious activity. Our rules are designed to be highly effective at detecting web application attack especially detecting latest CVEs.

> This repository is heavily influenced by `nuclei-templates` repository by ProjectDiscovery

# Usage

`main.py` will merge all rules into one file

```python
python3 main.py --path=/path/to/rules
```

# Suricata Rules Statistics

| Rules | Count |
| ----- | ----- |
| CVE-2021.rules | 49 |
| CVE-2019.rules | 49 |
| CVE-2025.rules | 47 |
| CVE-2026.rules | 46 |
| CVE-2018.rules | 46 |
| CVE-2023.rules | 46 |
| CVE-2022.rules | 45 |
| CVE-2020.rules | 45 |
| CVE-2024.rules | 44 |
| CVE-2017.rules | 33 |

# Rule Conventions

### SID allocation

| Range | Category |
| ----- | -------- |
| `1YYYYNNN` | `cnvd` (e.g. `12021001` = CNVD-2021, rule 001) |
| `2YYYYNNN` | `cves` (e.g. `22023001` = CVE-2023, rule 001) |
| `30000000+` | `default-logins` |
| `40000000+` | `miscellaneous` |
| `50000000+` | `tools` |
| `50100000` - `51400999` | `web-attacks` (one block per attack class) |
| `60000000+` | `vulnerabilities` |

### Writing matches against the right buffer

Suricata's `http_uri` is the **normalized** URI, not the bytes on the wire. With the
default `IDS` personality libhtp will, before your rule ever sees the buffer:

- percent-decode the path *and* the query (`%3Cscript` becomes `<script`)
- **lowercase the path** (`/Dialog/FileDialog.aspx` becomes `/dialog/filedialog.aspx`)
- convert backslashes to forward slashes and collapse repeated separators
- remove RFC 3986 dot-segments **from the path** (`/a/../b` becomes `/b`)

Practical consequences when adding a rule:

- Match payloads in their **decoded** form, and add `nocase` to every `http_uri` match.
- `../` survives in the **query string** but is removed from the **path**. To match
  traversal in the path, or any percent-encoded form, use `http_raw_uri`.
- `http_client_body` is raw: it is neither decoded nor lowercased, and `+` is not
  converted to a space.

# To-Do

- [x] Add more [cnvd](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/cnvd) rules
- [x] Add more [cves](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/cves) rules
- [x] Add more [default-logins](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/default-logins) rules
- [x] Add more [miscellaneous](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/miscellaneous) rules
- [x] Add more [vulnerabilities](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/vulnerabilities) rules
- [ ] Add more `Malware` rules
- [x] Add `URL Reference`
- [x] Add more web application attack rules (e.g. `SQL Injection`, `XSS`, etc)

# Contributors

You can contribute to this repository by adding new rules or you can update the existing rules

<p align="center">
<a href="https://github.com/daffainfo/suricata-rules/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=daffainfo/suricata-rules&max=25">
</a>
</p>


