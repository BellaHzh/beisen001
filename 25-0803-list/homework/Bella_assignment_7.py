cities = ["Chengdu", "Shanghai", "Shenyang", "Suzhou", "Changsha"]
prices = [800.05, 1200.0, 600.02, 750.01, 700.99]
tickets = [10, 5, 20, 12, 16]

while True:
    print()
    choice = input(
        "(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otal or (q)uit: ")
    while choice not in "sqlarut":
        print("Invalid option, try again")
        print()
        choice = input(
            "(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otal or (q)uit: ")
    if choice == "s":
        destination = input("Enter a destination city: ")
        if destination in cities:
            position = cities.index(destination)
            price = prices[position]
            left_tickets = tickets[position]
            print(
                f'We fly to "{destination}", ticket cost ${price} per person')
            print(f"We currently have {left_tickets} tickets available")
        else:
            print(f"Sorry, we don't fly to \"{destination}\"")

    elif choice == "a":
        new_city = input("Enter a new destination city: ")
        while new_city in cities:
            print("Sorry, we already fly to that city. Try again.")
            new_city = input("Enter a new destination city: ")
        new_price = float(input("Enter a ticket cost: "))
        while new_price <= 0:
            print("Invalid cost. Try again.")
            new_price = float(input("Enter a ticket cost: "))
        new_number = int(input("How many tickets do we have? "))
        while new_number <= 0:
            print("Invalid quantity. Try again.")
            new_number = float(input("How many tickets do we have? "))
        cities.append(new_city)
        prices.append(new_price)
        tickets.append(new_number)
        print("Destination added!")

    elif choice == "l":
        print()
        print(f"{'Destination City':<15}{'Price':>12}{'Quantity':>15}")
        length = len(cities)
        for i in range(length):
            print(f"{cities[i]:<15}{prices[i]:>12}{tickets[i]:>15}")
    elif choice == "r":
        remove = input("Enter a destination: ")
        if remove not in cities:
            print("Destination city doesn't exist. Can't remove.")
        if remove in cities:
            print("Destination removed!")
            cities.remove(remove)
    elif choice == "u":
        update_place = input("Enter a destination: ")
        if update_place not in cities:
            print("Destination doesn't exist. Can't update.")
        if update_place in cities:
            update_position = cities.index(update_place)
            update_detail = input(
                "What would you like to update? \n(c)ost or (q)uantity: ")
            if update_detail == "c":
                update_cost = float(input("Enter a new ticket cost: "))
                if update_cost <= 0:
                    print("Invalid cost!")
                    update_cost = float(input("Enter a new ticket cost: "))
                    prices[update_position] = update_cost
                    print("Ticket cost has been updated")
            elif update_detail == "q":
                update_cost = int(input("Enter a new ticket quantity: "))
                if update_cost <= 0:
                    print("Invalid quantity!")
                    update_quantity = int(
                        input("Enter a new ticket quantity: "))
                    tickets[update_position] = update_quantity
                    print("Ticket quantity has been updated")
    elif choice == "t":
        total = 0
        length_cities = len(cities)
        for i in range(length_cities):
            value = prices[i]*tickets[i]
            total += value
        print(f"Total value of all products: ${total}")

    elif choice == "q":
        print("See you soon!")
        break
