analyst = input("Enter your name:")
target = input("Enter your target:")
severity = input("Enter the severity:")

print(f"Analyst:{analyst}")
print(f"Target:{target}")
print(f"Severity{severity}")
print("Status:")
if severity.lower() == "high":
    print("Immediate investigation required")
elif severity.lower() == "medium":
    print("Review within 2 hours")
elif severity.lower() == "low":
    print("Continue Monitoring")
else:
    print("Invalid Severity")

