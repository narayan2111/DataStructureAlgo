def unique(array,size):
	array.sort()
	for i in range(size):
		for j in range(size-1):
			if array[i]!=array[j]:
				print(array[i])




array=[]
size=int(input("Enter size"))
for i in range(size):
	item=int(input())
	array.append(item)

print(unique(array,size))