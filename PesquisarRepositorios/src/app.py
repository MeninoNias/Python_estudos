from PesquisarRepositorios.src.model.buscarRepositorios import BuscarRepositorios
from util import imprime_repositorios


busca = BuscarRepositorios('tertri', 'js')

repositorios = busca.request_api()['items']

print(busca.request_api()['total_count'])
imprime_repositorios(repositorios)
print(len(repositorios))