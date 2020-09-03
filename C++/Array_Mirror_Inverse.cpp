// C++ implementation of the approach 
#include<bits/stdc++.h> 
using namespace std; 

// Function that returns true if 
// the array is mirror-inverse 
int isMirrorInverse(int arr[], int n) 
{ 
	for (int i = 0; i < n; i++) 
	{ 

		// If condition fails for any element 
		if (arr[arr[i]] != i) 
			return 0;
	} 

	// Given array is mirror-inverse 
	return 1;
} 

// Main fucntion
int main() 
{ 
		int arr[50], array_size; 

		cout<<"Enter Array Size: \n";
		cin>>array_size;

		cout<<"Enter "<<array_size<<" elements : \n";
		for(int i=0 ; i < array_size ; i++)
		{
			cin>>arr[i];
		}

		if (isMirrorInverse(arr , array_size)) 
			cout << "Yes,It's Array mirror-inverse"; 
		else
			cout << "No,It's not array mirror-inverse"; 
		return 0; 
} 

