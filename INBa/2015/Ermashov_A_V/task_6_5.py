# Создайте игру, в которой компьютер загадывает один из трех цветов светофора, а игрок должен его угадать.
# Ермашов А.В., 26.05.2016
import random
cvet = random.randint(1,3)
if cvet == 1: cvet="Красный"
elif cvet ==2: cvet="Желтый"
elif cvet ==3: cvet="Зеленый"
print("Угадайте цвет светофора: ")
otvet = input("\nВведите цвет: ")
while(otvet != cvet):
    print("\nНеправильно. Попробуй еще раз")
    otvet = input("\nВведите цвет: ")
 
print("Правильно! Это", cvet,"цвет!")
input("Нажмите ENTER для продолжения")
