plan_to_do = []

"""Функція сортування списку задач"""
def my_sort(item):
    """Так як ми зберігаємо час під індексом 1, то потрібно повертати саме його для правильного сортування задач"""
    return item[1]

def print_plan(plan):
    print("-" * 80)
    if plan:
        print("Ваші плани:")
        idx = 0
        for task , task_time in plan:
            idx += 1
            print(f"{idx}) {task_time} - '{task}'")
    else:
        print("Планів поки не збережено")
    print("-" * 80, "\n")

while True:
    user_choice = input("1.Додати плани\n"
                        "2.Передивитися розпорядок на день\n"
                        "3.Видалити пункт з плану\n"
                        "4.Змінити пункт у плані\n"
                        "5.Вихід\n"
                        "Введіть дію: ")

    print()

    if user_choice == "1":
        new_plan = input("Ведіть новий пункт до плану: ")
        new_time = input("Введіть час для виконання заданого пункту: ")
        plan_to_do.append([new_plan, new_time])
        plan_to_do.sort(key = my_sort)
        print(f"Пункт '{new_plan}' запланований на {new_time} успішно додано!", "\n")

    elif user_choice == "2":
        print_plan(plan_to_do)

    elif user_choice == "3":
        index = int(input("Введіть пункт який бажаєте видалити: ")) - 1
        if 0 <= index < len(plan_to_do):
            del plan_to_do[index]
            print(f"Пункт {index + 1} видалено!", "\n")
        else:
            print(f"Пункт {index + 1} не знайдено!", "\n")  
    
    elif user_choice == "4" :
        print_plan(plan_to_do)
        change_item_index = int(input("Введіть номер пункту який бажаєте змінити: \n")) - 1
        new_item_plan = input("Введіть дію на яку бажаєте змінити обраний пункт: ")
        new_item_time = input("Введіть час на який запланувати дану дію: ")
        if 0 <= change_item_index < len(plan_to_do):
            plan_to_do[change_item_index] = [new_item_plan, new_item_time]
            plan_to_do.sort(key = my_sort)
            print(f"Пункт {change_item_index + 1} успішно оновлено", "\n")
        else:
            print(f"Пункт {change_item_index + 1} не знайдено!", "\n")

    elif user_choice == "5":
        print("Вихід", "\n")
        break

    else:
        print("Ця дія не доступна!", "\n")
