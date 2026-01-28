# Mini SOC Detection Project

## Project Overview
This project is a mini SOC-style detection framework focused on identifying brute-force attacks by analyzing system and application logs.

The goal of this repository is to demonstrate core SOC Level 1 skills such as:
- log analysis
- detection logic development
- threshold-based alerting
- MITRE ATT&CK mapping
- structured alert generation

The project is designed as a portfolio project for entry-level SOC / cybersecurity roles.

---

## Implemented Detections

### 1. SSH Brute-Force Detection
**Log source:** `auth.log`

The detection identifies SSH brute-force attacks by:
- parsing authentication logs
- counting failed SSH login attempts per source IP
- triggering an alert when a threshold is exceeded

**Detection details:**
- Threshold: 10 failed login attempts
- Severity: HIGH
- MITRE ATT&CK:
  - T1110 – Brute Force
  - Tactic: Credential Access

---

### 2. Web Application Brute-Force Detection
**Log source:** `access.log`

This detection identifies brute-force attempts against web login endpoints by:
- analyzing HTTP access logs
- detecting repeated failed POST authentication attempts
- aggregating failures per source IP

**Detection details:**
- Detection logic:
  - HTTP method: POST
  - HTTP status code: 401 (Unauthorized)
- Threshold: 5 failed login attempts
- Severity: MEDIUM
- MITRE ATT&CK:
  - T1110.003 – Brute Force: Web Application

---

## Alert Output
All detections generate structured alerts containing:
- timestamp
- source IP address
- number of failed attempts
- severity level
- MITRE ATT&CK technique

Alerts are printed to stdout and appended to `alerts.log`.

### Example Alert
[2026-01-26 04:45:12] ALERT: Possible web brute-force attack
Source IP: 192.168.1.50
Failed Attempts: 5
Severity: MEDIUM
MITRE: T1110.003 - Brute Force: Web Application

---

## How to Run

### Requirements
- Python 3.14

### SSH Brute-Force Detection
```bash
python3 detections/ssh_bruteforce.py
python3 detections/web_bruteforce.py
