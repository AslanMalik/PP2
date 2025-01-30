def has_33(nums):
    flag = False
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            flag = True
    
    if flag:
        print("YES")
    else:
        print("NO")

has_33([1, 3, 3])   
has_33([1, 3, 1, 3])   
has_33([3, 1, 3]) 