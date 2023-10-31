import time #Добавил библиотеку времени для более реалистичной готовки

class Pizza(): #Создаю материнский класс пиццы 
    def __init__(self, thickness = 0.4, ingredients = ["Chesse", "ketchup"], time_of_cooking = 20):
        self.thickness = thickness
        self.ingredients = ingredients
        self.time_of_cooking = time_of_cooking
    def preparation(self): #Создаю метод подготовки перед готовкой
        print("Происходит подготовка перед выпечкой пиццы")
        time.sleep(0.5)
        print(f"Замешивается тесто толщиной {self.thickness}")
        time.sleep(1)
        print(f"Раскладывается начинка {self.ingredients}")
        time.sleep(1)
    def bake(self): # метод для готовки
        print(f"Пицца выпекается {self.time_of_cooking}")
        time.sleep(5)
    def cutting(self): #метод для нарезания
        print("Пицца нарезается")
        time.sleep(1)
    def packaging(self): #метод для упаковки
        print("Пицца упаковывается")
        time.sleep(1)


class Pizza_BBQ(Pizza):  #Создаю дочерний класс Пиццы с ббкью
    def __init__(self, thickness=0.4, ingredients=("Chesse"), time_of_cooking=20, bbq_sause = 0):
        super().__init__(thickness, ingredients, time_of_cooking)
        self.bbq_sause = bbq_sause
    def preparation(self):
        super().preparation()
        print("Происходит подготовка перед выпечкой пиццы")
        time.sleep(0.5)
        print(f"Замешивается тесто толщиной {self.thickness}")
        time.sleep(1)
        print(f"Раскладывается начинка {self.ingredients} и добавляется особый соус BBQ в количестве {self.bbq_sause}")


class Pizza_Peperoni(Pizza): #Создаю дочерний класс Пиццы с пеперони
    def __init__(self, thickness=0.4, ingredients=("Chesse", "ketchup"), time_of_cooking=20, number_of_peperoni = 0):
        super().__init__(thickness, ingredients, time_of_cooking)
        self.number_of_peperoni = number_of_peperoni
    def preparation(self):
        super().preparation()
        print("Происходит подготовка перед выпечкой пиццы")
        time.sleep(0.5)
        print(f"Замешивается тесто толщиной {self.thickness}")
        time.sleep(1)
        print(f"Раскладывается начинка {self.ingredients} и добавляется {self.number_of_peperoni} кусочков пеперони")
        time.sleep(1)

class Pizza_seafood(Pizza): #Создаю дочерний класс Пиццы с морепродуктами
    def __init__(self, thickness=0.4, ingredients=("Chesse"), time_of_cooking=20, seafood = ["salmon", "crab"]):
        super().__init__(thickness, ingredients, time_of_cooking)
        self.seafood = seafood
    def preparation(self):
        super().preparation()
        print("Происходит подготовка перед выпечкой пиццы")
        time.sleep(0.5)
        print(f"Замешивается тесто толщиной {self.thickness}")
        time.sleep(1)
        print(f"Раскладывается начинка {self.ingredients} и добавляются такие морепродукты как {self.seafood}")
        time.sleep(1)
    

# pizza1 = Pizza_BBQ(0.4, ("Chesse", "Tomato", "Cucumber"), 30, 3) #Создаю объекты
# pizza2 = Pizza_Peperoni(0.7, time_of_cooking=25, number_of_peperoni=10)
# pizza3 = Pizza_seafood(0.2)

print("Здравствуйте, вот наше меню:")
print("Пицца BBQ")
print("Пицца Пеперони")
print("Пицца с морепродуктами")
question = input("Желаете сделать заказ? y/n:  ")
while question != "y" or "n":
    if question == "n":
        print("Всего доброго, досвидание")
        quit()
    elif question == "y":
        break
    else:
        question = input("Желаете сделать заказ? y/n:  ")
orderList = []
order = int(input("Какую пиццу вы хотите заказать? (1 - BBQ, 2 - пеперони, 3 - с морепродуктами): "))    
while True:
    if order == 1:
        orderList.append(1)
        something_else = input("Вы заказали пиццу BBQ, чтото ещё? y/n: ")
        while something_else != "y" or "n":
            if something_else == "n":
                continue
            elif something_else == "y":
                order = int(input("Какую пиццу вы хотите заказать? (1 - BBQ, 2 - пеперони, 3 - с морепродуктами, 4 - завершить заказ): "))
                break
            else:
                something_else = input("Вы заказали пиццу BBQ, чтото ещё? y/n: ")
    elif order == 2:
        orderList.append(2)
        something_else = input("Вы заказали пиццу пеперони, чтото ещё? y/n: ")
        while something_else != "y" or "n":
            if something_else == "n":
                continue
            elif something_else == "y":
                order = int(input("Какую пиццу вы хотите заказать? (1 - BBQ, 2 - пеперони, 3 - с морепродуктами, 4 - завершить заказ): "))
                break
            else:
                something_else = input("Вы заказали пиццу BBQ, чтото ещё? y/n: ")
    elif order == 3:
        orderList.append(3)
        something_else = input("Вы заказали пиццу с морепродуктами, чтото ещё? y/n: ")
        while something_else != "y" or "n":
            if something_else == "n":
                continue
            elif something_else == "y":
                order = int(input("Какую пиццу вы хотите заказать? (1 - BBQ, 2 - пеперони, 3 - с морепродуктами, 4 - завершить заказ): "))
                break
            else:
                something_else = input("Вы заказали пиццу BBQ, чтото ещё? y/n: ")
    elif order == 4:
        False



