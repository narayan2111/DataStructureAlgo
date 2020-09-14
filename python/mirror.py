# Python 3 implementation of the approach 

# Function that returns true if 
# the array is mirror-inverse 
def isMirrorInverse(arr) : 
	n=len(arr)

	for i in range(n) : 

		# If condition fails for any element 
		if (arr[arr[i]] != i) : 
			return False; 
	
	# Given array is mirror-inverse 
	return true; 

# Driver code 
if __name__ == "__main__" : 
	
	arr=[]
	n=int(input("Enter size:"))
	for i in range(n):
		item=int(input())
		arr.append(item)
	
	if (isMirrorInverse(arr)) : 
		print("Yes"); 
	else : 
		print("No"); 

# This code is contributed by Ryuga 
