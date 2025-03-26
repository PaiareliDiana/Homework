my_score = 0
cat = input("З якої категорії хотіли б почати?: \nУкраїна \nМашини\nСпорт")

if cat == "Україна":
    first_quest = input("Яких кольорів прапор України?\n 1. жовтого\n 2. блакитного\n 3. жовтого і блакитного ")
    if first_quest == "3":
        print("✅")
        my_score = my_score + 1
    else:
        print("😿")
        my_score = my_score - 1 

    second_quest= input("Яка столиця України? \n1. Київ\n 2. Одесса\n 3. Львів ")
    if second_quest != "1":
        print("😿")
        my_score = my_score - 1
    elif second_quest == "1":
        print("✅")
        my_score = my_score + 1

    third_quest = input("Скільки областей в Україні?: \n1.24 \n2.26 \n3.30 ")
    if third_quest =="1":
        print("✅")
        my_score = my_score + 1
    else:
        print("😿")
        my_score = my_score - 1

    forth_quest = input("Хто є автором гімну України?: \n1.Тарас Шевченко \n2.Павло Чубинський \n3. Іван Франко ")
    if forth_quest!="2":
        print("😿")
        my_score = my_score - 1
    elif forth_quest =="2":
        print("✅")
        my_score = my_score + 1
    
    fifth_quest = input("Яка найбільша річка в Україні?: \n1.Дунай \n 2.Дніпро \n 3.Південний Буг ")
    if fifth_quest =="2":
        print("✅")
        my_score = my_score + 1
    else :
        print("😿")
        my_score = my_score - 1


elif cat == "Машини":
    quest_6 = input("Яка країна створила BMW?:\n1. Україна\n2. Швеція\n3. Німеччина ")
    if quest_6 != "3":
        print("😿")
        my_score = my_score - 1
    else:
        print("✅")
        my_score = my_score + 1

    quest_7 = input("В якої машини 4 кружечки?:\n 1.Audi\n 2.Mustang\n 3.Renault ")
    if quest_7 == "1":
        print("✅")
        my_score = my_score + 1
    else:
        print("😿")
        my_score = my_score - 1

    quest_8 = input("Яке паливо використовується в електромобілях?: \n1.Електроенергія \n2.Бензин \n3.Сонячна енергія ")
    if quest_8 =="1":
        print("✅")
        my_score = my_score + 1
    else:
        print("😿")
        my_score = my_score - 1

    quest_9 = input("Яка країна є батьківщиною марки Ferrari?: \n1.Італія \n2.Швеція\n3. Нідерланди ")
    if quest_9 =="1":
        print("✅")
        my_score = my_score + 1
    else:
        print("😿")
        my_score = my_score - 1

    quest_10 =input("Яка компанія першою випустила масовий електромобіль?:\n1.Nissan \n2.Ford\n3.Tesla ")
    if quest_10 =="3":
        print("✅")
    else:
        print("😿")
        my_score = my_score - 1

elif cat =="Спорт":
    quest_11 = input("Скільки гравців має бути у футбольній команді?\n1. 11\n2. 25\n3. 15 ")
    if quest_11 == "1":
        print("✅")
        my_score = my_score + 1
    else:
        print("😿")
        my_score = my_score - 1


    quest_12 = input("Яка країна Батьківщина Карате?\n 1.Україна\n 2.Китай\n 3.Японія ")
    if quest_12 == "3":
        print("✅")
        my_score = my_score + 1
    else:
        print("😿")
        my_score = my_score - 1


    quest_13 = input("Спорт який називають королем спорту?\n 1.фігурне катання\n2. футбол ")
    if quest_13 == "2":
        print("✅")
        my_score = my_score + 1
    else:
        print("😿")
        my_score = my_score - 1

    quest_14 = input("Скільки кілець на олімпійському логотипі? : \n1.4 \n2. 7\n3.5")
    if quest_14 =="3":
        print("✅")
        my_score = my_score + 1
    else :
        print("😿")
        my_score = my_score - 1

    quest_15 = input("У якому виді спорту використовують ключку та шайбу?:\n1.Хокей\n2.Гольф\n3.Поло ")
    if quest_15 == "1":
        print("✅")
        my_score = my_score + 1
    else:
        print("😿")
        my_score = my_score - 1

print(f"Ваші бали {my_score}/15!")
