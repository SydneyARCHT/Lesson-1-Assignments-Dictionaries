#1. Real-World Python Dictionary Applications
#Task 1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"]={"Dr.Pepper": 4.99, "Water": 0.00}  # adding the Bevarages column and using the drink names as keys and price as value
restaurant_menu["Main Course"]["Steak"] = 17.99                  # Changing the price of steak
del restaurant_menu["Starters"]["Bruschetta"]                    # removing Bruschetta from the Starters
print(restaurant_menu)



#2. Python Programming Challenges for Customer Service Data Handling
#Task 1
def new_service_ticket(tickets):
    ticket_number = input("Enter new ticket number: ")
    customer_name = input("Please enter customer name: ")
    ticket_issue = input("Please enter an issue/problem for the ticket: ")
    ticket_status = input("Ticket status? open/closed - Choose One: ")
    new_ticket = {
        "Customer": customer_name,
        "Issue": ticket_issue,
        "Status": ticket_status
    }
    tickets[ticket_number] = new_ticket
    print(f"Ticket {ticket_number} added successfully.")

def update_ticket_status(tickets):
    ticket_number = input("Enter ticket number to update status: ")
    if ticket_number in tickets:
        new_status = input("Enter new status (open/closed): ")
        tickets[ticket_number]["Status"] = new_status
        print(f"Ticket {ticket_number} status updated to {new_status}.")
    else:
        print(f"Ticket {ticket_number} not found.")

def display_ticket(tickets):
    for ticket_number, details in tickets.items():
        print(f"Ticket Number: {ticket_number}")
        for key, value in details.items():
            print(f" - {key}: {value}")
        print() 

def main(tickets):
    print("""
          1. Add a new service ticket
          2. Update ticket status for an existing ticket
          3. Display the current tickets
          4. Quit
          """)

    while True:
        response = input("What would you like to do? ")

        if response == "1":
            new_service_ticket(tickets)
        elif response == "2":
            update_ticket_status(tickets)
        elif response == "3":
            display_ticket(tickets)
        elif response == "4":
            print("Exiting Program...")
            break
        else:
            print("Please enter a valid response.")

service_tickets = {
"Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
"Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

main(service_tickets)
    
