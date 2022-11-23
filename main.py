from nba_api.stats.endpoints import playercareerstats
import json, numpy, requests, pandas
from flask import Flask
from flask_cors import CORS

#import ast

#giannis
career = playercareerstats.PlayerCareerStats(player_id='203507')

#print(career.get_data_frames()[0])

print(career.get_json())

# dictionary
player_dictionary = (career.get_dict())
#player_year1  = player_dictionary



pd2 = player_dictionary['resultSets']
current_stats = pd2[1]


header_row = str(pd2[1]['headers'])
results_row = str(pd2[1]['rowSet'])



app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
	return str(pd2[1])


@app.route('/table')
def table():
	return str(pd2[1])


	

app.run(host='0.0.0.0', port=81)
