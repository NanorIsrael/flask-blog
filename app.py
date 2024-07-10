from flask import Flask
from apifairy import authenticate

from api.auth import auth

app = Flask(__name__)

@app.route('/')
@authenticate(auth)
def index():
	print(auth.current_user())
	return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
	app.run(debug=True)