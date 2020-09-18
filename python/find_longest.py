#Program to find longest common prefix of given array of words. 

def longestCommonPrefix( string): 
	size = len(string) 

	# if size is 0, return empty string 
	if (size == 0): 
		return "" 

	if (size == 1): 
		return string[0] 
	string.sort() 
	
	# find the minimum length from first and last string 
	end = min(len(string[0]), len(string[size - 1])) 

	# find the common prefix between the first and last string 
	i = 0
	while (i < end and
		string[0][i] == string[size - 1][i]): 
		i += 1

	prefix = string[0][0: i] 
	return prefix 

string = []
size = int(input("Enter size:"))
for i in range(size):
	item=input()
	string.append(item)
print("The longest Common Prefix is :", longestCommonPrefix(string)) 

'''
Sample I/O:
	Input:
	Enter size: 3
	star
	start
	stardom

	Output:
	The longest Common Prefix is : star

Time Complexity:
