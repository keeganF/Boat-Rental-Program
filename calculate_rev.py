def cal_rev():
    with open('revenue.txt') as file:
        data = file.readlines()
    total = 0
    for line in data:
        x = float(line.strip())
        total += x
    return total



if __name__ == '__main__':
    print(cal_rev())



