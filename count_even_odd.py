def evenodd(lis):
    even_count = 0
    odd_count = 0
    for number in lis:
        if number%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Example usage:
lis = [1, 2, 3, 4, 5, 6]
even, odd = evenodd(lis)
print("Even count:", even)
print("Odd count:", odd)


