import random
try:
    player_choice = input("Введите 'камень', 'ножницы' или 'бумага': ").lower()
    comp_choice = random.choice(['камень', 'ножницы', 'бумага'])
    print(f"Компьютер выбрал {comp_choice}")
    if comp_choice == player_choice:
        print("Ничья!")
    elif comp_choice == "камень":
        if player_choice == "бумага":
            print("Вы проиграли!")
        else:
            print("Вы выиграли!")
    elif comp_choice == "ножницы":
        if player_choice == "камень":
            print("Вы проиграли!")
        else:
            print("Вы выиграли!")
    else:
        if player_choice == "ножницы":
            print("Вы проиграли!")
        else:
            print("Вы выиграли!")
except Exception as e:
    print(e)