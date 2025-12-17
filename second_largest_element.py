def second_largest_element(arr):
    if len(arr) < 2:
        return None  # Not enough elements for a second largest

    first = second = float('-inf')
    for number in arr:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    return second if second != float('-inf') else None 
# Example usage:
my_list = [12, 35, 1, 10, 34, 1]
second_largest = second_largest_element(my_list)
print("The second largest element is:", second_largest)# if there is no second largest (e.g., all elements are the same) 

