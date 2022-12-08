"""
	Using firebase as the database:
		- I will be defining here the model files
		- also the auth file
"""
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
from schema import Registration, UserSignin


cons = Console()

# connection to the application
cred = credentials.Certificate(
    "tours-eb670-firebase-adminsdk-ky8ly-946c723b7e.json")
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
            return user_query["intrests"]
        else:
            raise NoSuchUSer(value=value, message="Invalid uer credentials")
    
    
    # user sign in authentication from firebase
    def user_signup_auth(self, details: UserSignin):
        
        user = details["username"]
        user_query = self.database_query(user)
        
        if self.in_database(details) == False:
            new_user = database.collection(u'Users').document(u'{}'.format(user))
            new_user.set(details, merge=True)
            return {
                "Data_added" : details
            }
        else:
            raise NoSuchUSer(value=user, message="user already exists")

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

    _auth = UserAuthentication()

    user_login_auth = _auth.user_signup_auth(values)

    try:
        cons.log(user_login_auth)
    except Exception as e:
        cons.log(e)
