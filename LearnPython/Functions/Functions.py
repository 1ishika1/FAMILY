# expense_1 = [12, 34, 56, 67]
# expense_2 = [23, 45, 67, 78]
# total_expense_1 = 0
# for expense in expense_1:
#     total_expense_1 += expense

# print("Total expense:", total_expense_1)
#User-defined function
def calculate_total_expense(expenses):

    '''
    expenses: input list containing numbers
    return: total of all numbers in the list
    '''
    total=0
    for expense in expenses:
        total += expense
    return total

expense_1 = [34, 56, 78, 90]
expense_2 = [23, 45, 67, 78]

total_expense_1 = calculate_total_expense(expense_1)
total_expense_2 = calculate_total_expense(expense_2)

print("Total expense 1:", total_expense_1)
print("Total expense 2:", total_expense_2)
print(help(calculate_total_expense))

#built-in functions
import math
expenses = [12, 34, 56, 67]
total = math.fsum(expenses)
total_1 = math.sqrt(total)
print("Total:", total)
print("Total_1:", total_1)