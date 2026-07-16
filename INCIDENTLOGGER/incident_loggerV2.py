def get_incident_details():
    analyst = input("Enter your name: ")
    target = input("Enter your target: ")
    severity = input("Enter the severity: ")

    severity = severity.lower()

    return analyst, target, severity

def check_severity(severity):
    if severity == "high":
        return "Immediate Investigation"

    elif severity == "medium":
        return "Review"

    elif severity == "low":
        return "Monitor"

    else:
        return "Invalid severity"

def generate_report(analyst, target, severity, status):
    print("Analyst:", analyst)
    print("Target:", target)
    print("Severity:", severity)
    print("Status:", status)
result = get_incident_details()
status = check_severity(result[2])
generate_report(
    result[0],
    result[1],
    result[2],
    status
)