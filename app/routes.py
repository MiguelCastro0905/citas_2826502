from . import app, db
from .models import Medico , Paciente , Consultorio
from flask import render_template, request 



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
    return render_template("consultorios.html" , consultorios=consultorios)


#crear ruta para traer el medico por id()
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):   
    #return "id del medico:" + str(id)
    #traer el medico por id utilizando la entidad medico
    medico = Medico.query.get(id)
    #meterlo a una lista
    #hay que llamar la consulta no la clase.
    return render_template("medico.html", 
                            med = medico )

#ruta de pacientes
@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html",
                            pac = paciente)


#ruta de consultorio
#@app.route("/consultorios/<int:id>")
#def get_consultorio_by_id(id):
    #Consultorio = 


#crear una ruta para crear nuevo medico
@app.route("/medicos/create", methods = ['GET' , 'POST'] )
def create_medico():
   #####mostrar el formulario: metodo GET
    if( request.method == 'GET' ):
        #EL usuario ingreso con navegador http://localhost:5000/medicos/create
        especialidades = [
            "Cardiologia",
            "Odontologia",
            "Urologia"

        ]
        return render_template("medico_form.html",
                                especialidades = especialidades)
    


    #####
    ## Cuando el usuario presiona el boton de guardar
    ## los datos del formulario viajan al servidor 
    ## utilizando el metodo POST

    elif(request.method == 'POST'):
        #cuando se presiona 'guardar'
        #crear un objeto de tipo medico
        new_medico = Medico(nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_medico)
        db.session.commit()
        return "medico registrado"