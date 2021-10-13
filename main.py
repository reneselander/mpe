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