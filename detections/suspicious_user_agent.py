import re
from datetime import datetime

LOG_FILE = "logs/access.log"
ALERT_FILE = "alerts.log"

# Regex for suspicious User-Agents
SUSPICIOUS_UA_REGEX = re.compile(
    r"(sqlmap|nikto|curl|wget|python|python-requests)",
    re.IGNORECASE
)

print("=== SUSPICIOUS USER-AGENT ALERTS ===")

with open(LOG_FILE, "r") as file, open(ALERT_FILE, "a") as alert_file:
    for line in file:
        # Extract IP (first field)
        ip = line.split()[0]

        # Extract User-Agent (last quoted field)
        match = re.findall(r'"([^"]*)"', line)
        if not match:
            continue

        user_agent = match[-1]

        # Empty or dash UA
        if user_agent == "-" or SUSPICIOUS_UA_REGEX.search(user_agent):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            alert = (
                f"[{timestamp}] ALERT: Suspicious User-Agent detected\n"
                f"Source IP: {ip}\n"
                f"User-Agent: {user_agent}\n"
                f"Severity: MEDIUM\n"
                f"MITRE: T1071 - Application Layer Protocol\n"
                f"{'-'*40}\n"
            )

            print(alert)
            alert_file.write(alert)
