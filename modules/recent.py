message = "hello"

from nba_api.stats.endpoints import leagueleaders
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import playergamelog

player_info = leagueleaders.LeagueLeaders()
player_gamelog = playergamelog.PlayerGameLog(player_id=203507)


def get_scoreboard():

	# Today's Score Board
	games = scoreboard.ScoreBoard()

	# json
	games.get_json()

	# dictionary
	e = games.get_dict()
	return print(e)


def get_league_leaders():
	return print(player_info.get_json())


def get_gamelog():

	a = player_gamelog.get_dict()
	b = a['resultSets']
	c = b[0]['rowSet']
	d= c[0]
	return str(d)


if __name__ == "main":
	print("Hi")
