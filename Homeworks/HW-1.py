odd_number_list = [0,2,4,,6,,8,10,12,14,16,18,20]
even_number_list = [1,3,5,7,9,11,13,15,17,19,21]

merged_list = odd_number_list + even_number_list

merged_list.sort() 

final_list =([ i*2 for i in merged_list])


for i in final_list :
     print(type(i))
     print("i: ",i) 
