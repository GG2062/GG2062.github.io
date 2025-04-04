# exFactorial.py

def factorial(num):

    #recursive def
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

        '''
    #direct def
    prod = 1
    for i in range(1, num+1):
        prod *= i
    return prod
'''
    

def main():
    number = int(input('Enter a  + number or 0: '))

    result = factorial(number)

    print(f'{number}! = {result}')
    print()

main()