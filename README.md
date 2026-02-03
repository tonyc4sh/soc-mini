# SOC Mini Project – Detection & Reporting

## Project Overview

This project is a **mini SOC-style detection and reporting framework** built to simulate how a Security Operations Center detects, enriches, and reports security incidents based on log analysis.

The goal of this project is **not automation at scale**, but to demonstrate **SOC analyst thinking**:
- log analysis
- threat detection logic
- alert enrichment
- MITRE ATT&CK mapping
- operational reporting

---

##  Implemented Detections

### SSH Brute Force Detection
- Analyzes `auth.log`
- Counts failed SSH login attempts per IP
- Generates alert when threshold is exceeded

**MITRE ATT&CK:**  
- T1110 – Brute Force  
**Severity:** HIGH

---

### Web Brute Force Detection
- Analyzes `access.log`
- Detects repeated failed login attempts (`POST /login`)
- Threshold-based detection

**MITRE ATT&CK:**  
- T1110.003 – Brute Force: Web Application  
**Severity:** MEDIUM

---

### Suspicious User-Agent Detection
- Behavioral detection (no thresholds)
- Uses regex to identify automated tools such as:
  - sqlmap
  - nikto
  - curl
  - wget
  - python-requests
  - missing User-Agent (`"-"`)

**MITRE ATT&CK:**  
- T1071 – Application Layer Protocol  
**Severity:** MEDIUM

---

## Alert Enrichment

Each alert includes:
- timestamp
- detection type
- source IP
- severity
- MITRE ATT&CK technique
- contextual details (failed attempts / User-Agent)

Alerts are written to:
- terminal output
- `alerts.log`

---

## Reporting

After detections are executed, alerts are parsed and normalized into structured reports.

### JSON Alerts
`output/alerts.json`
- unified alert schema
- ready for SIEM / dashboard ingestion

### Daily Summary Report
`output/summary_report.txt`
- total alerts
- alerts by severity
- top source IPs

This simulates **SOC daily operational reporting**.

---

## How to Run

1. Generate alerts:
```bash
python3 detections/ssh_bruteforce.py
python3 detections/web_bruteforce.py
python3 detections/suspicious_user_agent.py
```
2. Generate reports:
```bash
python3 reporting/generate_report.py
```

