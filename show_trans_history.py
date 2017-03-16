def show_trans():
    with open('trans_history.txt') as file:
        transactions = file.read()
        print(transactions)



if __name__ == '__main__':
    print(show_trans())