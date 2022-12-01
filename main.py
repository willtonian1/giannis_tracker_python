from nba_api.stats.endpoints import playercareerstats
import json, numpy, requests, pandas
from flask import Flask
from flask_cors import CORS

import modules.recent as r
#import ast

#giannis
career = playercareerstats.PlayerCareerStats(player_id='203507')

# dictionary
player_dictionary = (career.get_dict())


pd2 = player_dictionary['resultSets']  #getting stats stuff

header_row = str(pd2[1]['headers'])  #headers only


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
	return str(pd2[1])


@app.route('/table')
def table():

	pd2 = player_dictionary['resultSets']

	
	results_row = (pd2[1]['rowSet'])


	print(results_row[0][1])
	#results_row2 = results_row.pop(results_row[0][1])

	results_row2 = results_row[0]

	return str(results_row2)


app.run(host='0.0.0.0', port=81)
