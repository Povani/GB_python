"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    color = {'красный': 7, 'желтый': 2, 'зеленый': 7}

    def running(self):
        while True:
            for key in TrafficLight.color:
                print(key)
                self.color = dict(TrafficLight.color)
                sleep(TrafficLight.color.get(key))


my_TrafficLight = TrafficLight()
my_TrafficLight.running()
