from google.appengine.ext import db

class VeiculoModel (db.Model):
	timestamp = db.DateTimeProperty(auto_now=True)
	modelo = db.StringProperty()
	fabricante = db.StringProperty()
	ano_fabricacao = db.StringProperty()
	ano_modelo = db.StringProperty()
	cor = db.StringProperty()
	user_name = db.StringProperty()

class CadastroModel (db.Model):
	name = db.StringProperty()