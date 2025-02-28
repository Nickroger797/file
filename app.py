from flask import Flask, jsonify
from database.database import db  # Import MongoDB

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Nickroger797'

# Route to fetch all users from MongoDB
@app.route('/users', methods=['GET'])
def get_users():
    users = list(db.users.find({}, {"_id": 0, "username": 1}))
    return jsonify(users)

if __name__ == "__main__":
    app.run()
