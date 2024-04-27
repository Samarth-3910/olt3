import numpy as np

num_input = input("Enter the number with spaces between them : ")
input_list = num_input.split()
num_list = [int(num) for num in input_list]

mean_list = np.mean(num_list)
print("The mean of given list is :",mean_list)