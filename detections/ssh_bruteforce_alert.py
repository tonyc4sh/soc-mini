from datetime import datetime

file = open("logs/auth.log", "r")

failed_logins = {}

ALERT_THRESHOLD = 10

for line in file:
    
    if "Failed Password" in line or "Failed password" in line:

        parts = line.split()

        if "from" in parts:
            ip_position = parts.index("from") + 1
            ip = parts[ip_position]

            if ip in failed_logins:
                failed_logins[ip] = failed_logins[ip] + 1
            else:
                failed_logins[ip] = 1

file.close()

alert_file = open("alerts.log", "w")

print("=== SSH BRUTEFORCE ALERTS ===")

for ip in failed_logins:
    count = failed_logins[ip]

    if count >= ALERT_THRESHOLD:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        severity = "HIGH"
        mitre = "T1110 - Brute Force"

        alert = (
            f"[{timestamp}] ALERT: Possible SSH brute-force attack\n"
            f"Source IP: {ip}\n"
            f"Failed Attempts: {count}\n"
            f"Severity: {severity}\n"
            f"MITRE: {mitre}\n"
            f"--------------------------------"
        )
        print(alert)
        alert_file.write(alert + "\n")

alert_file.close()