# exRecSum.py

def range_sum(num_list, start, end):
    if start > end:     #empty list
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)
    
def main():
    numbers = [2, 5, 7, 10, 4, 8, 1, 7, 2]
    mysum = range_sum(numbers, 0, len(numbers)-1)

    print(f'The sum is {mysum}.')

main()

