#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

bdhistorias = mongoOP.OpMongoDB('forestbd','historias')

def createHistorias( dados):
    return bdhistorias.save(dados)

def uploadHistorias(id,dados):
    return bdhistorias.upload(id, dados)

def deleteHistorias(id):
    return bdhistorias.remove(id)
    
def listHistorias():
    return bdhistorias.list()
    
def getHistorias(id):
    return bdhistorias.findById(id)

def addLoc(id, dados):
    return bdhistorias.patch(id, dados)