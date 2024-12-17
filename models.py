from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname=db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Contact {self.name}>'
