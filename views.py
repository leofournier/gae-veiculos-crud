#Collection of handlers which is to process route request from main.py

import webapp2
import cgi
import jinja2
import os

from datetime import datetime
from logics import Veiculo
from google.appengine.ext import db
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

jinja_environment.globals['year'] = datetime.now().year

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            veic = Veiculo() 
            template_values = {'veiculo' : veic.listar_veiculo()}
            template = jinja_environment.get_template('template/index.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def post(self):
        user = users.get_current_user()
        if user:
            if self.request.POST.get('delete'): #if user clicks "Delete" button
                veiculo_ids = self.request.get('veiculo_id',allow_multiple=True) #allow_multiple=True so that it reads multiple key into list.
                veic = Veiculo()
                veic.excluir_veiculo(veiculo_ids)
                self.redirect('/')
        else:
            self.redirect(users.create_login_url(self.request.uri))

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template = jinja_environment.get_template('template/create.html')
            self.response.out.write(template.render())
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        #get all input values
        input_modelo = self.request.get('modelo').strip()
        input_fabricante = self.request.get('fabricante').strip()
        input_ano_fabricacao = self.request.get('ano_fabricacao').strip()
        input_ano_modelo = self.request.get('ano_modelo').strip()
        input_cor = self.request.get('cor').strip()
        
        veic = Veiculo()
        veic.salvar_veiculo(input_modelo,input_fabricante,input_ano_fabricacao,input_ano_modelo,input_cor,0)
        self.redirect('/create')


class EditHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        if user:
            veic_k = db.Key.from_path('CadastroModel','LFournier','VeiculoModel',long(self.request.get('id')))
            veic = db.get(veic_k)

            template_values = {'veiculo' : veic}
            template = jinja_environment.get_template('template/edit.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        input_id = self.request.get('id')
        input_modelo = self.request.get('modelo').strip()
        input_fabricante = self.request.get('fabricante').strip()
        input_ano_fabricacao = self.request.get('ano_fabricacao').strip()
        input_ano_modelo = self.request.get('ano_modelo').strip()
        input_cor = self.request.get('cor').strip()

        veic = Veiculo()
        veic.salvar_veiculo (input_modelo,input_fabricante,input_ano_fabricacao,input_ano_modelo,input_cor,long(input_id))
        self.redirect('/')