#string

#concatenation
print("\n==concatenation=============")
print("a"+"b")

#string replication 
print("\n==string replication========")
print("abc"*20)

#string length
print("\n==length====================")
print(len("abc"))

#string slicing
print("\n==string slicing============")
arr = "shivam varshney"
print(arr[0:6:2])#start:end:steps 
print(arr[-6:-1])

#string case conversion
print("\nstring case conversion======")
print("Shivam".lower())
print("shivam".upper())

#string stripping
print("\nstring stripping============")
print("    shivam  varshney        ".strip())

#string replacing
print("\nstring replacing============")
print('shivam'.replace('h','v'))

#string count
print("\nstring count================")
print("shivam".count('s'))

#string find
print("\nstring find=================")
print("shivam".find("iv"))

#string check
print("\nstring check================")
print("shivam".islower())
print("ABC".isupper())
print("12a".isdigit())
print("hsdkShhsHSu)".isalpha())


#string capitalization
print("\nstring capitalization=======")
print("shivam varshney".capitalize())
print("shivam varshney".title())


#check for start end end
print("\nstart and end===============")
print("Shivam".startswith("Shi"))
print("Varshney".endswith("ney"))

#allignment
print("\nallignment==================")
print("Shivam".center(20,"?"))
print("Shivam".ljust(20,'?'))
print("Shivam".rjust(20,'?'))