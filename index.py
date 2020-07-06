from flask import Flask, render_template, request, redirect, url_for
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

	def __repr__(self):
		return f"{self.admision_no}"


@app.route('/')
def index():
	students = Students.query.all()
	return render_template('admin.html', Students=students)

@app.route('/delete/<int:id>')
def delete(id):
	student_to_delete = Students.query.get_or_404(id)
	db.session.delete(student_to_delete)
	db.session.commit()
	return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	student = Students.query.get_or_404(id)
	if request.method == 'POST':
		student.first_name = request.form['firstname']
		student.last_name = request.form['lastname']
		student.admision_no = request.form['adm']
		student.blood_type = request.form['blood']
		student.religion = request.form['religion']
		student.medical_conditions = request.form['medical']
		student.grade = request.form['grade']
		student.parent_contact = request.form['parent']
		db.session.commit()
		return redirect(url_for('index'))
	else:
		return render_template('update.html', id=id, students=student)

	













if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)