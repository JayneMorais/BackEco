# -*- coding: utf-8 -*-

# Este modulo carrega todas as funções do flas
from flask import Flask, request
from flask_cors import CORS, cross_origin

from flask import Flask
from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId

class ObjectIDConverter(BaseConverter):
    def to_python(self, value):
        try:
            return ObjectId(base64_decode(value))
        except (InvalidId, ValueError, TypeError):
            raise ValidationError()
    def to_url(self, value):
        return base64_encode(value.binary)


# Importando controller de teste
from controllers import tree
from controllers import user
from controllers import insetos
from controllers import fosseis
import json

# Flask app
application = Flask(__name__)
application.url_map.converters['objectid'] = ObjectIDConverter
CORS(application)
# Rota index para teste

"""
----------------------------------------------------
                    TREE
----------------------------------------------------
"""
@application.route("/trees", methods=['POST','GET'])
# Função da rota index
def ctrlTree():
    if (request.method == 'POST'):
        res = tree.createTree(request.json)
        return dumps(res)

    elif (request.method == 'GET'):
        res = tree.listTrees()
        return dumps(res)



@application.route('/tree/<idtree>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdTree(idtree):
    if (request.method == "GET"):
        res = tree.getTree(idtree)
        return dumps(res)

    elif (request.method == 'DELETE'):
        print(idtree)
        res = tree.deleteTree(idtree)
        return dumps(res)

    elif (request.method == 'PUT'):
        res = tree.uploadTree(idtree,request.json)
        return dumps(res)

    elif (request.method == 'PATCH'):

        res = tree.addLoc(idtree, request.json)
        return dumps(res)


"""
----------------------------------------------------
					FOSSEIS
----------------------------------------------------
"""

@application.route("/fosseis", methods=['POST', 'GET'])
def ctrlFossil():
	if (request.method == "POST"):
		res = fosseis.createFosseis(request.json)
		return dumps(res)

	elif (request.method == "GET"):
		res = fosseis.listFosseis()
		return dumps(res)



@application.route('/fossil/<idfossil>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdFossil(idfossil):
    if (request.method == "GET"):
        res = fosseis.getFosseis(idfossil)
        return dumps(res)

    elif (request.method == 'DELETE'):
        print(idfossil)
        res = fosseis.deleteFosseis(idfossil)
        return dumps(res)

    elif (request.method == 'PUT'):
        res = fosseis.uploadFosseis(idfossil,request.json)
        return dumps(res)

    elif (request.method == 'PATCH'):
        res = fosseis.addLoc(idfossil, request.json)
        return dumps(res)


"""
----------------------------------------------------
					INSETO
----------------------------------------------------
"""

@application.route("/insetos", methods=['POST', 'GET'])
def ctrlInseto():
	if (request.method == "POST"):
		res = insetos.createInsetos(request.json)
		return dumps(res)

	elif (request.method == "GET"):
		res = insetos.listInsetos()
		return dumps(res)


@application.route('/inseto/<idinseto>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdInseto(idinseto):
    if (request.method == "GET"):
        res = insetos.getInsetos(idinseto)
        return dumps(res)

    elif (request.method == 'DELETE'):
        print(idinseto)
        res = insetos.deleteInsetos(idinseto)
        return dumps(res)

    elif (request.method == 'PUT'):
        res = insetos.uploadInsetos(idinseto,request.json)
        return dumps(res)

    elif (request.method == 'PATCH'):

        res = insetos.addLoc(idinseto, request.json)
        return dumps(res)



"""
----------------------------------------------------
                    USER
----------------------------------------------------
"""


@application.route("/user", methods=['POST','GET'])
# Função da rota indextree
def ctrlUser():
    if (request.method == 'POST'):
        res = user.createUser(request.json)
        return dumps(res)

    elif (request.method == 'GET'):
        res = user.listUser()
        return dumps(res)


@application.route('/user/<iduser>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdUser(iduser):

    if (request.method == "GET"):
        res = user.getUser(iduser)
        return dumps(res)

    elif (request.method == 'DELETE'):
        print(iduser)
        res = user.deleteUser(iduser)
        return dumps(res)

    elif (request.method == 'PUT'):
        res = user.uploadUser(iduser,request.json)
        return dumps(res)

    elif (request.method == 'PATCH'):
        res = user.patchUser(iduser,request.json)
        return dumps(res)



"""
----------------------------------------------------
                    ACTIVITIES
----------------------------------------------------
"""

@application.route("/activities", methods=['POST','GET', 'DELETE'])
def ctrlAct():
    if (request.method == 'POST'):
        pass  # TODO
    elif (request.method == 'GET'):
        return "This router works :)"
    elif (request.method == 'DELETE'):
        pass #TODO 






    
