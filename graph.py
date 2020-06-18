from kivy.uix.button import Button
from  kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class ttsApp(App):
    def build(self):
        mbl=BoxLayout(orientation='vertical',padding=[20,20,20,20])
        bl=BoxLayout(padding=[20,20,20,20],spacing=40,height=.1)
        t=TextInput(height=.9)
        b1=Button(text='Play')
        b2=Button(text='Pause')
        mbl.add_widget(t)
        mbl.add_widget(bl)
        bl.add_widget(b1)
        bl.add_widget(b2)
        return mbl

if __name__ == '__main__':
    app = ttsApp()
    app.run()