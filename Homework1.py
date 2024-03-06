#  1 harc
# def main():
#     array=list(map(int,input("Enter the element of integer array separated by spaces:").split()))
#     min_value= min(array,None)

#     if min_value is not None:
#         print("Minimum value in the array:", min_value)
#     else:
#         print("the array is empty.")

# if __name__ == "__main__":
#     main()

 
 
# 2 haarc
# def main():
#     array=list(map(int,input("enter the elementof the integer of the array sparated by spaces:" ).split()))
#     odd_count=sum(1 for num in array if num %2 !=0)
#     print("number of odd elements in the array:",odd_count)

# if __name__ == "__main__":
#      main() 


# 3 harc
# def remuve_element_at_index(arr,index):
#     return arr[:index]+arr[index+1:]

# arr=[1,6,3,7,9,5]
# index=1
# new_arr=remuve_element_at_index(arr,index)
# print("updated arr",new_arr)


# 4 haarc
# def find_min_max_sum(arr):
#     if len(arr)==0:
#         return None
    
#     min_val=max_val=arr[0]

#     for num in arr:
#         if num<min_val:
#             min_val=num
#         if num>max_val:
#             max_val=num

#     min_max_sum=min_val+max_val
#     return min_max_sum        


# arr = [11, 7, 3, 9, 5]
# result = find_min_max_sum(arr)
# if result is not None:
#     print("Sum of minimum and maximum elements:", result)
# else:
#     print("Array is empty.")




# 5 harc

# def segregate(a, n):
	
# 	i = 0
# 	j = (n - 1)

	
# 	while (j >= i):
	
	
		
# 		if (a[i] % 2 != 0):
# 			if (a[j] % 2 == 0):
				
				
# 				a[i], a[j] = a[j], a[i]
# 				i += 1
# 				j -= 1
			
# 			else:
# 				j -= 1
# 		else:
# 			i += 1;
			
# 	for i in range(n):
# 		print(a[i], end = " ")


# a = [ 1, 2, 3, 4, 5, 6 ]
# n = len(a)

# segregate(a, n)

                  
                
# 6 harc

# list1=[10,5,25,33,80,88]
# only_odd=[num for num in list1 if num % 2 ==1]      ?
# print(only_odd)


# 7 harc








# 8 harc
# import numpy as np
# N=5

# matrix=np.random.randit(1,10,size=(N,N))
# print("original matrix:")
# print(matrix)

# first_column=matrix[:,0]
# third_column=matrix[:,2]

# print(first_column)
# print(third_column)


# 9 harc

# import numpy as np
# N=5
# matrix=np.random.randit(1,10,size=(N,N))
# print(matrix)

# first_row_sum = np.sum(matrix[0, :])
# fourth_row_sum = np.sum(matrix[3, :])

# max_sum = max(first_row_sum, fourth_row_sum)
# min_sum = min(first_row_sum, fourth_row_sum)

# print("Minimum sum:", min_sum)


# 10 harc
# my_list=[1,3,5,7,9]
# item=my_list.pop(4)
# print(item)
# print(my_list)
 
