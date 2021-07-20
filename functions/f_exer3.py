# Write a function that returns the mean of a list of numbers.
def Average(lst):
    return sum(lst) / len(lst)


#lst = [4, 3, 2, 6]
lst = [10, 5, 6]
average = Average(lst)
(print("Average of the list = ", round(average, 2)))
