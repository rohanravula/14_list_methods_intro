# a=[]
# print(a,type(a))

# c=["hey hii rohan",39]
# print(c,type(c)) #['hey hi rohan', 39] list. in this we are printing the c and type of c also.
# print(c[0],type(1)) #hey hii rohan 'int. in this we are printing the index position 0 and we are printing the index postion 1 which type it is.
# print(c[0],type(0)) #hey hii rohan 'str'.
# print(c[1],type(1)) #39 'int'
# print(c[2]) #IndexError: list index is out of range. we will be getting the output as like this because the index postion 2 is not there in that list.

# d="hello"
# print(d,type(d)) #hello 'str'. the varable d is in str type so it is str
# print(d[0]) #h. at the index postition 0 is h so it print h
# print(d[-1]) #o. at the index postion -1 is o so it print o. in -1 it prints the last value.
# print(d[5]) #IndexError : string index out of range. coz at the index postion 5 is not there so it prints the error.
# d[0]="H" #TypeError: 'str' object does not support item assignment. which means in str we cannot do any modifications.

# x=[3,4.6,"rohan",None,True]
# print(x[0],type(0)) #3 'int'. at the index postion 0 their is 3 and 3 is int type
# print(x[1],type(x[1])) #4.6 'float'
# print(x[2],type(x[2])) #rohan 'str'
# print(x[3],type(x[3])) #None 'None' none is also a data type
# print(x[4],type(x[4])) #True 'bool'
# print(x[5],type(x[5])) #IndexErroe: list index out of range.

"how to do modification in list"
# r=[5,6.7,"python"]
# r[0]=6.6
# print(r) #[6.6,6.7,'python']at the index postion 0 previously it was 5 then we are saying that at the index postion 0 change it as 6.6.

n=[6,5.6,"hello",[4,6]]
# print(n[0],type(n[0])) #6 'int'
# print(n[1],type(n[1])) #5.6 'float'
# print(n[2],type(n[2])) #hello 'str'
# print(n[3],type(n[3])) #[4,6] 'list'
print(n[3][0],type(n[3][0])) 
print(n[3][1],type(n[3][1])) 
