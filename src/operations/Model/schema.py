"""
	I will declare all needed schemas here both for validation 
	and database operations 
	I am using pydantic for validation and tortoise as the DB orm
	I am not sure about the database to use, but its all up to you
"""
import time
from enum import Enum
from datetime import datetime
from typing import Optional
from pprint import pprint

from rich.console import Console
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
# schema libraries
from pydantic import Field
from pydantic import AnyUrl
from pydantic import ConfigDict
from pydantic.dataclasses import dataclass 
from pydantic import BaseModel, ValidationError, validator
from pydantic import Field, EmailStr


# console config
console = Console()


# a list of all user interests
INTRESTS = [
	"churches",
	"resorts",
	"beaches",
	"parks",
	"theatres",
	"museums",
	"malls",
	"zoo",
	"restaurants",
	"pubs_bars",
	"local_services",
	"burger_pizza_shops",
	"hotels_other_lodgings",
	"juice_bars",
	"art_galleries",
	"dance_clubs",
	"swimming_pools",
	"gyms",
	"bakeries",
	"beauty_spas",
	"cafes",
	"view_points",
	"monuments",
	"gardens"
]



# error for user not present/ not in database
class NoIntrest(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
        super().__init__(message)



# user registration schema
@dataclass
class Registration(BaseModel):

	username: str = Field(default=None)
	email: EmailStr = Field(default=None)
	password: str = Field(default=None)
	Intrests: list = Field(default=[None])

	# username validator
	@validator('password')
	def weak_or_short_pass(cls, value) -> str:

		if (value is None) or (len(value) < 8):
			raise ValueError("Password should have 8 or more characters")
		return value

# user signin
@dataclass
class UserSignin(BaseModel):
	
	email: EmailStr = Field(default=None)
	password: str = Field(default=None)



def check(**kwargs: Registration):
	return kwargs



if __name__ == "__main__":



	new_user = Registration(
		username="Shadrack",
		email="shadcodes@gmail.com",
		password="Meolimioo)*@)"
	)
	# old_user_by_username = UsernameSignin(
	# 	username="shadrack",
	# 	password="Meolimioo)*@)"
	# )
	print(new_user.username)

	# console.log(Registration.__pydantic_model__.schema())
	# console.log(UsernameSignin.__pydantic_model__.schema())
	