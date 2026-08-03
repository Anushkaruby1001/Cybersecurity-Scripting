import re
from collections import Counter

# Read log file
with open("security.log", "r") as file:
    content = file.read()

# Regular Expressions
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", content)
emails = re.findall(r"\w+@\w+\.\w+", content)
dates = re.findall(r"\d{4}-\d{2}-\d{2}", content)
times = re.findall(r"\d{2}:\d{2}:\d{2}", content)
urls = re.findall(r"https?://[^\s]+", content)
users = re.findall(r"User:\s*(\w+)", content)

failed_logins = re.findall(r"Failed login", content, re.IGNORECASE)
success_logins = re.findall(r"Login Successful", content, re.IGNORECASE)

severity = re.findall(r"INFO|WARNING|ERROR|CRITICAL", content, re.IGNORECASE)

ports = re.findall(r":(\d{1,5})", content)

sql = re.findall(
    r"union|select|drop|insert|delete|' or '1'='1|--",
    content,
    re.IGNORECASE
)

xss = re.findall(
    r"<script>|javascript:|onerror=|onload=",
    content,
    re.IGNORECASE
)

commands = re.findall(
    r"powershell|cmd\.exe|bash|curl|wget|nc|netcat",
    content,
    re.IGNORECASE
)

files = re.findall(
    r"\b[\w.-]+\.(?:exe|dll|pdf|zip|docx|txt|js|php|bat)\b",
    content,
    re.IGNORECASE
)

# Counters
ip_counter = Counter(ips)
severity_counter = Counter([s.upper() for s in severity])

# Display Report
print("=" * 50)
print("      MINI SOC LOG ANALYZER")
print("=" * 50)

print("\nTop 5 Active IPs")
for ip, count in ip_counter.most_common(5):
    print(f"{ip} -> {count} events")

print("\nPrivate/Public IPs")
for ip in set(ips):
    if ip.startswith(("10.", "192.168.", "172.")):
        print(f"{ip} -> Private")
    else:
        print(f"{ip} -> Public")

print("\nEmail Addresses")
for email in sorted(set(emails)):
    print(email)

print("\nUsernames")
for user in sorted(set(users)):
    print(user)

print("\nURLs")
for url in sorted(set(urls)):
    print(url)

print("\nFiles")
for f in sorted(set(files)):
    print(f)

print("\nPorts")
print(", ".join(sorted(set(ports))))

print("\nDates")
print(", ".join(sorted(set(dates))))

print("\nTimes")
print(", ".join(sorted(set(times))))

print("\nSeverity Report")
for level, count in severity_counter.items():
    print(f"{level}: {count}")

print("\nSecurity Events")
print(f"Failed Logins      : {len(failed_logins)}")
print(f"Successful Logins  : {len(success_logins)}")
print(f"Possible SQLi      : {len(sql)}")
print(f"Possible XSS       : {len(xss)}")
print(f"Suspicious Commands: {len(commands)}")

print("\nSuspicious Commands Found")
for cmd in sorted(set(commands)):
    print(cmd)

print("\nBrute Force Check")
for ip, count in ip_counter.items():
    if count >= 5:
        print(f"{ip} -> High Activity ({count} events)")

print("\nSummary")
print("-" * 50)
print(f"Total IPs          : {len(ips)}")
print(f"Unique IPs         : {len(set(ips))}")
print(f"Emails             : {len(emails)}")
print(f"Users              : {len(users)}")
print(f"URLs               : {len(urls)}")
print(f"Files              : {len(files)}")
print(f"Ports              : {len(set(ports))}")
print(f"Dates              : {len(set(dates))}")
print(f"Times              : {len(set(times))}")

# Save report
with open("report.txt", "w") as report:
    report.write("MINI SOC LOG ANALYZER REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write("Top IPs\n")
    for ip, count in ip_counter.most_common():
        report.write(f"{ip} -> {count}\n")

    report.write("\nSeverity Report\n")
    for level, count in severity_counter.items():
        report.write(f"{level}: {count}\n")

    report.write(f"\nFailed Logins: {len(failed_logins)}")
    report.write(f"\nSuccessful Logins: {len(success_logins)}")
    report.write(f"\nSQLi Attempts: {len(sql)}")
    report.write(f"\nXSS Attempts: {len(xss)}")

print("\nReport saved successfully as report.txt")