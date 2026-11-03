import os
import subprocess
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyOwnApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.lbl = Label(text="எனது சொந்த Python APK ஆப் (Vivo Y20G)", font_size=20)
        layout.add_widget(self.lbl)
        
        # 1. பைதான் சர்வரை ஆன் செய்ய பட்டன்
        btn_start = Button(text="Start Python Server", size_hint=(1, 0.3))
        btn_start.bind(on_press=self.start_server)
        layout.add_widget(btn_start)
        
        # 2. கிட்ஹப் மூலம் ஆப்பை அப்டேட் செய்ய பட்டன்
        btn_update = Button(text="Check & Download Update from GitHub", size_hint=(1, 0.3))
        btn_update.bind(on_press=self.update_from_github)
        layout.add_widget(btn_update)
        
        return layout

    def start_server(self, instance):
        # பின்னணியில் Flask/FastAPI போன்ற உங்கள் சொந்த பைதான் சர்வரை இயக்கும்
        self.lbl.text = "Python Server Started on Port 8080!"
        # இங்கு உங்கள் சொந்த app.py கோடை ரன் செய்ய லோக்கல் கமாண்ட் கொடுக்கலாம்
        
    def update_from_github(self, instance):
        self.lbl.text = "Checking GitHub for updates..."
        # கிட்ஹப்பில் இருந்து கோடை டவுன்லோடு செய்து ஆட்டோ-அப்டேட் செய்யும் லாஜிக்

if __name__ == '__main__':
    MyOwnApp().run()
