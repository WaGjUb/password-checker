import validate_password
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_password_checker():
    return validate_password.password_checker()

@app.route("/verifypassword", methods=['POST'])
def is_valid_password():
    data = request.data.decode()
    password_checker = get_password_checker()
    valid_ret = password_checker.is_valid_password(data)
    return jsonify(valid_ret)

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8080)
