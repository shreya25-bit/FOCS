def sort_asecending_dec(list):
    """Sort a list in ascending order."""
    return sorted(list)def sort_descending_dec(list):  

    """Sort a list in descending order."""
    return sorted(list, reverse=True)           

# Example usage:
my_list = [5, 2, 9, 1, 5, 6]
asc_sorted = sort_asecending_dec(my_list)           
desc_sorted = sort_descending_dec(my_list)
print("Ascending order:", asc_sorted)       
print("Descending order:", desc_sorted)
