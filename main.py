#import random

'''
print('What is {} times {}?'.format(random.randrange(1, 11),random.randrange(1, 11)))
a = random.randrange(1, 11)
print(a)

from random import randrange

#print('What is {randrange(1, 11)} times {randrange(1, 11)}?')

#f-string (f) {} (bättre än .format)
#print(f'What is {randrange(0, 10)} times {randrange(0, 10)}?')

#Skapar en variabel som i det här fallet blir att heta name.
name = (input('Vad heter du?'))
alder = (input('Din ålder?'))

print (f"Hej {name} {name}")
,'\n'
print ('Du är', alder,'år.')
n1 = random.randint(50,150)
n2 = random.randint(150,250)
n3 = random.randint(250,500)

print('number1:', n1)
print('number2:', n2)
print('number3:', n3)

#Sum and average
"""n1 = random.randint(50,100)
n2 = random.randint(100,150)
n3 = random.randint(200,250)
summa = (n1 + n2 + n3)

print(summa)
average = (summa / 3)
print(average)"""

"""n1 = random.randint(50,150)
print(n1)
print(35)"""


"""num = "05012345"
print(num)"""

"""
potensen
a = 2
b = 4
c = a ** b

print(c)"""


result = 4
print((result - 2) * (result + 2) //result)

temperatur = float(input('Hur många grader är det idag? '))
idag = '° grader idag.'
print(f'Det är {temperatur}{idag}')
#print(f'Det är',temperatur,idag)
type(temperatur)'''
'''

#print(f'What is {randrange(0, 10)} times {randrange(0, 10)}?')

print(8 + 3)
print(8 - 3)
print(8 * 3)
print(8 // 3) #Flyttalsdivision, 5.7 2.4 etc... obs: inte kommatecken, endast punkt som decimal
print(8 / 3)
print(8 % 3)
print(8 ** 3)

taljare = int(input('Mata in täljaren: '))
namnare = int(input('Mata in nämnaren: '))

try:
        kvot = taljare // namnare
        rest = taljare % namnare

        print('kvot =', kvot)
        print('rest =', rest)

except:
        print('Du kan inte dividera med noll.')'''

#int(input('Your age please:'))
'''taljaren = float(input('mata in täljaren: '))
namnaren = float(input('mata in nämnaren: '))


try:
        print('svar: ',taljaren / namnaren)
except:
        print('Du kan inte dividera med 0.')'''

'''
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") '''
'''
for selander in 'René':
        print(selander, end = ' ')
'''
'''
def printHello():
    print('Hello')

def printWorld():
    print('World')

printHello()

printWorld()

printHello()'''
'''
def rakna_ut_arean_for_en_rektangel(width, height):
    print('Arean är', width * height)

rakna_ut_arean_for_en_rektangel(5, 4)'''
'''
for x in [1, 2, 3, 4, 5]:
    print(x)
print("Happy Birthday, dear " + fornamn + " "  + efternamn + "!")        print("Happy Birthday to you!")
    '''
'''
def felruta(x): 
     print(xxxxx)
                
 
def main():
     x = input("Enter first name of birthday hero: ")
     felruta(x)

main()'''
'''
def annualsalary(monthlysalary):
    print('')


annualsalary()'''
'''
menu = ['eggs', 'oatmeal', 'bacon']

print(menu[1])'''
'''
for tal in range (1, 10000):
    print(tal, '', end = '')'''
'''
a = add(multi(3));
a = a + mod(div(a + 3)) + sub(12)

print(a)'''
'''
def rutan(x):
        print (5 * x)
        print (5 * x)
        print (5 * x)
        print (5 * x)

rutan('penix')
print ()
rutan('A')
print ()
rutan('#')'''
'''
for tecken in 'Fazer':
    print(tecken, end = '')'''
'''
import random
 
from random import randrange
 
for i in range(1, 11):   
 
    x = random.randrange(0, 11)
 
    y = random.randrange(0, 11)
 
    tot = (x * y)
 
    a = int(input(f'What is {x} * {y}? '))
 
    if a == tot:
 
        print('Correct')
 
    else:
        print(f'Not correct, the correct answer is {tot}.')'''

import random

from random import randrange
 
for i in range(1, 11):
        
     num_1 = random.randrange(0, 11)
    
     num_2 = random.randrange(0, 11)
    
     result = (num_1 * num_2)

     while True:

         try:

             a = int(input(f'What is {num_1} times {num_2}? '))

             if a == result:

                print('Correct')

             else:

                print(f'Not correct, the correct answer is {result}.')

             break

         except ValueError:

                print("You did not enter an answer.")