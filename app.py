
"""
https://fooobar.com/questions/14054372/how-to-get-id-and-text-value-of-a-kivy-button-as-string

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
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

import sqlite3



Config.set('kivy', 'keyboard_mode', 'systemanddock')
KV = '''
<Add>:
    task:task
    rows:2
    MDTextField:
        hint_text: "Задача"
        id: task


<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height
    type_swipe: "auto"
    on_swipe_complete: app.on_swipe_complete(root)

    MDCardSwipeFrontBox:

    MDCardSwipeFrontBox:
        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True


Screen:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'fon.jpg'

    BoxLayout:
        rows:3
        orientation: "vertical"

        MDToolbar:
            opacity: 0.7
            title: "BEST TODO"
            right_action_items: [["update", lambda x: app.update()]]
            left_action_items: [["exit-to-app", lambda x: app.stop()]]


        ScrollView:
            MDList:
                id: md_list
                padding: 0

        MDBottomAppBar:    
            MDToolbar:
                opacity: 0.5
                icon: 'plus'
                type: 'bottom'
                on_action_button: app.navigation_draw()    
'''


class Add(GridLayout):
    pass


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()


class MainApp(MDApp):
    icon = 'face.jpg'
    dialog = None


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "BlueGray"
        self.screen = Builder.load_string(KV)




    def build(self):
        return self.screen



    def update(self):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute('''SELECT task FROM tasks''')
        result = c.fetchall()
        # print(result)
        for i in result:
            task = i[0]
            self.screen.ids.md_list.add_widget(SwipeToDeleteItem(text=task))
        conn.close()


    def on_swipe_complete(self, instance):
        print(instance)  # FOR tests
        print(instance.text)  # FOR tests
        self.screen.ids.md_list.remove_widget(instance)
        DB.drop_from_db(instance.text)
        Snackbar(text='Так держать!').show()

    def remove_item(self, instance):
        print(instance)  # FOR tests
        self.screen.ids.md_list.remove_widget(instance)

    def navigation_draw(self):
        self.dialog = MDDialog(
            title="Что надо сделать?",
            type="custom",
            size_hint=(0.9, 1),
            content_cls=Add(),
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=self.close_dialog),
                MDFlatButton(
                    text="OK",
                    on_release=self.save_task),
            ],
        )
        self.dialog.open()



    def save_task(self, inst):
        print(self.dialog.content_cls.ids.task.text)
        task = self.dialog.content_cls.ids.task.text
        DB.save_from_db(task)
        self.screen.ids.md_list.add_widget(SwipeToDeleteItem(text=task))
        self.dialog.dismiss()



    def save(self):
        for i in range(self.screen.ids.md_list):
            print(i)

    def close_dialog(self, obj):
        self.dialog.dismiss()

class DB:
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task text)''')
    conn.commit()
    conn.close()




    def save_from_db(task):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()

        c.execute('''INSERT INTO tasks(task)
            VALUES (?)''', (task,))
        conn.commit()
        conn.close()

    def drop_from_db(task):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute('''DELETE FROM tasks WHERE task=? ''', (task,))
        conn.commit()
        conn.close()





if __name__ == "__main__":
    MainApp().run()
    DB = DB


