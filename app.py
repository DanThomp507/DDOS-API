from models import Accesslog
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kqqosbjxojgacl:11035ded7ad1a400c28f78af1d37b7e054c7362f7ecee3ee55fb596a106f1c17@ec2-18-232-143-90.compute-1.amazonaws.com:5432/d7p5nmq38d18j5'


@app.route('/')
def hello():
    return "DDOS Protector API"


@app.route('/all', methods=['GET'])
def handle_logs():
        query = """
        SELECT * FROM accesslog;
        """
        print(query)
        return query


if __name__ == '__main__':
    app.run()
