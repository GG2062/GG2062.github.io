# exGCD.py

def gcd(x, y):
    if x % y == 0:
        return y
    
    else:
        return gcd(y, x % y)
    
def main():

    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    print(f'Their GCD is {gcd(num1, num2)}.')
    print()

main()