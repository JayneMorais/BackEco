#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

bdinsetos = mongoOP.OpMongoDB('forestbd','insetos')

def createInsetos( dados):
    return bdinsetos.save(dados)

def uploadInsetos(id,dados):
    return bdinsetos.upload(id, dados)

def deleteInsetos(id):
    return bdinsetos.remove(id)
    
def listInsetos():
    return bdinsetos.list()
    
def getInsetos(id):
    return bdinsetos.findById(id)

def addLoc(id, dados):
    return bdinsetos.patch(id, dados)