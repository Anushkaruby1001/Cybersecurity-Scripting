incident = int(input("Enter how many incidents:"))

for i in range(incident):
    print("Incident", incident+1)

    analyst = input("Enter you analyst name:")
    target = input("Enter the target:")
    print(f"Analyst:{analyst}")
    print(f"Target:{target}")
    
    severity = input("Enter the severity:")
    severity = severity.lower()
    if severity == "high":
        print("Immediate Investigation")
    elif severity == "medium":
        print("Review")
    elif severity == "low":
        print("Monitor")
    else:
        print("Invalid Severity")