'''
Python Program to get the multiplication of largest number in an given list

Time Complexity:O(numbers)
Space Complexity:O(1)

Sample I/O:
	Input:
	3
	10 8 9

	Output:
	90

'''
def maximum(numbers):
	numbers.sort()
	return numbers[-2] * numbers[-1]

numbers = []
n = int(input())
numbers = [int(i) for i in input().split()]
print(maximum(numbers))
