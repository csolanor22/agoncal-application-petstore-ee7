from flask import Flask, jsonify, request, make_response
from config import config
from model.models import db, Country

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config['development']
app = create_app(enviroment)
  
  
@app.route('/country', methods=['GET'])
def get_all_countries():
    name = request.args.get('name')
    isoCode = request.args.get('isoCode')
    printableName = request.args.get('printableName')
    iso3 = request.args.get('iso3')
    numcode = request.args.get('numcode')
    if name != None or isoCode != None or printableName != None or iso3 != None or numcode != None:
       countries = [ Country.json(country) for country in Country.query.filter((Country.name == name) |
                                                                            (Country.isoCode == isoCode) |
                                                                            (Country.printableName == printableName) |
                                                                            (Country.iso3 == iso3) |
                                                                            (Country.numcode == numcode)) ] 
    else:
        countries = [ Country.json(country) for country in Country.query.all() ] 
    return jsonify(countries)

@app.route('/country/<int:id>', methods=['GET'])
def get_country(id):
  try:
    country = Country.query.filter_by(id=id).first()
    if country:
      return make_response(jsonify(country.json()), 200)
    return make_response(jsonify({'message': 'country not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting country'}), 500)


@app.route('/country', methods=['POST'])
def create_country():
  try:
    data = request.get_json()
    new_country = Country(version=1, isoCode=data['isoCode'], name=data['name'], printableName=data['printableName'], iso3=data['iso3'], numcode=data['numcode'])
    db.session.add(new_country)
    db.session.commit()
    return make_response(jsonify({'message': 'country created'}), 201)
  except e:
    return make_response(jsonify({'message': 'error creating country'}), 500)

@app.route('/country/<int:id>', methods=['PUT'])
def update_country(id):
  try:
    country = Country.query.filter_by(id=id).first()
    if country:
      data = request.get_json()
      country.isoCode = data['isoCode']
      country.name = data['name']
      country.printableName = data['printableName']
      country.iso3 = data['iso3']
      country.numcode = data['numcode']
      db.session.commit()
      return make_response(jsonify({'message': 'country updated'}), 200)
    return make_response(jsonify({'message': 'country not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating country'}), 500)
  
@app.route('/country/<int:id>', methods=['DELETE'])
def delete_country(id):
  try:
    country = Country.query.filter_by(id=id).first()
    if country:
      db.session.delete(country)
      db.session.commit()
      return make_response(jsonify({'message': 'country deleted'}), 200)
    return make_response(jsonify({'message': 'country not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting country'}), 500)

  
if __name__ == '__main__':
    app.run(debug=True)