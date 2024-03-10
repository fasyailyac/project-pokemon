from .resources.signin.login import PokemonLogin
def initialize_routes(api):
    api.add_resource(PokemonLogin, '/pokemon-login')