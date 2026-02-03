import json
from collections import Counter
from datetime import datetime

ALERTS_LOG = "alerts.log"
JSON_OUTPUT = "output/alerts.json"
SUMMARY_OUTPUT = "output/summary_report.txt"

alerts = []

with open(ALERTS_LOG, "r") as file:
    current_alert = {}

    for line in file:
        line = line.strip()

        if line.startswith("[") and "ALERT" in line:
            current_alert["timestamp"] = line.split("]")[0][1:]
            current_alert["description"] = line.split("ALERT: ")[1]

        elif line.startswith("Source IP:"):
            current_alert["source_ip"] = line.split(": ")[1]

        elif line.startswith("Failed Attempts:"):
            current_alert["details"] = line

        elif line.startswith("User-Agent:"):
            current_alert["details"] = line

        elif line.startswith("Severity:"):
            current_alert["severity"] = line.split(": ")[1]

        elif line.startswith("MITRE:"):
            current_alert["mitre"] = line.split(": ")[1]

        elif line.startswith("-" * 10):
            # end of alert
            current_alert["detection_type"] = current_alert.get(
                "description", "Unknown"
            )
            alerts.append(current_alert)
            current_alert = {}

# Write JSON alerts
with open(JSON_OUTPUT, "w") as json_file:
    json.dump(alerts, json_file, indent=4)

# Generate summary
total_alerts = len(alerts)
by_severity = Counter(alert["severity"] for alert in alerts)
by_ip = Counter(alert["source_ip"] for alert in alerts)

with open(SUMMARY_OUTPUT, "w") as summary:
    summary.write("SOC MINI PROJECT – DAILY SUMMARY\n")
    summary.write(f"Generated: {datetime.now()}\n\n")

    summary.write(f"Total alerts: {total_alerts}\n\n")

    summary.write("Alerts by severity:\n")
    for sev, count in by_severity.items():
        summary.write(f"  {sev}: {count}\n")

    summary.write("\nTop source IPs:\n")
    for ip, count in by_ip.most_common(5):
        summary.write(f"  {ip}: {count}\n")

print("Report generated:")
print(f"- {JSON_OUTPUT}")
print(f"- {SUMMARY_OUTPUT}")
