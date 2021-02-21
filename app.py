
"""
Layout - типа компоновщиков.

box-layout - вертикальная ориентация и горизонтальная. То есть все виджеты находятся четко друг под другом
grid layout - сетка, таблица.
staclayout - туча boxlaoyt, идущих друг за другом в строк или в столбец, то есть расположение не семетрично.
anchorlayout - подходит для фиксации меню сверху.
page layout - для создания страниц и перелистывания, как раз подойдет для различных страниц.


размеры виджетов:
size - размер в пикселях(фиксированно)
sizehint - в процентах от свободного места(0-1)

Положение виджетов на Layout определяется свойствами
- pos - в пикселях
- pos_hint - в процентах
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.core.window import Window



from kivy.config import Config

Config.set('kivy', 'keyboard_mode',
           'systemanddock')

# Window.size = (720, 1200)
# Window.size = (480, 840)

def get_ing(m):
    nitro_1 = str(10*m/1000)
    nitro_2 = str(10 * m / 1000)
    nitro_3 = str(10 * m / 1000)
    nitro_4 = str(10 * m / 1000)
    nitro_5 = str(10 * m / 1000)

    return {'nitro_1': nitro_1, 'nitro_2': nitro_2, 'nitro_3': nitro_3, 'nitro_4': nitro_4, 'nitro_5': nitro_5}

class Container(GridLayout):

    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingridients = get_ing(mass)

        self.nitro_1.text = ingridients.get('nitro_1')
        self.nitro_2.text = ingridients.get('nitro_2')
        self.nitro_3.text = ingridients.get('nitro_3')
        self.nitro_4.text = ingridients.get('nitro_4')
        self.nitro_5.text = ingridients.get('nitro_5')

class MyApp(MDApp):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()
