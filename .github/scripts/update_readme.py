import os

arr = []

def count_lines(file_path):
    files_dict = {}
    for root, dirs, files in os.walk(file_path):
        for filename in files:
            if filename.endswith(".rules"):
                filepath = os.path.join(root, filename)
                with open(filepath) as file:
                    num_lines = sum(1 for line in file)
                    files_dict[filename] = num_lines

    sorted_files = sorted(files_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(10):
        if i >= len(sorted_files):
            arr.append(f"|  |  |")
        else:
            arr.append(f"| {sorted_files[i][0]} | {sorted_files[i][1]} |")
    return arr

if __name__ == "__main__":
    print("""# Suricata Rules

This repository contains a large collection of rules for the Suricata intrusion detection system (IDS). Suricata is an open-source network IDS that can detect a wide range of threats, including malware, exploits, and other malicious activity. Our rules are designed to be highly effective at detecting web application attack especially detecting latest CVEs.

> This repository is heavily influenced by `nuclei-templates` repository by ProjectDiscovery

# Usage

`main.py` will merge all rules into one file

```python
python3 main.py --path=/path/to/rules
```

# Suricata Rules Statistics

| Rules | Count |
| ----- | ----- |""")

for rules in count_lines("."):
    print(rules)

print("""\n# To-Do

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

""")