# Python program to find LCM of two numbers 

# Recursive function to return gcd of a and b 
def gcd(a,b): 
	if a == 0: 
		return b 
	return gcd(b % a, a) 

# Function to return LCM of two numbers 
def lcm(a,b): 
	return (a*b) // gcd(a,b) 

# Driver program to test above function 
a, b = [int(x) for x in input().split()]
print(lcm(a, b)) 

# This code is contributed by Danish Raza 
