
# ----------- Default python libraies to be used ------------
import json
import time
from datetime import datetime
# ---------------------------------------------------------


# ------- The kivy UI library and all the used methods/ widgets
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.graphics import Rectangle, Color
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ListProperty 
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.uix.button import Button
# -------------------------------------------------------------



# ---------------Declare you custom files/modules here for better collaboration ---------------

# from src 

# ---------------------------------------------------------------------------------------------



"""
    window size for testing and development
    After development make sure to remove the default screen size 
    to make it adaptive on every android/ ios device.

    You can use this default size on presentation to also avoid ovalaping widgets 
"""
Window.size = (350, 700)

class SomeError(Exception):
    pass

# main entry app class holding the widgetsand files to render
class Tours(MDApp):


    # add constants here direct to here to the parent class or use the < __init__ !> method
    async def intrests(self, intrests):
        return intrests

    async def user_registration(self, username, email, password, confirm_password):

        intrests = await self.intrests()

        try:
            if confirm_password != password:
                raise SomeError()
            else:

            return {
            "username"  : username,
            "email" : email,
            "password" : password,
            "intrests" : intrests
            }
            
        except:
            return {
            "username"  : username,
            "email" : email,
            "password" : password,
            "intrests" : intrests
            } 


    # rendering function to display the screens
    def build(self):

        global screen_manager
        screen_manager = ScreenManager()

        """ 
            Declare different pages here with the name and path < components/file_name.kv ! >

            - Pages files are placed in the components folder
            - Pages files should be a kivy file -> FORMAT : <file_name>.kv

         Render the pages using screen manager
        # """
        screen_manager.add_widget(Builder.load_file("components/splashscreen.kv"))
        screen_manager.add_widget(Builder.load_file("components/startscreen.kv"))

        """
                 How to collect user data


                 {
                    "username" : "the name",
                    "intrests" : ["park", "rand", "rand2", "rand3", "rand4"]
                 }
        """
        screen_manager.add_widget(Builder.load_file("components/signup.kv"))
        screen_manager.add_widget(Builder.load_file("components/interests.kv"))
        screen_manager.add_widget(Builder.load_file("components/signin.kv"))
        screen_manager.add_widget(Builder.load_file("components/homepage.kv"))

        
        """
        on returning the screen_manager all pages are preloaded and will only been 
        displayed when called by a call_back function or any user action
        """
        return screen_manager


# initilizer
if __name__ == '__main__':
    # if you want to add other fonts donwload and unzip it to the font folder  and call it her and shown below
    LabelBase.register(name='Poppins', fn_regular='src/assets/font/Poppins-Regular.ttf')
    # on calling the entry class with the mDApp inherited; it will run the declared screen manager < Line 81!> 
    Tours().run()
