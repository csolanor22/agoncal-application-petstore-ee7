from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(2), nullable=False)
    isoCode = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    printableName = db.Column(db.String(80), nullable=False)
    iso3 = db.Column(db.String(3), nullable=False)
    numcode = db.Column(db.String(3), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'version': self.version,
            'isoCode': self.isoCode,
            'name': self.name,
            'printableName': self.printableName,
            'iso3': self.iso3,
            'numcode': self.numcode,
        }
