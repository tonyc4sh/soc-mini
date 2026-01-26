# SSH Brute Force Detection – Mini SOC Project

## 📌 Project Overview
This project is a simple **SOC-style detection script** that analyzes SSH authentication logs (`auth.log`) to identify **possible brute-force attacks** based on repeated failed login attempts from a single IP address.

The goal of this project is to demonstrate:
- log parsing
- basic detection logic
- alert generation
- SOC-oriented thinking (severity, MITRE mapping)

This is a **junior-level / SOC L1 portfolio project**.

---

## 🔍 What the Script Does

1. Reads SSH authentication logs (`auth.log`)
2. Detects **failed SSH login attempts**
3. Counts failed attempts **per source IP**
4. Triggers an alert if a defined threshold is exceeded
5. Generates a structured alert with:
   - timestamp
   - source IP
   - number of failed attempts
   - severity level
   - MITRE ATT&CK technique
6. Saves alerts to a log file (`alerts.log`)

---

## 🚨 Detection Logic

- **Threshold:** 10 failed SSH login attempts from a single IP
- **Detection type:** SSH brute-force
- **Severity:** HIGH
- **MITRE ATT&CK:**  
  - Technique: **T1110 – Brute Force**  
  - Tactic: Credential Access

---

## 📂 Project Structure
soc-mini/
├── logs/
│ └── auth.log
├── ssh_failed_counter.py
├── ssh_bruteforce_alert.py
├── alerts.log
└── README.md

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Place SSH logs in `logs/auth.log`
3. Run the detection script:

```bash
python3 ssh_bruteforce_alert.py

---

📄 Example Alert Output

[2026-01-26 04:22:54] ALERT: Possible SSH brute-force attack
Source IP: 192.168.1.10
Failed attempts: 11
Severity: HIGH
MITRE: T1110 - Brute Force
--------------------------------
