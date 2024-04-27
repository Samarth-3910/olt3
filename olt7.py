import numpy as np

num_input = input("Enter the number with spaces between them : ")
input_list = num_input.split()
num_list = [int(num) for num in input_list]

Standard_list = np.std(num_list)
print("The Standard Deviation of given list is :",Standard_list)