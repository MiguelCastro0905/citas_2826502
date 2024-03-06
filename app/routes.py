from . import app
from .models import Medico , Paciente , Consultorio
from flask import render_template 


#crear ruta  para ver los medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos )

#crear ruta pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes )

#crear ruta consultorio
@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorio.html" , consultorios=consultorios)

    