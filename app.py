from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)


@app.route('/')
def index():
    students = session.query(Student).all()
    # students=Student.query.all()
    return render_template('index.html', students=students)


@app.route('/details/<int:id>')
def details(id):
    s = session.query(Student).get(id)
    return render_template('details.html', s=s)


@app.route('/delete/<int:id>')
def delete(id):
    s = session.query(Student).get(id)
    session.delete(s)
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    st = session.query(Student).get(id)
    if request.method == "POST":
        n = request.form['name']
        e = request.form['email']
        st.name=n 
        st.email=e 
        session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', st=st)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        n = request.form['name']
        e = request.form['email']
        new_user = Student(name=n, email=e)
        session.add(new_user)
        session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
