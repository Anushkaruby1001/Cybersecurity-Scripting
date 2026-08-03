import re
from collections import Counter

# Read log file
with open("security.log", "r") as file:
    content = file.read()

# Regular Expressions
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", content)
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", content)
dates = re.findall(r"\d{4}-\d{2}-\d{2}", content)
times = re.findall(r"\d{2}:\d{2}:\d{2}", content)
urls = re.findall(r"https?://[^\s]+", content)
domains = re.findall(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b", content)
ports = re.findall(r":(\d{1,5})", content)
users = re.findall(r"User:\s*(\w+)", content)
failed = re.findall(r"Failed login", content, re.IGNORECASE)
severity = re.findall(r"INFO|WARNING|ERROR|CRITICAL", content, re.IGNORECASE)
sql = re.findall(r"union|select|drop|delete|insert|' or '1'='1|--", content, re.IGNORECASE)
xss = re.findall(r"<script>|javascript:|onerror=|onload=", content, re.IGNORECASE)
commands = re.findall(r"powershell|cmd\.exe|bash|curl|wget|nc", content, re.IGNORECASE)
hashes = re.findall(r"\b[a-fA-F0-9]{32,64}\b", content)

# Counters
ip_counter = Counter(ips)
severity_counter = Counter(map(str.upper, severity))

# Print Report
print("=" * 50)
print("      MINI SOC LOG ANALYZER")
print("=" * 50)

print("\nUnique IP Addresses")
for ip in sorted(set(ips)):
    print(ip)

print("\nTop 5 Active IPs")
for ip, count in ip_counter.most_common(5):
    print(f"{ip} -> {count} events")

print("\nPrivate/Public IPs")
for ip in sorted(set(ips)):
    if ip.startswith(("10.", "192.168.", "172.")):
        print(f"{ip} -> Private")
    else:
        print(f"{ip} -> Public")

print("\nEmails")
for email in sorted(set(emails)):
    print(email)

print("\nUsernames")
for user in sorted(set(users)):
    print(user)

print("\nDomains")
for domain in sorted(set(domains)):
    print(domain)

print("\nURLs")
for url in sorted(set(urls)):
    print(url)

print("\nPorts")
print(", ".join(sorted(set(ports))))

print("\nDates")
print(", ".join(sorted(set(dates))))

print("\nTimes")
print(", ".join(sorted(set(times))))

print("\nHashes")
for h in hashes:
    print(h)

print("\nSuspicious Commands")
for cmd in sorted(set(commands)):
    print(cmd)

print("\nSeverity Summary")
for level, count in severity_counter.items():
    print(f"{level}: {count}")

print("\nFailed Login Attempts:", len(failed))
print("Possible SQL Injection Attempts:", len(sql))
print("Possible XSS Attempts:", len(xss))

print("\nBrute Force Detection")
for ip, count in ip_counter.items():
    if count >= 5:
        print(f"WARNING: {ip} appeared {count} times")

print("\nOverall Summary")
print("-" * 50)
print(f"Total IPs          : {len(ips)}")
print(f"Unique IPs         : {len(set(ips))}")
print(f"Emails             : {len(emails)}")
print(f"Domains            : {len(domains)}")
print(f"URLs               : {len(urls)}")
print(f"Ports              : {len(ports)}")
print(f"Dates              : {len(dates)}")
print(f"Times              : {len(times)}")
print(f"Failed Logins      : {len(failed)}")
print(f"SQLi Indicators    : {len(sql)}")
print(f"XSS Indicators     : {len(xss)}")
print(f"Commands Detected  : {len(commands)}")
print(f"Hashes Found       : {len(hashes)}")

# Save report
with open("report.txt", "w") as report:
    report.write("Mini SOC Log Analyzer Report\n")
    report.write("=" * 40 + "\n\n")

    report.write("Top Active IPs\n")
    for ip, count in ip_counter.most_common(5):
        report.write(f"{ip} -> {count}\n")

    report.write("\nSeverity Summary\n")
    for level, count in severity_counter.items():
        report.write(f"{level}: {count}\n")

    report.write(f"\nFailed Logins: {len(failed)}")
    report.write(f"\nSQLi Indicators: {len(sql)}")
    report.write(f"\nXSS Indicators: {len(xss)}")

print("\nReport saved as report.txt")