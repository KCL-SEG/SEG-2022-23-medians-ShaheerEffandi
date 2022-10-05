"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

"""
Create 3 branches of selection statements.
one for if the size of the input is 1
one for if the input size is odd and one for if it is even

"""
listLen = len(numbers)
median = 0

numbers = sorted(numbers)

if (listLen == 1):
    median = numbers[0]
elif (listLen % 2 == 0):
    """If there are an even number of values the median is the mean
    of (length/2) and (length/2) - 1
    Since indexes start at 0
    """
    median = (numbers[int(listLen / 2)] + numbers[int((listLen / 2) - 1)]) / 2

else:
    median = numbers[int(listLen//2)]

print(f"The median of the numbers {numbers} is:")
print(median)
