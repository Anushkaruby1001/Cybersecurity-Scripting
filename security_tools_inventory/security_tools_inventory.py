security_tools = [
    "Wireshark",
    "Burp Suite",
    "Nmap",
    "Hydra",
    "Nessus"
]


def show_tools():
    print("\nSecurity Tools:")

    for tool in security_tools:
        print("-", tool)


def add_tool(tool):
    security_tools.append(tool)
    print(f"{tool} added successfully")


def remove_tool(tool):

    if tool in security_tools:
        security_tools.remove(tool)
        print(f"{tool} removed successfully")

    else:
        print("Tool not found")


def search_tool(tool):

    if tool in security_tools:
        print(f"{tool} is available")

    else:
        print(f"{tool} is not available")


def count_tools():
    return len(security_tools)



# Main program

show_tools()

new_tool = input("\nEnter a new security tool: ")
add_tool(new_tool)

show_tools()

search = input("\nSearch a tool: ")
search_tool(search)

total = count_tools()

print("\nTotal Security Tools:", total)