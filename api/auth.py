from flask_httpauth import HTTPBasicAuth
import hashlib
import os
from werkzeug.security import generate_password_hash, check_password_hash


auth = HTTPBasicAuth()

# def generate_password_hash(password):
# 	salt = os.urandom(16)
# 	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8', ), salt, 100000)
# 	return salt + key

# def check_password_hash(stored_password, user_password):
# 	salt = stored_password[:16]
# 	stored_key = stored_password[16:]
# 	new_key = hashlib.pbkdf2_hmac('sha256', user_password.encode('utf-8', ), salt, 100000)
# 	print(new_key, stored_key)
# 	return new_key == stored_key

users = {
	"john": generate_password_hash("hello"),
	"susan": generate_password_hash("bye")
}


@auth.verify_password
def verify_password(username, password):
	if username in users and \
			check_password_hash(users.get(username), password):
		return username