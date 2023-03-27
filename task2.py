import random

bush = list(random.randint(1,5) for i in range(int(input("Введите количество кустов: "))))
print(bush)
num_bush = int(input("Введите номер куста: "))

temp = 0
if num_bush ==1:
    temp = bush[0] + bush[1] + bush[-1]    #0.1.6 
    # print(temp)    
elif num_bush == len(bush):
    temp = bush[-2] + bush[-1] + bush[0]   #0.5.6
else:
    temp = bush[num_bush-1]  + bush[num_bush-2] + bush[num_bush]   #1.2.3
print(f" ягод - {temp}")    
