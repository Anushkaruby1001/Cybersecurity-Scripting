import csv

# ----------------------------
# Function to read CSV file
# ----------------------------
def read_security_report(filename):
    reports = []

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)

            header = True

            for row in reader:
                if header:
                    header = False
                    continue

                report = {
                    "username": row[0],
                    "failed_attempts": int(row[1])
                }

                reports.append(report)

        return reports

    except FileNotFoundError:
        print("File not found.")
        return []

    except Exception as e:
        print("Error:", e)
        return []


# ----------------------------
# Display all users
# ----------------------------
def show_reports(reports):

    print("\n------ Security Report ------")

    for report in reports:
        print(
            f"Username: {report['username']} | "
            f"Failed Attempts: {report['failed_attempts']}"
        )


# ----------------------------
# Find a user
# ----------------------------
def search_user(reports):

    username = input("\nEnter username to search: ")

    found = False

    for report in reports:

        if report["username"].lower() == username.lower():

            print("\nUser Found")
            print(f"Username: {report['username']}")
            print(f"Failed Attempts: {report['failed_attempts']}")

            found = True

    if not found:
        print("User not found.")


# ----------------------------
# Count users
# ----------------------------
def count_users(reports):

    print("\nTotal Users:", len(reports))


# ----------------------------
# Check Severity
# ----------------------------
def check_severity(reports):

    print("\n------ Severity Report ------")

    for report in reports:

        attempts = report["failed_attempts"]

        if attempts >= 10:
            severity = "HIGH"

        elif attempts >= 5:
            severity = "MEDIUM"

        else:
            severity = "LOW"

        print(
            f"{report['username']} --> "
            f"{attempts} attempts --> {severity}"
        )


# ----------------------------
# Highest Failed Attempts
# ----------------------------
def highest_attempts(reports):

    highest = max(reports, key=lambda x: x["failed_attempts"])

    print("\nHighest Failed Attempts")
    print("-----------------------")
    print("Username:", highest["username"])
    print("Attempts:", highest["failed_attempts"])


# ----------------------------
# Average Attempts
# ----------------------------
def average_attempts(reports):

    total = 0

    for report in reports:
        total += report["failed_attempts"]

    average = total / len(reports)

    print(f"\nAverage Failed Attempts: {average:.2f}")


# ----------------------------
# Save Summary
# ----------------------------
def save_summary(reports):

    with open("summary.txt", "w") as file:

        file.write("Security Report Summary\n")
        file.write("------------------------\n")

        for report in reports:

            file.write(
                f"{report['username']} : "
                f"{report['failed_attempts']} failed attempts\n"
            )

    print("Summary saved successfully.")


# ----------------------------
# Menu
# ----------------------------
def menu():

    reports = read_security_report("security_report.csv")

    if len(reports) == 0:
        return

    while True:

        print("\n====== Security Log Analyzer ======")
        print("1. Show All Reports")
        print("2. Search User")
        print("3. Count Users")
        print("4. Severity Report")
        print("5. Highest Failed Attempts")
        print("6. Average Failed Attempts")
        print("7. Save Summary")
        print("8. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            show_reports(reports)

        elif choice == "2":
            search_user(reports)

        elif choice == "3":
            count_users(reports)

        elif choice == "4":
            check_severity(reports)

        elif choice == "5":
            highest_attempts(reports)

        elif choice == "6":
            average_attempts(reports)

        elif choice == "7":
            save_summary(reports)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice.")


# ----------------------------
# Start Program
# ----------------------------
menu()