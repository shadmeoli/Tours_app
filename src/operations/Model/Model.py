"""
	Using firebase as the database:
		- I will be defining here the model files
		- also the auth file
"""
import sys, os
# sys.path.append('/home/meoli/Desktop/traveling-recommender')
import json

# authentication setup
import firebase_admin
import pyrebase
from firebase import firebase
from firebase import jsonutil
from firebase_admin import credentials, db, firestore
from firebase._async import process_pool
import uvicorn
import firebase_admin
import pyrebase
from rich.console import Console


# schem defination
from .schema import Registration, UserSignin # for app running
# from schema import Registration, UserSignin # for file running


cons = Console()

# connection to the application
cred = credentials.Certificate("src/operations/tours-eb670-firebase-adminsdk-ky8ly-946c723b7e.json")
firebase_admin.initialize_app(cred)
database = firestore.client()


# error for user not present/ not in database
class NoSuchUSer(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
        super().__init__(message)



class UserAuthentication():

    def __init__(self):
        pass

    def database_query(self, value: str):

        # querying firebase database
        user_ref = database.collection(u'Users').document(u'{}'.format(value))

        user_query = user_ref.get()
        user_query = user_query.to_dict()

        return user_query

    # checking if the user on our database
    def in_database(self, details) -> bool:

        user = details["username"]
        paswd = details["password"]

        user_query = self.database_query(user)

        if user_query != None:
            try:

                if user_query["username"] == user:
                    return True
                else:
                    return "Invalid user data"

            except Exception as e:
                raise NoSuchUSer(
                    value=user, message="Check your username and password")

        else:
            return False

    # validating user login
    def user_login_auth(self, details: UserSignin) -> bool:

        user = details["username"]
        paswd = details["password"]

        user_query = self.database_query(user)

        value = details["username"]

        if self.in_database(details):

            try:
                if len(user_query["intrests"]) >= 5:
                    return {"status" : 200,  "intrests" : user_query["intrests"]}
            
            except Exception as e:
                if Exception == KeyError:
                    return False            
    
    
    # user sign in authentication from firebase
    def user_signup_auth(self, details: UserSignin):
        
        user = details["username"]
        user_query = self.database_query(user)
        
        if self.in_database(details) == False:
            
            new_user = database.collection(u'Users').document(u'{}'.format(user))
            new_user.set(details, merge=True)
            
            return 200

        else:
            return 400
    
    # user intrests update
    def user_intrests(self, username:str, intrests: list):

        doc_ref.update({
            "intrests" : intrests
        })


if __name__ == '__main__':
    values = {
        "username": "some_otherverynewuser",
        "email": "onlunewmail@gmail.com",
        "password": "neadABCD!@#$",
        "intrests": [
            "chruch",
            "dance_clubs",
            "hotel",
            "restaurant",
            "park",
        ]
    }
    
    values2 = {
        "username": "Meolishad",
        "email": "shad.thee@yahoo.com",
        "password": "ABcd12#$"
    }


    _auth = UserAuthentication()

    user_signup_auth = _auth.user_signup_auth(values2)

    try:
        cons.log(user_signup_auth)
    except Exception as e:
        cons.log(e)
