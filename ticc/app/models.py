"""
Definition of models.
"""

from django.db import models
from ticc.settings import DBNAME
from mongoengine import *

connect(DBNAME)

class Cidade(EmbeddedDocument):
	nome = StringField(max_length = 40, required=True)

class Localizacao(EmbeddedDocument):
	cidade = StringField(max_length = 40, required=True)
	estado = StringField(max_length = 2, required=True)

class Estado(Document):
	nome = StringField(max_length = 20, required=True)
	sigla = StringField(max_length = 2, required=True)
	cidades = EmbeddedDocumentField(Cidade)

class Usuario(Document):
	nome = StringField(max_length = 50, required=True)
	email = StringField(regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", max_length = 50, required=True, unique=True)
	cpf = IntField(required=True, unique_with='email')
	cidade = EmbeddedDocumentField(Localizacao)