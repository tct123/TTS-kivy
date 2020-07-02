from kivy.uix.button import Button
from  kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window

import pyttsx3
import pygame
import os
import glob


pygame.init()
engine = pyttsx3.init()
count=0
sc = pygame.display.set_mode((1, 1))





def to_file(text,name):
    engine.save_to_file(text,'Audio/'+name+'.wav')
    engine.runAndWait()


class ttsApp(App):
    def build(self):
        mbl=BoxLayout(orientation='vertical',
                      padding=[20,20,20,20])

        bl=BoxLayout(padding=[20,20,20,20],
                     spacing=40,height=.1)
        # Window.bind(on_request_close=self.clear)
        self.ti=TextInput(height=.9)

        b_conv=Button(text='Конвектировать')
        b_conv.bind(on_press=self.f_conv)

        b_pause=Button(text='Pause')
        b_pause.bind(on_press=self.f_pause
                     )
        b_play=Button(text='Play')
        b_play.bind(on_press=self.f_play)

        mbl.add_widget(self.ti)
        bl.add_widget(b_play)
        bl.add_widget(b_conv)
        bl.add_widget(b_pause)
        mbl.add_widget(bl)

        return mbl
    def f_conv(self,instance):
        global count
        to_file(self.ti.text,str(count))
        pygame.mixer.music.load('Audio/'+str(count)+'.wav')
        pygame.mixer.music.play()
        count+=1


    def f_pause(self,instance):
        pygame.mixer.music.pause()
    def f_play(self,instance):
        pygame.mixer.music.unpause()
    # def clear(self,instance):
    #     files = glob.glob('/Audio/*')
    #     for f in files:
    #         print(1)
    #         os.remove(f)
    #     print(1)
    #     return False
if __name__ == '__main__':
    app = ttsApp()
    app.run()
