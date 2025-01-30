
def palindrom(s):
    return s == s[::-1]

stroka = input()
if(palindrom(stroka)):
    print("Da, eto palindrom")
else:
    print("No, eto ne palindrom")