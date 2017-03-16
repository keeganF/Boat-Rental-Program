import csv

def view_inv(document):
    "Displays the current inventory to user"

    with open(document) as file:
        document = csv.reader(file)

    for row in document:
        formatted_inv = ('{:<15} {:<15} {:<15} {:<15} {:<15}'.format(*row))
        action = print(formatted_inv)

def rent_item(inventory):
    "Allows customer to rent item of choice"

    with open(inventory, 'r') as f:
        items = csv.DictReader(f)
        stock = []

        for row in items:
            stock.append(row)

    (view_inv('inventory.csv'))
    print("____________________________________")
    rent_process = True
    while rent_process:
        choice = input("What would you like to rent today? ").lower().strip()

        for d in stock:
            if d['Name'] == choice:
                if int(d['Quantity']) < 1:
                    zero = "Sorry item out of stock check again next week."
                    return print(zero)
                quantity = int(d['Quantity'])
                price = int(d['Price'])
                replacement_v = int(d['Replacement Value'])
                sales_tax = price * .07
                deposit = replacement_v * .10
                total = price + sales_tax + deposit
                d['Quantity'] = quantity - 1
                rent_process = False

    rate_process = True
    while rate_process:
        rates = input("Would you like to rent for 2, 4, or 8 hours? ")
        if rates == '2':
            with open('inventory.csv', 'w') as file:
                wf = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rental Rate',
                                                    'Quantity', 'Replacement Value'])
                wf.writeheader()
                for item in stock:
                    wf.writerow({'Name': item['Name'], 'Price':item['Price'],
                                'Rental Rate':item['Rental Rate'], 'Quantity':item['Quantity'],
                                'Replacement Value':item['Replacement Value']})

                with open('trans_history.txt', 'a') as f:
                    f.write("Boat Type:{}   Total:{}\n".format(choice, total))
                    f.close()
                print("Thank you for shopping at Keegan's Premium Boats", "you have just rented", choice, "your total is", total, "You now have a remainig balance with us until your item is returned. See you soon.")
                rate_process = False

        elif rates == '4':
            total = (price * 2) + sales_tax + deposit
            with open('inventory.csv', 'w') as file:
                wf = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rental Rate',
                                                    'Quantity', 'Replacement Value'])
                wf.writeheader()
                for item in stock:                                                                                                                  
                    wf.writerow({'Name': item['Name'], 'Price':item['Price'],
                                'Rental Rate':item['Rental Rate'], 'Quantity':item['Quantity'],
                                'Replacement Value':item['Replacement Value']})

                with open('trans_history.txt', 'a') as f:
                    f.write("Boat Type:{}   Total:{}\n".format(choice, total))
                    f.close()
                print("Thank you for shopping at Keegan's Premium Boats", "you have just rented", choice, "your total is", total, "You now have a remainig balance with us until your item is returned. See you soon.")
                rate_process = False
        elif rates == '8':
            total = (price * 3) + sales_tax + deposit
            with open('inventory.csv', 'w') as file:
                wf = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rental Rate',
                                                    'Quantity', 'Replacement Value'])
                wf.writeheader()
                for item in stock:
                    wf.writerow({'Name': item['Name'], 'Price':item['Price'],

                                'Rental Rate':item['Rental Rate'], 'Quantity':item['Quantity'],
                                'Replacement Value':item['Replacement Value']})

            with open('trans_history.txt', 'a') as f:
                f.write("Boat Type:{}   Total:{}\n".format(choice, total))
                f.close()
            print("Thank you for shopping at Keegan's Premium Boats", "you have just rented", choice, "your total is", total, "You now have a remainig balance with us until your item is returned. See you soon.")
            rate_process = False

