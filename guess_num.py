import random

print("Привіт!Давай пограєм в гру, я загадую число від 1 до 25," \
" а ти будеш намагатися вгадати по моїм підказкам")

def guess_number():
    random_num = random.randint(1, 25) 
    choice = 0
    while choice != random_num :
        choice = int(input("Вгадай число :\n"))
        if random_num < choice:
            print("Близенько але ні, візьми поменьше")
        elif random_num > choice :
            print("Візми число побільше")
        elif random_num == choice :
            print("Вгадав!!!")

variant = None

while variant != 1:
    guess_number()
    variant = input("Чи бажаєш пограти знову? \n1.Так \n2.Ні\n")
    if variant == "2":
        break
