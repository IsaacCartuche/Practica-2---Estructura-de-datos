import random
from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from CONTROLADOR.DaoServidorPublicoControl import DaoServidorPublicoControl
from CONTROLADOR.DaoTransaccionControl import DaoTransaccionControl
from CONTROLADOR.tda.linked.linkedList import Linked_List

from flask_cors import CORS
router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
CORS(router)
cors = CORS(router, resources={
    r"/*": {
        "origins": "*"
        }
    })

##########################################################################################################################################
@router.route('/')
def home():
    # return make_response(
    #     jsonify({"msg":"OK", "code": 200}),
    #     200
    # )
    return render_template("template.html", nombre = "Practica 2")
    
# LISTA PERSONA GET
@router.route('/personas')
def lista_personas():
    pd = DaoServidorPublicoControl()
    #return render_template("nene/lista.html", lista = pd.to_dict())
    return render_template("servidorpublico/lista.html", lista = pd.to_dict())

# LISTA PERSONA GET
@router.route('/personas/agregar')
def ver_guardar():
       return render_template("servidorpublico/guardar.html")

# LISTA PERSONA GET
@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = DaoServidorPublicoControl()
    nene = pd._lista.get(int(pos) -1 )
    print(nene)
    print("vamos bien!!!")
    return render_template("servidorpublico/editar.html", data = nene)

# GUARDAR PERSONA POST
@router.route('/personas/guardar', methods=['POST'])
def guardar_personas():
    pd = DaoServidorPublicoControl()
    data = request.form
    
    if "apellidos" not in data.keys():
        abort(400)
    #TODO validar
    pd._servidorPublico._nombres = data['nombres']
    pd._servidorPublico._apellidos = data['apellidos']
    pd._servidorPublico._numeroPila = data['numeroPila']
    pd.save
    return redirect("/personas", code = 302)


# MODIFICAR PERSONA POST
@router.route('/personas/modificar', methods=['POST'])
def modificar_personas():
    pd = DaoServidorPublicoControl()
    data = request.form
    pos = data["id"]
    nene = pd._lista.get(int(pos) - 1)
    
    if "apellidos" not in data.keys():
        abort(400)
        

    #TODO validar
    pd._servidorPublico = nene
    pd._servidorPublico._nombres = data['nombres']
    pd._servidorPublico._apellidos = data['apellidos']
    pd._servidorPublico._numeroPila = data['numeroPila']
    pd.merge(int(pos) - 1)
    return redirect("/personas", code = 302)
##########################################################################################################################################

###### TRANSACCIONES

#TRANSACCION GET
@router.route('/transaccion')
def lista_transaccion():
    tc = DaoTransaccionControl()
    #return render_template("nene/lista.html", lista = pd.to_dict())
    return render_template("transaccion/lista.html", lista = tc.to_dict())

# LISTA PERSONA GET
@router.route('/transaccion/agregar')
def ver_guardarTransaccion():
       return render_template("transaccion/guardar.html")

# LISTA PERSONA GET
@router.route('/transaccion/editar/<pos>')
def ver_editarTransaccion(pos):
    tc = DaoTransaccionControl()
    nene = tc._lista.get(int(pos) -1 )
    return render_template("transaccion/editar.html", data = nene)

# GUARDAR PERSONA POST
@router.route('/transaccion/guardar', methods=['POST'])
def guardar_transaccion():
    tc = DaoTransaccionControl()
    data = request.form
    
    if "ventanilla" not in data.keys():
        abort(400)
    #TODO validar
    tc._transaccion._ventanilla = data['ventanilla']
    tc._transaccion._fecha = data['fecha']
    tc._transaccion._tiempo = random.uniform(5, 20)
    tc._transaccion._detalle = data['detalle']
    tc._transaccion._calificacion = ""
    tc.save
    
    return redirect("/transaccion", code = 302)


