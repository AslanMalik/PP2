def reverse_string(stroka):
    stroka = stroka.split()
    for i in range(len(stroka)):
        print(stroka[len(stroka)-1-i], end = " ")

string = input()
reverse_string(string)