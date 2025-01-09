from utils.url_resolver import UrlResolver as Url


class GamesEndpoints():

    __HOST = Url.resolve()
    get_games_list = f"{__HOST}/games"
