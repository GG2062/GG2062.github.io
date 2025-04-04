# Design a recursive function that accepts a list as an argument and returns the largest value in the list.  
# Write a program to test it.

def max(a, b):
    # if-else to return the largest value.
    if a > b:
        return a
    else:
        return b

def find_largest(num_list, index):
    
    # if reached the last value return it.
    if index == len(num_list) - 1:
        return num_list[index]
    
    # find the largest in the list
    else:
        largest = find_largest(num_list, index + 1)

        # return the largest value in the list.
        return max(num_list[index], largest)
    
def main():
    # list of numbers.
    numbers = [205, 50, 71, 120, 64, 800, 1, 59, 620]
    # to find the largest number in the list.
    largest_value = find_largest(numbers, 0)  
    print()
    #display the largest number.
    print(f'The largest value in the list is {largest_value}.')
    print()
    
# call the main function.
if __name__ == '__main__':
    main()

'''

The largest value in the list is 800.

'''