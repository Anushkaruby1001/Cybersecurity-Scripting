import re
from collections import Counter

file = open("security.log", "r")
content = file.read()

# Find IP addresses
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", content)

# Find email addresses
emails = re.findall(r"\w+@\w+\.\w+", content)

# Find dates
dates = re.findall(r"\d{4}-\d{2}-\d{2}", content)

# Failed logins
failed_logins = re.findall(r"Failed login", content, re.IGNORECASE)

# Usernames
users = re.findall(r"User:\s*(\w+)", content)

# URLs
urls = re.findall(r"https?://[^\s]+", content)

# Severity Levels
high_alerts = re.findall(r"HIGH|CRITICAL", content, re.IGNORECASE)

print("=" * 40)
print("IP Addresses Found:")
for ip in set(ips):
    print(ip)

print("\nIP Address Frequency")
ip_count = Counter(ips)
for ip, count in ip_count.items():
    print(f"{ip} -> {count} time(s)")

print("\nEmail Addresses Found:")
for email in set(emails):
    print(email)

print("\nUsernames Found:")
for user in set(users):
    print(user)

print("\nURLs Found:")
for url in set(urls):
    print(url)

print("\nDates Found:")
for date in set(dates):
    print(date)

print("\nFailed Login Attempts:", len(failed_logins))
print("High/Critical Alerts:", len(high_alerts))

print("\nSummary")
print("-" * 40)
print(f"Total IPs: {len(ips)}")
print(f"Unique IPs: {len(set(ips))}")
print(f"Total Emails: {len(emails)}")
print(f"Total Dates: {len(dates)}")
print(f"Total Users: {len(users)}")
print(f"Total URLs: {len(urls)}")

# Save report
with open("report.txt", "w") as report:
    report.write("Security Log Report\n")
    report.write("=" * 30 + "\n\n")

    report.write("IP Frequency\n")
    for ip, count in ip_count.items():
        report.write(f"{ip} -> {count}\n")

    report.write(f"\nFailed Logins: {len(failed_logins)}")
    report.write(f"\nHigh/Critical Alerts: {len(high_alerts)}")

print("\nReport saved as report.txt")

file.close()