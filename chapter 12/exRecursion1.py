# exRecursion1.py

def message(n):
    if n > 0: 
        print(f'Come on time!! n = {n}')
        message(n-1) 
        print(f'Come on time!! n = {n}')
    
    #base case when n<=0

def main():
    message(5)

main()