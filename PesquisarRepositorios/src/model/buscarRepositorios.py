import requests, json
from util import imprime_repositorios

class BuscarRepositorios():

    def __init__(self, searsh, league):
        self.searsh = searsh
        self.league = league

    def request_api(self):
        resposta = requests.get(
            f' https://api.github.com/search/repositories?q={self.searsh}+language:{self.league}&sort=stars&order=desc')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code


