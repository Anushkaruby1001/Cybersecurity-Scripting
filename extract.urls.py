import re

file = open("security.log", "r")
content = file.read()

# Find IP addresses
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", content)

# Find email addresses
emails = re.findall(r"\w+@\w+\.\w+", content)

# Find dates (YYYY-MM-DD)
dates = re.findall(r"\d{4}-\d{2}-\d{2}", content)

# Find failed login messages
failed_logins = re.findall(r"Failed login", content, re.IGNORECASE)

print("=" * 40)
print("IP Addresses Found:")
for ip in set(ips):
    print(ip)

print("\nEmail Addresses Found:")
for email in set(emails):
    print(email)

print("\nDates Found:")
for date in set(dates):
    print(date)

print("\nFailed Login Attempts:", len(failed_logins))

print("\nSummary")
print("-" * 40)
print(f"Total IPs: {len(ips)}")
print(f"Unique IPs: {len(set(ips))}")
print(f"Total Emails: {len(emails)}")
print(f"Total Dates: {len(dates)}")

file.close()