security_tools = {
}

def show_tools():
    if security_tools:
     print("\nSecurity tool Inventory:")
     for tool,category in security_tools.items():
        print(f"Tool:{tool} - Category:{category}")
    else:
        print("No Tools Available")
# show_tools()

def search_tool():
    tool = input("Enter your tool name:")
    if tool in security_tools:
        print("Tool found:", tool)
        print("Category:",security_tools[tool])
    else:
        print("Tool Not Found")
# search_tool()

def add_tool():
    adding_tool = input("Enter what tool you want to add:")
    adding_category = input ("Enter what you want to add category for the tool:")
    security_tools[adding_tool] = adding_category
    print("Tool added successfully!")
# add_tool()

def count_tools():
    return len(security_tools)

def remove_tool():
    removing_tool = input("Enter tool you want to delete:")
    if removing_tool in security_tools:
     del security_tools[removing_tool]
     print("Tool Removed Successfully")
    else:
        print("Tool Not Found")

def save_to_file():
    with open("security_tools.txt", "w") as file:
        for tool,category in security_tools.items():
            file.write(f"{tool},{category}\n")
    print("Inventory Saved Successfully")

def load_from_file():
    try:
     with open("security_tools.txt", "r") as file:
      for line in file:
        if "," in line:
         tool, category = line.split(",")
         category = category.strip()
         security_tools[tool] = category
     file.close()
    except FileNotFoundError:
        print("No inventory file found. Starting fresh.")
load_from_file()
while True:
    print()

    print("1. Show Tools")
    print("2. Search Tool")
    print("3. Add Tool")
    print("4. Count Tools")
    print("5. Remove Tool")
    print("6. Save to File")
    print("7. Exit")
    


    choice = input("Enter Choice:")
    if choice == "1":
        show_tools()
    elif choice == "2":
        search_tool()
    elif choice == "3":
        add_tool()
    elif choice == "4":
        print("Total tools:",count_tools())
    elif choice == "5":
        remove_tool()
    elif choice == "6":
        save_to_file()
    elif choice == "7":
        show_tools()
        print("Goodbye")
        break
    else:
        print("Invalid Choice")
# show_tools()

# filename = input("Enter the filename:").strip().lower()
# extensions = (".exe",".dll",".bat")
# if filename.endswith(extensions):
#     print("Executable file Detected")
# else:
#     print("Not an Executable")