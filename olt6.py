import numpy as np

num_input = input("Enter the number with spaces between them : ")
input_list = num_input.split()
num_list = [int(num) for num in input_list]

median_list = np.median(num_list)
print("The median of given list is :",median_list)