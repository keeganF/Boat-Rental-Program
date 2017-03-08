import csv

data_lst = [['pontoon boat', 500, [2, 4, 8], 3, 1500],
            ['cruiser boat', 350, [2, 4, 8], 3, 800],
            ['speed boat', 250, [2, 4, 8], 3, 100], 
            ['bass boat', 200, [2, 4, 8], 3, 750],
            ['jon boat', 150, [2, 4, 8], 3, 125], 
            ['jet ski', 100, [2, 4, 8], 3, 500],
            ['kayak', 50, [2, 4, 8], 3, 120]]

with open('inventory.csv', 'w') as file:
    wf = csv.DictWriter(file,
                        fieldnames=['Name', 'Price', 'Rental Rate', 
                                    'Quantity', 'Replacement Value'])
    wf.writeheader()

    for data in data_lst:
        wf.writerow({'Name': data[0],
                     'Price': data[1],
                     'Rental Rate': data[2],
                     'Quantity': data[3],
                     'Replacement Value': data[4]})


