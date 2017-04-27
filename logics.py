from models import VeiculoModel, CadastroModel
from google.appengine.ext import db
from google.appengine.api import users

class Veiculo(object):
	def salvar_veiculo (self,modelo,fabricante,ano_fabricacao,ano_modelo,cor,id):
		if id>0:
			veic_k = db.Key.from_path('CadastroModel','LFournier','VeiculoModel',long(id))
			veic = db.get(veic_k)
		else:
			cad = CadastroModel(key_name='LFournier',name='LFournier Engenharia')
			cad.put()
			veic = VeiculoModel(parent = cad)

		veic.modelo = modelo
		veic.fabricante = fabricante
		veic.ano_fabricacao = ano_fabricacao
		veic.ano_modelo = ano_modelo
		veic.cor = cor
		veic.user_name = users.get_current_user().email()
		veic.put()

	def excluir_veiculo (self, veiculos_ids):
		if len(veiculos_ids)>0:
			for veiculo_id in veiculos_ids:
				veic_k = db.Key.from_path('CadastroModel','LFournier','VeiculoModel',long(veiculo_id))
				veic = db.get(veic_k)
				db.delete(veic_k)

	def listar_veiculo (self):
		cad = db.Key.from_path('CadastroModel','LFournier')
		veiculo_query = VeiculoModel.all()
		veiculo_query.ancestor(cad)
		return veiculo_query