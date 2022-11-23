message = "hello"

from nba_api.stats.static import teams

def get_recent_game():
	print(teams.find_team_by_abbreviation('MIL'))
	
if __name__ == "main":
	print("Hi")