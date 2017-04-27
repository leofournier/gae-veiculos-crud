import unittest
from google.appengine.api import users

class TesteVeiculo(unittest.TestCase):

    def TestaUsuarioLogado(self):
        self.assertNotEqual(users.get_current_user().email(), '')

    def TestaUsuarioNaoLogado(self):
        self.assertEqual(users.get_current_user().email(), '')

suite = unittest.TestLoader().loadTestsFromTestCase(TesteVeiculo)
unittest.TextTestRunner(verbosity=2).run(suite)