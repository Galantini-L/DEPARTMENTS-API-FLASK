from urllib import request
from wsgiref import validate
from flask import Blueprint, jsonify
from ..models.all_models import Model_Departaments
from validation import val_deptData

main = Blueprint('personal_blueprint',__name__)

@main.route('/')
def home():
    return '''<h1>HOME PAGE</h1>
            <h4>Endpoints access:</h4>
            <p>
                departaments: /departaments <br>
                specific departament : /departament/id
            </p>
            '''

@main.route('/insert/departments')
def add():
    req = request.get_json()
    validated_data = map(val_deptData,req)
    insert_dept = Model_Departaments.post_department(validated_data)
    return insert_dept

@main.route('/departaments/')
def get_departaments():
    try:
        departaments= Model_Departaments.get_departaments()
        return jsonify(departaments)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500


@main.route('/departament/<id>')
def get_departament(id):
    try:
        departament= Model_Departaments.get_departament(id)
        if departament != None:
            return jsonify(departament)
        else:
            return jsonify({'message':'id not found'})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500