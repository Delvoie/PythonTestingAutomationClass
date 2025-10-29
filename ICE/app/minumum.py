# Date: Oct 29, 2025
# Name: "Minimum.py - ICE3 Application"
# Programmer: Lucas
# Description: Application to find the minimum value in a list of integers


# finds the minimum value in a list of only numbers retunrs the minimum value and error messages for invalid inputs
def find_minimum(integer_list):

    # first Check if list is empty
    if len(integer_list) == 0:
        raise ValueError("List is empty")
    
    # Check if all values are integers
    for integers in integer_list:
        if not isinstance(integers, int):
            raise ValueError(f"Error in list must contain only integers.")

    # Find and return the minimum value
    # initialize list with first value
    minimum = integer_list[0]
    # for loop to check each value in the list
    for num in integer_list:
        #compare each value to the minimum value
        if num < minimum:
            minimum = num
    # return the minimum value
    return minimum
