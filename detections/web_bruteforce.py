from datetime import datetime

LOG_FILE = "logs/access.log"
ALERT_FILE = "alerts.log"
THRESHOLD = 5

failed_attempts = {}

with open(LOG_FILE, "r") as file:
    for line in file:
        if "POST /login" in line or "POST /wp-login.php" in line:
            parts = line.split()
            ip = parts[0]

            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print("=== WEB BRUTEFORCE ALERTS ===")

with open(ALERT_FILE, "a") as alert_file:
    for ip, count in failed_attempts.items():
        if count >= THRESHOLD:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            alert = (
                f"[{timestamp}] ALERT: Possible web brute-force attack\n"
                f"Source IP: {ip}\n"
                f"Failed Attempts: {count}\n"
                f"Severity: MEDIUM\n"
                f"MITRE: T1110.003 - Brute Force: Web Application\n"
                f"{'-'*40}\n"
            )

            print(alert)
            alert_file.write(alert)
