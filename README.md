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
| linux-structures.rules | 16 |
| CNVD-2021.rules | 10 |
| CVE-2008.rules | 9 |
| CVE-2013.rules | 8 |
| CNVD-2020.rules | 5 |
| miscellaneous.rules | 4 |
| CVE-2020.rules | 4 |
| CVE-2002.rules | 4 |
| CVE-2007.rules | 4 |
| cross-site-scripting.rules | 3 |

# To-Do

- [ ] Add more [cvnd](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/cvnd) rules
- [ ] Add more [cves](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/cves) rules
- [ ] Add more [default-logins](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/default-logins) rules
- [ ] Add more [miscellaneous](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/miscellaneous) rules
- [ ] Add more [vulnerabilities](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/vulnerabilities) rules
- [ ] Add more `Malware` rules
- [ ] Add `URL Reference`
- [ ] Add more web application attack rules (e.g. `SQL Injection`, `XSS`, etc)

# Contributors

You can contribute to this repository by adding new rules or you can update the existing rules

<p align="center">
<a href="https://github.com/daffainfo/suricata-rules/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=daffainfo/suricata-rules&max=25">
</a>
</p>


