def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

total_sum = sum_all(1, 5, 7, 3)
print("Total Sum:", total_sum)

def company_info(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])


company_info(ticker='AAPL', ceo = 'Tim Cook', revenue = "$274.5B")

x = lambda r, h:3.14*(r ** 2) * h
print("Volume_2:", x(33, 22))

