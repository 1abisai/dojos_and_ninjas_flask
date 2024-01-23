from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/')
def dashboard():
    return render_template('index1.html', dojos_list=Dojo.get_all())

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')

@app.route('/new_dojo')
def new_dojo():
    return redirect('/')

@app.route('/show/<int:id>')
def get_one_ninja(id):
    return render_template("show.html", ninjas=Dojo.read_ninjas(id))


@app.route('/new_ninja')
def new_ninja():
    return render_template("index2.html", dojos=Dojo.get_all())


@app.route('/create_ninja', methods=["POST"])
def create_ninja():

    Ninja.create(request.form)
    print(request.form['dojo_id'])
    return redirect(f'/show/{request.form['dojo_id']}')