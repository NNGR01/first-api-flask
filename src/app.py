from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db , Test


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app)
Migrate(app, db)

@app.route('/api/test', methods=['GET'])
def get_test():
    all_test = Test.query.all()
    all_test = list(map(lambda test: test.serialize() , all_test ))


    """ print(all_test) """
    return jsonify(all_test), 200

@app.route('/api/test', methods=['POST'])
def post_test():    
    
    """ datos = request.get_json()

    test = Test() 
    test.name = datos['name']
    test.phone = datos['phone']

    test.save() """

    name = request.json.get('name')
    phone = request.json.get('phone')

    test = Test()
    test.name = name
    test.phone = phone
    test.save()



    return jsonify(test.serialize()), 201

if __name__ == '__main__':
    app.run()


# 00:34:50    