# MODIFICAR PERSONA POST
@router.route('/transaccion/modificar', methods=['POST'])
def modificar_transaccion():
    tc = DaoTransaccionControl()
    data = request.form
    pos = data["id"]
    nene = tc._lista.get(int(pos) - 1)
    
    if "ventanilla" not in data.keys():
        abort(400)
        

    #TODO validar
    tc._transaccion = nene
    tc._transaccion._ventanilla = data['ventanilla']
    tc._transaccion._fecha = data['fecha']
    tc._transaccion._tiempo = random.uniform(5, 20)
    tc._transaccion._detalle = data['detalle']
    tc._transaccion._calificacion = ""
    tc.merge(int(pos) - 1)
    return redirect("/transaccion", code = 302)




##########################################################################################################################################
# RUTA DE ORDENAMIENTO

@router.route('/personas/ordenar')
def ordenar_personas():
    metodo = "1"
    criterio = "_id"
    tipo = "1"
    metodo = request.args.get("metodo", "1")
    criterio = request.args.get("selectcosa", "_id")
    tipo = request.args.get("selecttipo", "1")
    sp = DaoServidorPublicoControl() 
    listaa = sp._list()
    listaa.sort_models(criterio, int(tipo), int(metodo))
    i = 0
    listoforo = []
    while i < len(listaa.toArray._array):
        listoforo.append(listaa.toArray._array[i].serialize)
        i = i + 1
    return render_template("servidorpublico/ordenar.html", lista = listoforo)


@router.route('/transaccion/ordenar')
def ordenar_transaccion():
    metodo = "1"
    criterio = "_id"
    tipo = "1"
    metodo = request.args.get("metodo", "1")
    criterio = request.args.get("selectcosa", "_id")
    tipo = request.args.get("selecttipo", "1")
    sp = DaoTransaccionControl() 
    listaa = sp._list()
    listaa.sort_models(criterio, int(tipo), int(metodo))
    i = 0
    listoforo = []
    while i < len(listaa.toArray._array):
        listoforo.append(listaa.toArray._array[i].serialize)
        i = i + 1
    return render_template("transaccion/ordenar.html", lista = listoforo)


##########################################################################################################################################
# RUTA DE ORDENAMIENTO


@router.route('/personas/buscar')
def buscar_personas():
    metodo = request.args.get("metodo", "1")
    elemento = request.args.get("nombre", "")
    atributo = request.args.get("selectcosa", "_apellidos")
    pd = DaoServidorPublicoControl() 
    lista = Linked_List()
    lista = pd._list()
    #print(pd.to_dict())
    index = lista.search_binary_models(elemento,atributo)
    if(metodo == "1"):    
        if(index != -1):
            lista = pd._list()
            lista.sort_models(atributo, 1, 1)
            #print(lista.get(index).serialize)
            #print(lista.toArray._array)
            i = 0
            listoforo = []
            listoforo.append(lista.get(index).serialize)
            return render_template("servidorpublico/buscar.html", lista = listoforo)
    elif (index != -1):
        lista.search_binarySecuencial_models(elemento, atributo)
        print(type(lista.toArray._array))
        return render_template("servidorpublico/buscar.html", lista = lista.toArray._array)
    return render_template("servidorpublico/buscar.html", lista = pd.to_dict())

    
    
    


@router.route('/transaccion/buscar')
def buscar_transaccion():
    metodo = request.args.get("metodo", "1")
    elemento = request.args.get("nombre", "")
    atributo = request.args.get("selectcosa", "_ventanilla")
    pd =DaoTransaccionControl() 
    lista = Linked_List()
    lista = pd._list()
    index = lista.search_binary_models(elemento,atributo)
    if(metodo == "1"):    
        if(index != -1):
            lista = pd._list()
            lista.sort_models(atributo, 1, 1)
            listoforo = []
            listoforo.append(lista.get(index).serialize)
            return render_template("transaccion/buscar.html", lista = listoforo)
    elif (index != -1):
        lista.search_binarySecuencial_models(elemento, atributo)
        return render_template("transaccion/buscar.html", lista = lista.toArray._array)
    return render_template("transaccion/buscar.html", lista = pd.to_dict())
    