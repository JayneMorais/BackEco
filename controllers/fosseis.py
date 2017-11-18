#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

bdfosseis = mongoOP.OpMongoDB('forestbd','fosseis')

def createFosseis( dados):
    return bdfosseis.save(dados)

def uploadFosseis(id,dados):
    return bdfosseis.upload(id, dados)

def deleteFosseis(id):
    return bdfosseis.remove(id)
    
def listFosseis():
    return bdfosseis.list()
    
def getFosseis(id):
    return bdfosseis.findById(id)

def addLoc(id, dados):
    return bdfosseis.patch(id, dados)