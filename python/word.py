# Python 3 code to demonstrate 
# removing duplicated from list 
# using naive methods 

# initializing list 
test_list = input().split()
print ("The original list is : " + str(test_list)) 

# using naive method 
# to remove duplicated 
# from list 
res = [] 
for i in test_list: 
	if test_list!=res:
		res. append(i) 

# printing list after removal 
print ("The list after removing duplicates : " + str(res)) 
