'''Using python 3.6
Write a program that reads 2 lines from input, first line is alphabet order and second line is string that you want to sort using that order.
e.g
input line 1 -> abcdefghijklmnopqrstuvwxyz
input line 2 -> cyxbza
output -> abcxyz

Input line 1 - > zyxwvutsrqponmlkjihgfedcba
Input line 2 ->cyxbza
Output -> zyxcba
'''

ref=input("Enter The pattern:")
tosort=input("Enter The input string:")
pattern=[]
sort=[]
sorted=[]
for value in ref:
    pattern.append(value)   #loop for storing alphabets as elements in a list
for value in tosort:
    sort.append(value)      #loop for storing input string as elements in a list
for value in pattern:
    for i in sort:
        if value==i:        #checking the input string elements w.r.t. alphabets and storing them in another list
            sorted.append(i)
print("".join(sorted))  #printing list as a string