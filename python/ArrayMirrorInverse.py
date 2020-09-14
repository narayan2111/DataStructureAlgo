def arraymirror(arr):
	n=len(arr)
	for i in range(0,n):
		if (arr[arr[i]]!=i):
			return False

	return True
arr=[]
n=int(input("Enter size:"))
for i in range(n):
	item=int(input())
	arr.append(item)
if(arraymirror(arr)):
	print("Yes")
else :
	print("No")


