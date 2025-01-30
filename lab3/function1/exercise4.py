
def check_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def simple(*args):
    list_simple = []
    for number in args:
        if check_number(int(number)):
            list_simple.append(int(number))
    return list_simple


number_list = input().split()
print(simple(*number_list))