def arraymirror(arr):
	arr.sort()
	for i in range(1,n-1):
		if (arr[arr[i]]!=i):
			return False

	return True

arr = []
n = int(input())
arr = [int(i) for i in input().split()]
if(arraymirror(arr)):
	print("Yes")
else :
	print("No")


