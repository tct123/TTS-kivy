import os


import kivy
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.audio import SoundLoader
import pyttsx3

engine = pyttsx3.init()
kivy.require('2.0.0')

class ttsApp(App):

    def build(self):
        mbl = BoxLayout(orientation='vertical',
                        padding=[20, 20, 20, 20])

        bl = BoxLayout(padding=[20, 20, 20, 20],
                       spacing=40, height=.1)

        self.ti = TextInput(height=.9)
        self.sound = SoundLoader.load('converted.wav')
        self.time = None
        convertbutton = Button(text='Convert',on_press = self.convert)
        pausebutton = Button(text='Pause', on_press = self.f_pause)
        playbutton = Button(text='Play', on_press = self.f_play)

        mbl.add_widget(self.ti)
        bl.add_widget(playbutton)
        bl.add_widget(convertbutton)
        bl.add_widget(pausebutton)
        mbl.add_widget(bl)

        return mbl

    def convert(self, obj):
        engine.save_to_file(self.ti.text,'converted.wav')
        engine.runAndWait()
        self.sound = SoundLoader.load('converted.wav')
        os.remove('converted.wav')


    def f_pause(self, obj):
        if self.sound!=None:
            self.sound.stop()



    def f_play(self, obj):
        if self.sound != None:
            self.sound.play()



if __name__ == '__main__':
    app = ttsApp()
    app.run()
