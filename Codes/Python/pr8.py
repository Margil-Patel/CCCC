def sort():
    if order=="A":
        Sl=sorted(list1)
    elif order=="D":
        Sl=sorted(list1,reverse=True)
    else:
        print("involid")
    return Sl
list1=input("enter the list elements\n").split()
list1=[int(n) for n in list1]
order=input("A or D\n")
Sl=sort()
print(Sl)