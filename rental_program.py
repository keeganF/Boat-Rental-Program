import csv
from boats import view_inv
from boats import rent_item
from boats import return_item
from boats import replace_item
from calculate_rev import cal_rev
from view_trans import view_trans_history



in_store = True
while in_store:

    identify = input("Are you a Customer or Manager (enter 'Q' to leave store)? ").lower().strip()

    if identify == "q":
        break

    elif identify == "customer":
        in_store = False
        option = True
        while option:
            try:
                option = int(input("Welcome to Keegan's Premium Boats. Would you like to,"
                " 1.(view inventory), 2.(rent item), 3.(return item) or 4.(replace item)? "))

                if option == 1:
                    view_inv('inventory.csv')

                elif option == 2:
                    rent_item('inventory.csv')
                    option = False



                elif option == 3:
                    return_item('inventory.csv')
                    option = False


                elif option == 4:
                    replace_item('inventory.csv')
                    option = False

            except ValueError:
                print("Invalid Input!")



    elif identify == "manager":
        option2 = True
        while option2:
            try:
                print("**ENTER 1 OR 2**")
                option2 = int(input("Would you like to 1.(view revenue) or 2.(view transaction history)? "))
                if option2 == 1:
                    print(cal_rev())
                    option2 = False
                    in_store = False

                elif option2 == 2:
                    print(view_trans_history())
                    option2 = False
                    in_store = False
            except ValueError:
                print("Invalid Input!")


















