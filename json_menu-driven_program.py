import json

with open("hello.json", "r") as file:
    data = json.load(file)

while True:
    print("\n1. View")
    print("2. Search")
    print("3. Add")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        for tool, desc in data.items():
            print(tool, ":", desc)

    elif choice == "2":
        tool = input("Enter Tool: ")
        if tool in data:
            print(data[tool])
        else:
            print("Not Found")

    elif choice == "3":
        tool = input("Enter Tool: ")
        desc = input("Enter Description: ")
        data[tool] = desc

    elif choice == "4":
        tool = input("Enter Tool: ")
        if tool in data:
            data[tool] = input("Enter New Description: ")
        else:
            print("Not Found")

    elif choice == "5":
        tool = input("Enter Tool: ")
        if tool in data:
            del data[tool]
        else:
            print("Not Found")

    elif choice == "6":
        with open("hello.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Data Saved")
        break

    else:
        print("Invalid Choice")