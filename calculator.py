# write a progarm which takes two numbers and an operator from the user
def cal(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return 'Invalid operator'
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter operator: ')
print(cal(num1, num2, op))


