import re
file = open("security.log", "r")
content = file.read()

ips = re.findall(r"\d+\.\d+\.\d+\.\d+", content)
emails = re.findall(r"\w+@\w+\.\w+", content)
print("IP addresses found:")
print(ips)

print("Email(s) Found:")
print(emails)
file.close()

import re

file = open("security.log", "r")
content = file.read()

ips = re.findall(r"\d+\.\d+\.\d+\.\d+", content)
emails = re.findall(r"\w+@\w+\.\w+", content)

print("IP addresses found:")
print(ips)

print("Email(s) Found:")
print(emails)

file.close()