import random

letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j',
           'k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I',
           'O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','V','B','N','M']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(','],','?','[','.',':','{','}','=','+','-','_','|','/','~','`','>','<',',']
           
plus = letters + numbers + symbols

passwordLength = 15
passwordList = []

for i in range(passwordLength):
    passwordList.append(random.choice(plus))
random.shuffle(passwordList)

passwordString = ''
for i in passwordList:
    passwordString += i
print(passwordString)


