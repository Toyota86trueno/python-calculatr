print('Hey This is a simple calculater programm which can add, substract, multiply, or divide. ')
ch = input('Enter the keyword for the corresponding action: add/substract/multiply/divide: ')
fir = input('Enter the first number: ')
sec = input('Enter the second number: ')
a = int(fir)
b = int(sec)
if ch == 'add':
    sum = a+b
    print('The answer is:', sum)

if ch == 'substract':
    sum = a-b
    print('The answer is:',sum)

if ch == 'multiply':
    sum = a*b
    print('The answer is:', sum)

if ch == 'divide':
    sum = a/b
    print('The answer is:', sum)
