# Python code to demonstrate 
# decode() 
import base64
# initializing string 
str = "geeksforgeeks"

# encoding string 
str_enc = base64.b64encode(str, 'strict') 

# printing the encoded string 
print ("The encoded string in base64 format is : " )
print (str_enc) 

# printing the original decoded string 
print ("The decoded string is : ")
print (base64.b64decode(str_enc, 'strict') )
