#Задача 7. Вариант 45
#Как шестая, только с балами.

#Зябко Антон
#20.05.2016

import random
Chudesa=("Пирамида Хеопса", "Висячие сады Семирамиды","Статуя Зевса"," Храм Артемиды"," Мавзолей в Галикарнасе"," Колосс Родосский","Александрийский маяк")
Chudo=random.randint(0,6)
rand=Chudesa[Chudo]
print("Попробуй угадать одно из семи чудес света, но у тебя все равно ничего не выйдет. Это невозможно.")
ball=100
otvet=0
while(otvet)!=(rand):
	otvet=input("Ну, попробуй угадай")
	if(otvet)!=(rand):
		print("Я же говорил, что ты не сможешь. Пробуй еще.")
		ball/=2
	elif(otvet)==(rand):
		print("Ты очень сильный маг. Поздравляю.")
		print("Твои жалкие балы:" +str(ball))
		break
input ("Нажмите enter для выхода")