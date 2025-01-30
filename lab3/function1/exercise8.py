
def order007(spisok):

    list007 = []
    for i in spisok:
        if i == 0 or i == 7:
            list007.append(i)

    flag = False
    for i in range(len(list007)-2):
        if(list007[i] == 0 and list007[i+1] == 0 and list007[i+2] == 7):
            flag = True
    
    if flag:
        print("YES")
    else:
        print("NO")



order007([1, 2, 4, 0, 0, 7, 5]) 
order007([1, 0, 2, 4, 0, 5, 7])   
order007([1, 7, 2, 0, 4, 5, 0]) 