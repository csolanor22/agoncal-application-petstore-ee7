from flask import Flask, jsonify, request, make_response
from config import config
from model.models import db, Category

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config['development']
app = create_app(enviroment)
  
  
@app.route('/category', methods=['GET'])
def get_all_countries():
    name = request.args.get('name')
    description = request.args.get('description')
    if name != None or description != None:
      categories = [ Category.json(category) for category in Category.query.filter((Category.name==name) | (Category.description==description))]
    else:
      categories = [ Category.json(category) for category in Category.query.all() ] 
    return jsonify(categories)

@app.route('/category/<int:id>', methods=['GET'])
def get_category(id):
  try:
    category = Category.query.filter_by(id=id).first()
    if category:
      return make_response(jsonify(category.json()), 200)
    return make_response(jsonify({'message': 'category not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting category'}), 500)


@app.route('/category', methods=['POST'])
def create_category():
  try:
    data = request.get_json()
    new_category = Category(version=1, name=data['name'], description=data['description'])
    db.session.add(new_category)
    db.session.commit()
    return make_response(jsonify({'message': 'category created'}), 201)
  except e:
    return make_response(jsonify({'message': 'error creating category'}), 500)

@app.route('/category/<int:id>', methods=['PUT'])
def update_category(id):
  try:
    category = Category.query.filter_by(id=id).first()
    if category:
      data = request.get_json()
      category.name = data['name']
      category.description = data['description']
      db.session.commit()
      return make_response(jsonify({'message': 'category updated'}), 200)
    return make_response(jsonify({'message': 'category not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating category'}), 500)
  
@app.route('/category/<int:id>', methods=['DELETE'])
def delete_category(id):
  try:
    category = Category.query.filter_by(id=id).first()
    if category:
      db.session.delete(category)
      db.session.commit()
      return make_response(jsonify({'message': 'category deleted'}), 200)
    return make_response(jsonify({'message': 'category not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting category'}), 500)

  
if __name__ == '__main__':
    app.run(debug=True)