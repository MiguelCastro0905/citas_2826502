from . import app, db
from .models import Medico , Paciente , Consultorio
from flask import render_template, request, flash, redirect 



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

@app.route("/consultorios/create", methods = ['GET','POST'])
def create_consultorio():
    if(request.method == 'GET'):
        nc = []
        return render_template("consultorio_form.html",
                               numero = nc)
    
    elif(request.method == 'POST'):
        
            new_consultorio = Consultorio(numero = request.form ["nc"])
            db.session.add(new_consultorio)
            db.session.commit()
            return "consultorio registrado"


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

@app.route("/pacientes/create", methods = ['GET' , 'POST'] )
def create_paciente():
 
    if(request.method == 'GET'):
        tipo_sangre = [
            "A-",
            "B+",
            "O+",
            "AB-"
        ]
        return render_template("paciente_form.html",
                                tipo_sangre = tipo_sangre)

    elif(request.method == 'POST'):
            #cuando se presiona 'guardar'
            #crear un objeto de tipo medico
            new_paciente = Paciente(nombre = request.form["nombre"],
                                apellidos = request.form["apellidos"],
                                tipo_identificacion = request.form["ti"],
                                numero_identificacion = request.form["ni"],
                                altura = request.form["al"],
                                tipo_sangre = request.form["ts"]
                                )
            #añadirlo a la sesion sqlalchemy
            db.session.add(new_paciente)
            db.session.commit()
            return "paciente registrado"


#ruta de consultorio
@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html",
                            con = consultorio)


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
        flash("Medico registrado correctamente")
        return redirect("/medicos")
    
    
@app.route("/medicos/update/<int:id>", methods=["POST", "GET"])
def update_medico(id):
    especialidades = [
            "Cardiologia",
            "Odontologia",
            "Urologia"

        ]
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html",
                           medico_update = medico_update, 
                           especialidades = especialidades)
    elif(request.method == "POST"):
        #actualizara el medico, con los datos del form
        medico_update.nombre = request.form["nombre"]
        medico_update.apellidos = request.form["apellidos"]
        medico_update.tipo_identificacion = request.form["ti"]
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"]
        db.session.commit()
        return "Medico actualizado"  
    
@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect ("/medicos")
          


     