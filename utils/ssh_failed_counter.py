file = open("logs/auth.log", "r")

failed_logins = {}

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

print("Failed SSH login attempts:")
for ip in failed_logins:
    print(ip, "->", failed_logins[ip])
