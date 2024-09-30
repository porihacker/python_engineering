# numbers =[20029,6267,7269,65,6363,839,9272]

def smallest(numbers):
    small=numbers[0]
    for number in numbers:
        if number < small:
            small=number
    return small

# smallest(numbers)
