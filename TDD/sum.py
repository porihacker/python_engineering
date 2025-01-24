# def add(a: int, b: int) -> int:
#     result = a + b
#     return result

# group = ["aloy", "thato", "khosi", "mpho"]
# group2 = ["aloy", "hashim", "khosi", "jason"]

# result = set(group) - set(group2)

# print(result)


# def merge_dicts(dict1, dict2):
#     merged = dict1.copy()
#     merged.update(dict2)
#     return merged


# # Test
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4, "a": 8}
# # print(merge_dicts(d1, d2))  # {'a': 1, 'b': 3, 'c': 4}
# A = [1, 2, 4, 5]
# b = tuple(A)
# T = 2
# print(A.count(T))


# def square_root(x):
#     if x < 0:
#         raise ValueError("Cannot compute the square root of a negative number.")
#     return x**0.5


# # Example calls
# print(square_root(9))  # Output: 3.0
# print(
#     square_root(-4)
# )  # Raises: ValueError: Cannot compute the square root of a negative number.


# def sum_multiples_of_3_or_5(number: int) -> int:
#     list_sum = []
#     for i in range(number):
#         if i % 5 == 0 or i % 3 == 0:
#             list_sum.append(i)
#     return sum(list_sum)


# print(sum_multiples_of_3_or_5(10))


def is_palindrome(string_sentence: str) -> bool:
    # Remove punctuation and spaces, convert to lowercase

    clean = "".join(x.lower() for x in string_sentence if x.isalnum())
    if clean == clean[::-1]:
        return True
    else:
        return False


# Now these all return True
print(is_palindrome("racecar"))
print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("Was it a car or a cat I saw?"))

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("A man, a plan, a canal, Panama"))
