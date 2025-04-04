# exFib.py

def fib(n):

    if n ==0:
        return 0
    
    elif n ==1:
        return 1
    
    else:
        return fib(n-1) +fib(n-2)
    
def main():
    print('The first 10 Fibonacci numbers are: ')

    for num in range(0, 10):
        print(fib(num), end = "\t")
    print()

main()