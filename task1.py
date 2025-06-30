dict={"Alice":45,"John":65,"Virat":89,"Messy":76}
i=input("Enter the student's name: ")
if i in dict:
    print( i,"'s marks:" ,dict.get(i))
else:
    print("student not found")
