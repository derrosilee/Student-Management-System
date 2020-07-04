from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_name = 'students_management.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Students(db.Model):
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(100), nullable=False)
	last_name = db.Column(db.String(100), nullable=False)
	admision_no = db.Column(db.Integer, nullable=False)
	blood_type = db.Column(db.String(10), nullable=False)
	religion = db.Column(db.String(100), nullable=False)
	sport = db.Column(db.String(50), nullable=False)
	medical_conditions = db.Column(db.String(100), nullable=False)
	grade = db.Column(db.Integer, nullable=False)
	parent_contact = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
	return "hello World"


if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)