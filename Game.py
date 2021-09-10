import os
import time
import random
import pyfiglet

banner1 = pyfiglet.figlet_format('Hackers')
print(banner1)

time.sleep(2)
print('Starting...')
time.sleep(2)
os.system('cls')
print(banner1)

a = random.randint(100, 999)
b = random.randint(100, 999)
c = random.randint(100, 999)
print('New Ip adress found :- ')
print(a, '.', b, '.', c)
print()
print('__________________COMMAND NEEDED_______________________')
print()
time.sleep(5)
print('Give command to system :- \n (a).Attack \n (b).No-Attack \n')
i = input('Enter your choice :-')

if i=='a' :
   print('Attacking')
   i = random.randint(1000, 9999)
   j = random.randint(1000, 9999)
   print('Loot Avaliable :- ', i)
   print('Coins Avaliable :- ', j)
   print()
   print('Enter Option : \n (a).Loot all \n (b).Exit')
   u = input('Enter Option :-')
   if u=='a' :
     print('Looting all Resources..')
     time.sleep(2)
     print('Resources looted Sucessfully...')
     time.sleep(3)
     os.system('cls')
     print('Options : \n (a).Stay \n (b).Exit')
     n = input('Enter Options :-')
     time.sleep(2)
     if n=='b' :
       print('Exiting...')
       time.sleep(2)
       exit()
   time.sleep(10)

else :
    os.system('cls')
    print(banner1)
    time.sleep(2)    
