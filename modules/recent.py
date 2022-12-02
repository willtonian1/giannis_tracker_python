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
	return print(player_gamelog.get_data_frames())
	
if __name__ == "main":
	print("Hi")