<<<<<<< HEAD
from prettytable import PrettyTable

price = 0
rows = 20
seats_per_row = 3
adminpass = "pass"
seat_map = {}
flight_list = {"Mumbai", "France", "United States", "Maldives"}

flights = PrettyTable()
flights.field_names = ["Serial Number", "Flight Number", "Destination", "Time of Departure"]
flights.add_rows(
    [
        [1, "X02971", "Mumbai", "0700"],
        [2, "Z02543", "France", "1300"],
        [3, "Y05643", "United States", "2350"],
        [4, "t09356", "Maldives", "0100"],
    ]
)

rate = PrettyTable()
rate.field_names = ["Class", "One-way Fare", "Round-Trip Fare", "Baggage"]
rate.add_rows(
    [
        ["Economy", "50$", "100$", "1-Checked In, 1-Carry on"],
        ["Economy+", "60$", "130$", "2-Checked In, 1-Carry on"],
        ["Business", "90$", "200$", "2-Checked In, 1-Carry on & Lounge access"],
    ]
)

menu = {
    "1": "Dosa & Sambar",
    "2": "Ghee Roast",
    "3": "Masala Dosa",
    "4": "Dosa & Chutney",
}

admin = input("Enter admin password: ")
if admin == adminpass:
    print("\nWelcome to DosaAir!")
    while True:
        print()
        print("1. Make Reservation")
        print("2. Print Reservation Details")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            table = PrettyTable(["Row", "Seats"] + [chr(s + 64) for s in range(1, seats_per_row + 1)])
            for r in range(1, rows + 1):
                row_data = [str(r), ""]
                for s in range(1, seats_per_row + 1):
                    seat_key = f"{r}{chr(s + 64)}"
                    status = "Available" if seat_key not in seat_map else "Booked"
                    row_data.append(status)
                table.add_row(row_data)

            print(rate)
            print(flights)
            dest = input("\nPlease enter your destination: ")
            if dest.capitalize() in flight_list:
                print(table)
                tckch = input("\nEnter ticket type: ").capitalize()

                if tckch in {"Economy", "Economy+", "Business"}:
                    way = input("\nSelect (1) for One-way & (2) for Round-Trip: ")

                    ticket_prices = {
                        "Economy": {"1": 50, "2": 100},
                        "Economy+": {"1": 60, "2": 130},
                        "Business": {"1": 90, "2": 200},
                    }

                    if way in ticket_prices[tckch]:
                        price += ticket_prices[tckch][way]
                        name = input("\nEnter your full name: ")
                        age = int(input("\nEnter your age: "))
                        row = int(input("\nEnter the row number: "))
                        seat = input("\nEnter the seat letter (A, B, C): ")

                        food = input("\nWould you like food to be served? (y/n): ")

                        if food.lower() == "y":
                            print("Menu:\n 1. Dosa & Sambar \n 2. Ghee Roast \n 3. Masala Dosa \n 4. Dosa & Chutney")
                            valid_choices = menu.keys()
                            fch = input("\nEnter choice of dish: ")

                            while fch not in valid_choices:
                                print("\nInvalid choice. Please select a valid dish from the menu.")
                                fch = input("\nEnter choice of dish: ")
                        else:
                            fch = "nil"

                        seat_key = f"{row}{seat.upper()}"

                        if seat_key in seat_map:
                            print("\nSeat already booked. Please choose another seat.")
                        else:
                            seat_map[seat_key] = {"name": name, "food_choice": menu.get(fch, "___")}
                            print(f"Reservation successful! Seat {seat_key} booked for {name} with food choice as {menu.get(fch, '___')} to destination {dest.capitalize()}. Fare: {price}$")
                    else:
                        print("Invalid choice for One-way/Round-Trip.")
                else:
                    print("Invalid ticket type entered")
            else:
                print("Sorry, we don't fly to this destination")

        elif choice == "2":
            print("Reservation Details:")
            for seat, details in seat_map.items():
                print()
                print(f"Seat {seat} for {details['name']} to {dest.capitalize()} with food choice {details['food_choice']} - Fare: {price}$")

        elif choice == "3":
            print("\nExiting the reservation system. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
else:
    print("Invalid Password.")
=======
from prettytable import PrettyTable

price = 0
rows = 20
seats_per_row = 3
adminpass = "pass"
seat_map = {}
flight_list = {"Mumbai", "France", "United States", "Maldives"}

flights = PrettyTable()
flights.field_names = ["Serial Number", "Flight Number", "Destination", "Time of Departure"]
flights.add_rows(
    [
        [1, "X02971", "Mumbai", "0700"],
        [2, "Z02543", "France", "1300"],
        [3, "Y05643", "United States", "2350"],
        [4, "t09356", "Maldives", "0100"],
    ]
)

rate = PrettyTable()
rate.field_names = ["Class", "One-way Fare", "Round-Trip Fare", "Baggage"]
rate.add_rows(
    [
        ["Economy", "50$", "100$", "1-Checked In, 1-Carry on"],
        ["Economy+", "60$", "130$", "2-Checked In, 1-Carry on"],
        ["Business", "90$", "200$", "2-Checked In, 1-Carry on & Lounge access"],
    ]
)

menu = {
    "1": "Dosa & Sambar",
    "2": "Ghee Roast",
    "3": "Masala Dosa",
    "4": "Dosa & Chutney",
}

admin = input("Enter admin password: ")
if admin == adminpass:
    print("\nWelcome to DosaAir!")
    while True:
        print()
        print("1. Make Reservation")
        print("2. Print Reservation Details")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            table = PrettyTable(["Row", "Seats"] + [chr(s + 64) for s in range(1, seats_per_row + 1)])
            for r in range(1, rows + 1):
                row_data = [str(r), ""]
                for s in range(1, seats_per_row + 1):
                    seat_key = f"{r}{chr(s + 64)}"
                    status = "Available" if seat_key not in seat_map else "Booked"
                    row_data.append(status)
                table.add_row(row_data)

            print(rate)
            print(flights)
            dest = input("\nPlease enter your destination: ")
            if dest.capitalize() in flight_list:
                print(table)
                tckch = input("\nEnter ticket type: ").capitalize()

                if tckch in {"Economy", "Economy+", "Business"}:
                    way = input("\nSelect (1) for One-way & (2) for Round-Trip: ")

                    ticket_prices = {
                        "Economy": {"1": 50, "2": 100},
                        "Economy+": {"1": 60, "2": 130},
                        "Business": {"1": 90, "2": 200},
                    }

                    if way in ticket_prices[tckch]:
                        price += ticket_prices[tckch][way]
                        name = input("\nEnter your full name: ")
                        age = int(input("\nEnter your age: "))
                        row = int(input("\nEnter the row number: "))
                        seat = input("\nEnter the seat letter (A, B, C): ")

                        food = input("\nWould you like food to be served? (y/n): ")

                        if food.lower() == "y":
                            print("Menu:\n 1. Dosa & Sambar \n 2. Ghee Roast \n 3. Masala Dosa \n 4. Dosa & Chutney")
                            valid_choices = menu.keys()
                            fch = input("\nEnter choice of dish: ")

                            while fch not in valid_choices:
                                print("\nInvalid choice. Please select a valid dish from the menu.")
                                fch = input("\nEnter choice of dish: ")
                        else:
                            fch = "nil"

                        seat_key = f"{row}{seat.upper()}"

                        if seat_key in seat_map:
                            print("\nSeat already booked. Please choose another seat.")
                        else:
                            seat_map[seat_key] = {"name": name, "food_choice": menu.get(fch, "___")}
                            print(f"Reservation successful! Seat {seat_key} booked for {name} with food choice as {menu.get(fch, '___')} to destination {dest.capitalize()}. Fare: {price}$")
                    else:
                        print("Invalid choice for One-way/Round-Trip.")
                else:
                    print("Invalid ticket type entered")
            else:
                print("Sorry, we don't fly to this destination")

        elif choice == "2":
            print("Reservation Details:")
            for seat, details in seat_map.items():
                print()
                print(f"Seat {seat} for {details['name']} to {dest.capitalize()} with food choice {details['food_choice']} - Fare: {price}$")

        elif choice == "3":
            print("\nExiting the reservation system. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
else:
    print("Invalid Password.")
>>>>>>> 87bee1c771d8f04424a35e7bc6e9ecf7c775d40c
