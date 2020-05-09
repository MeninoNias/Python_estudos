

def imprime_repositorios(repositorios):
    dados_api = repositorios
    if type(dados_api) is not int:
        for i in range(len(dados_api)):
            print(dados_api[i]['full_name'])
    else:
        print(dados_api)