def return_item(inventory):
    "Allows customers to return item"

    with open(inventory, 'r') as f:
        items = csv.DictReader(f)
        stock = []

        for row in items:
            stock.append(row)

    revenue = []
    total_revenue = 0
    with open('revenue.txt') as file:
        for line in file:
            revenue.append(line)

    return_boat = input("What item will you be returning? ")

    for d in stock:
        if d['Name'] == return_boat:
            if int(d['Quantity']) == 3:
                print("That item is fully stocked")
            quantity = int(d['Quantity'])
            price = int(d['Price'])
            replacement_v = int(d['Replacement Value'])
            sales_tax = price * .07
            deposit = replacement_v * .10
            total = price + sales_tax + deposit
            d['Quantity'] = quantity + 1


    rate = input("How long did you rent this item? ")

    if rate == '2':
        total_revenue += total
        with open('revenue.txt', 'a') as f:
            f.write("{}\n".format(total_revenue))
            f.close()
        with open('inventory.csv', 'w') as file:
            wf = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rental Rate',
                                                  'Quantity', 'Replacement Value'])
            wf.writeheader()
            for item in stock:
                wf.writerow({'Name': item['Name'], 'Price':item['Price'],
                             'Rental Rate':item['Rental Rate'], 'Quantity':item['Quantity'],
                             'Replacement Value':item['Replacement Value']})
        print("Thank you for shopping with Keegan's Premium Boats. Please come again!")

    elif rate == '4':
        total = (price * 2) + sales_tax + deposit
        total_revenue += total
        with open('revenue.txt', 'a') as f:
            f.write("{}\n".format(total_revenue))
            f.close()
        with open('inventory.csv', 'w') as file:
            wf = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rental Rate',
                                                  'Quantity', 'Replacement Value'])
            wf.writeheader()
            for item in stock:
                wf.writerow({'Name': item['Name'], 'Price':item['Price'],
                             'Rental Rate':item['Rental Rate'], 'Quantity':item['Quantity'],
                             'Replacement Value':item['Replacement Value']})
        print("Thank you for shopping with Keegan's Premium Boats. Please come again!")

    elif rate == '8':
        total = (price * 3) + sales_tax + deposit
        total_revenue += total
        with open('revenue.txt', 'a') as f:
            f.write("{}\n".format(total_revenue))
            f.close()
        with open('inventory.csv', 'w') as file:
            wf = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rental Rate',
                                                  'Quantity', 'Replacement Value'])
            wf.writeheader()
            for item in stock:
                wf.writerow({'Name': item['Name'], 'Price':item['Price'],
                             'Rental Rate':item['Rental Rate'], 'Quantity':item['Quantity'],
                             'Replacement Value':item['Replacement Value']})
        print("Thank you for shopping with Keegan's Premium Boats. Please come again!")

def replace_item(inventory):
    with open(inventory, 'r') as f:
        items = csv.DictReader(f)
        stock = []

        for row in items:
            stock.append(row)

    revenue = []
    total_revenue = 0
    with open('revenue.txt') as file:
        for line in file:
            revenue.append(line)

    replace_process = True
    item = input("What item are you replacing? ")


    for d in stock:
        if d['Name'] == item:
            quantity = int(d['Quantity'])
            price = int(d['Price'])
            replacement_v = int(d['Replacement Value'])
            sales_tax = price * .07
            deposit = replacement_v * .10
            total = price + sales_tax + deposit
            d['Quantity'] = quantity + 1
            total_revenue += replacement_v
            replace_process = False
            with open('trans_history.txt', 'a') as f:
                f.write("Boat Replaced:{}  Total:{}".format(item, replacement_v))
            with open('revenue.txt', 'a') as f:
                f.write("{}\n".format(total_revenue))
                f.close()
            with open('inventory.csv', 'w') as file:
                wf = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rental Rate',
                                                    'Quantity', 'Replacement Value'])
                wf.writeheader()
                for item in stock:
                    wf.writerow({'Name': item['Name'], 'Price':item['Price'],
                                'Rental Rate':item['Rental Rate'], 'Quantity':item['Quantity'],
                                'Replacement Value':item['Replacement Value']})
            print("Thank you for shopping with Keegan's Premium Boats. Please come again!")