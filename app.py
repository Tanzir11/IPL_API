from flask import Flask, jsonify, request
import ipl
import utils

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)


# post: When we try send data i.e hidden from the url we use post. It's primarily used with sensitive information
# get: When we try to send data through url for that we use get method


@app.route('/api/teamvteam')
def teamvteam():
    # Below is how we input the parameters inside the api we use "?" to provide the key we are accepting and then "=" the value corresponding to that key
    # http://127.0.0.1:5000/api/teamvteam?team1=Rajasthan%20Royals&team2=Royal Challengers Bangalore
    # To test out the api in post man we will have to provide the api end point then go inside params and provide keys name along with the values
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    response = ipl.teamVteamAPI(team1,team2)
    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    # http://127.0.0.1:5000/api/team-record?team=Kolkata Knight Riders
    team_name = request.args.get("team")
    data = utils.teamAPI(team_name)
    return data

@app.route('/api/batting-record')
def batting_record():
    # http://127.0.0.1:5000/api/batting-record?batsman=HH Pandya
    batsman_name = request.args.get("batsman")
    data = utils.batsmanAPI(batsman_name)
    return data

@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = utils.batsmanAPI(batsman_name)
    return response

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = utils.bowlerAPI(bowler_name)
    return response

app.run(debug=True)

