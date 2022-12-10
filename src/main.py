
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
from kivymd.uix.snackbar import BaseSnackbar
from kivy.properties import StringProperty, NumericProperty
# -------------------------------------------------------------


# ---------------Declare you custom files/modules here for better collaboration ---------------

from operations import places
from operations.Model import Model, schema
from operations.Model.Model import UserAuthentication

# ---------------------------------------------------------------------------------------------

"""
    window size for testing and development
    After development make sure to remove the default screen size 
    to make it adaptive on every android/ ios device.

    You can use this default size on presentation to also avoid ovalaping widgets 
"""
Window.size = (350, 700)




# toast snack bar for unmatched password for signup screen
class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")


# main entry app class holding the widgetsand files to render
class Tours(MDApp):




    def __init__(self):
        super().__init__()
        # global screen_manager
        self.screen_manager = ScreenManager()

    

    # rendering function to display the screens
    def build(self):

        """ 
            Declare different pages here with the name and path < components/file_name.kv ! >

            - Pages files are placed in the components folder
            - Pages files should be a kivy file -> FORMAT : <file_name>.kv

         Render the pages using screen manager
        # """
        self.screen_manager.add_widget(
            Builder.load_file("components/splashscreen.kv"))
        self.screen_manager.add_widget(
            Builder.load_file("components/startscreen.kv"))

        """
                 How to collect user data


                 {
                    "username" : "the name",
                    "intrests" : ["park", "rand", "rand2", "rand3", "rand4"]
                 }
        """
        self.screen_manager.add_widget(Builder.load_file("components/signup.kv"))
        self.screen_manager.add_widget(Builder.load_file("components/interests.kv"))
        self.screen_manager.add_widget(Builder.load_file("components/signin.kv"))
        self.screen_manager.add_widget(Builder.load_file("components/homepage.kv"))

        """
        on returning the screen_manager all pages are preloaded and will only been 
        displayed when called by a call_back function or any user action
        """
        return self.screen_manager
    
    # user registraion
    def user_registration(self, username, email, password, confirm_password):
        data = {
            "username": username,
            "email": email,
            "password": password,
        }

        # print()
        try:
            if confirm_password == password:

                data = {
                    "username": username,
                    "email": email,
                    "password": password,
                }

                status = Model.UserAuthentication()
                registration_status = status.user_signup_auth(data)
                
                if registration_status == 200:
                    return True
                
                elif registration_status == 400:
                    snackbar = CustomSnackbar(
                    text="Username is already taken!",
                    icon="information",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    radius=[10, 10, 10, 10]
                    )
                    snackbar.size_hint_x = (
                        Window.width - (snackbar.snackbar_x * 2)
                    ) / Window.width
                    snackbar.open()

                    return False


            elif confirm_password != password:
                snackbar = CustomSnackbar(
                    text="The password dont match!",
                    icon="information",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    radius=[10, 10, 10, 10]
                    )
                snackbar.size_hint_x = (
                    Window.width - (snackbar.snackbar_x * 2)
                ) / Window.width
                snackbar.open()

                return data

        except Exception as e:
            print(e.__name__)



    # user sign in
    def user_signin(self, username, password):

        values = {
            "username": username,
            "password": password
        }
        try:
            
            firebase_auth = UserAuthentication()
            response = firebase_auth.user_login_auth(values)

            if reponse["status"] == 200:
                return True
                
        except Exception as e:

            if e.__name__ == NameError:
                snackbar = CustomSnackbar(
                    text="No interests connected to this user!",
                    icon="information",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    radius=[10, 10, 10, 10]
                    )
                snackbar.size_hint_x = (
                    Window.width - (snackbar.snackbar_x * 2)
                ) / Window.width
                snackbar.open()

                return False


    def intrests(self, intrests):
        
        if len(intrests) > 0:
            return True
        
        else:
            snackbar = CustomSnackbar(
                text="Choose at least 5 intrests!",
                icon="information",
                snackbar_x="10dp",
                snackbar_y="10dp",
                radius=[10, 10, 10, 10]
                )
            snackbar.size_hint_x = (
                Window.width - (snackbar.snackbar_x * 2)
            ) / Window.width
            snackbar.open()

            return False


# initilizer
if __name__ == '__main__':
    # if you want to add other fonts donwload and unzip it to the font folder  and call it her and shown below
    LabelBase.register(
        name='Poppins', fn_regular='src/assets/font/Poppins-Regular.ttf')
    # on calling the entry class with the mDApp inherited; it will run the declared screen manager < Line 81!>
    Tours().run()
