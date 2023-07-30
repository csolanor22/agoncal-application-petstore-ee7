from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(3000), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'version': self.version,
            'name': self.name,
            'description': self.description
        }