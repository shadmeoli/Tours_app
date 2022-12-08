import json

from flask import Flask, jsonify, request
from flask_restful import Api
from flask_restful import Resource, abort
from flask import redirect 

# schemas
from Model.schema import Registration, UserSignin, Interests
from places import all_places



app = Flask(__name__)
api = Api(app)

# user signup
class UserRegistration(Resource):

	def get(self):
		return jsonify("Running API")

	def post(self):

		userdetails: Registration = request.get_json()
		
		if len(userdetails["Intrests"]) == 5 or len(userdetails["Intrests"] > 5):
			return redirect(userdetails)

		elif len(userdetails["Intrests"]) < 5:
			return jsonify(error="You need 5 or more Intrests", status_code=404)
		
		# else:
		# 	abort(404, message="No such user details")


class UserSignin(Resource):

	def post(self):
		userdetails: UserSignin = request.get_json()
		return jsonify(userdetails)


# all user intrests
class UserIntrest(Resource):

	def get(self):
	return jsonify("Some user intrests") 

# sending suggestions to user
class Recommendations(Resource):

	def get(self):
		return jsonify("Some user recommendations")




# endpoints
api.add_resource(UserRegistration, '/sign_up')
api.add_resource(UserSignin, '/sign_in')
api.add_resource(UserIntrest, '/home')
api.add_resource(Recommendations, '/expole')



if __name__ == "__main__":
	app.run(debug=True)
