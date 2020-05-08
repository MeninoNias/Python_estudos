from ListarRepositorios.src.model.api_github import ListaDeRepositorios


user_name = 'MeninoNias'

repositorios = ListaDeRepositorios(user_name)
repositorios.imprime_repositorios()