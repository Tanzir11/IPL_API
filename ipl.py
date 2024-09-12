import pandas as pd
import numpy as np
import json

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

# print(matches.head())

def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches["Team2"])))
    team_dict = {
        "teams":teams
    }
    return team_dict

def teamVteamAPI(team1,team2):
    valid_teams = list(set(list(matches['Team1']) + list(matches["Team2"])))
    if team1 in valid_teams and team2 in valid_teams:
        temp_df = matches[((matches["Team1"] == team1) & (matches["Team2"] == team2)) | 
                          ((matches["Team1"] == team2) & (matches["Team2"] == team1))]
        total_matches = temp_df.shape[0]
        matches_won_team_1 = temp_df["WinningTeam"].value_counts()[team1]
        matches_won_team_2 = temp_df["WinningTeam"].value_counts()[team2]
        draws = total_matches-(matches_won_team_1+matches_won_team_2)
        response = {"Total_Matches": str(total_matches),
                    team1:str(matches_won_team_1),
                    team2: str(matches_won_team_2),
                    "Draw":str(draws),
                    }
    else:
        response = {"Error":"Wrong team name"}
    return response