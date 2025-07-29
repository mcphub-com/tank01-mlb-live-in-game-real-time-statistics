import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/tank01/api/tank01-mlb-live-in-game-real-time-statistics'

mcp = FastMCP('tank01-mlb-live-in-game-real-time-statistics')

@mcp.tool()
def get_daily_scoreboard_live_real_time(gameID: Annotated[Union[str, None], Field(description='')] = None,
                                        gameDate: Annotated[Union[str, None], Field(description='')] = None,
                                        topPerformers: Annotated[Union[str, None], Field(description='true If the game has started, then this will give you the top performers for the game. If not, then it gives top performers from each team based on season stats.')] = None) -> dict: 
    '''Use this if you want basic game data returned. It's lighter/quicker than getting the full boxscore, for applications that do not need anything but basic data like line score, away/home, etc. /getMLBScoresOnly This can be called using ?gameDate (returns all games for a date, format YYYYMMDD) or ?gameID (returns one game, format YYYYMMDD_AWAY@HOME) Also can be called with topPerformers=true to get a list of stat leaders in each category, per team.'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBScoresOnly'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'gameID': gameID,
        'gameDate': gameDate,
        'topPerformers': topPerformers,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_box_score_live_real_time(gameID: Annotated[Union[str, None], Field(description='')] = None,
                                 playerStatsFormat: Annotated[Union[str, None], Field(description='can be list or map. defaults to map. this determines whether the playerStats element comes back as a list of players or a map with playerID being the key of the key/value pair.')] = None,
                                 startingLineups: Annotated[Union[str, None], Field(description='true for a map of the starters (batters and pitchers) for each team')] = None,
                                 fantasyPoints: Annotated[Union[str, None], Field(description='true will compute fantasy scores for each player, within their playerStats element')] = None,
                                 battingR: Annotated[Union[str, None], Field(description='number, for how many points a batter should receive for each R scored')] = None,
                                 battingTB: Annotated[Union[str, None], Field(description='number, for how many points a batter should receive for total bases')] = None,
                                 battingRBI: Annotated[Union[str, None], Field(description='number, for how many points a batter should receive for each RBI')] = None,
                                 battingBB: Annotated[Union[str, None], Field(description='number, for how many points a batter should receive for each BB')] = None,
                                 battingSO: Annotated[Union[str, None], Field(description='number, for how many points a batter should receive for each strike out')] = None,
                                 baseRunningSB: Annotated[Union[str, None], Field(description='number, for how many points a runner should receive for each stolen base')] = None,
                                 pitchingIP: Annotated[Union[str, None], Field(description='number, for how many points a pitcher should receive for each Inning Pitched')] = None,
                                 pitchingH: Annotated[Union[str, None], Field(description='number, for how many points a pitcher should receive for each hit given up')] = None,
                                 pitchingER: Annotated[Union[str, None], Field(description='number, for how many points a pitcher should receive for each earned run charged')] = None,
                                 pitchingBB: Annotated[Union[str, None], Field(description='number, for how many points a pitcher should receive for each walk given up')] = None,
                                 pitchingSO: Annotated[Union[str, None], Field(description='number, for how many points a pitcher should receive for each strike out thrown')] = None,
                                 pitchingW: Annotated[Union[str, None], Field(description='number, for how many points a pitcher should receive for the win')] = None,
                                 pitchingL: Annotated[Union[str, None], Field(description='number, for how many points a pitcher should receive for the loss')] = None,
                                 pitchingHold: Annotated[Union[str, None], Field(description='number, for how many points a pitcher should receive for a hold')] = None,
                                 pitchingSave: Annotated[Union[str, None], Field(description='number, for how many points a pitcher should receive for the save')] = None) -> dict: 
    '''Retrieves the entire box score for a game either in progress or already completed. The stats retrieved here are what are normally shown in box scores or used in fantasy games. If there are any stats not here that you'd like to see, we can add them. The call looks like this /getMLBBoxScore?gameID=20220409_CHW@DET The call needs to be exactly in the same format as above. 8 digit date, underscore, then the away team abbreviation, @, then home team abbreviation. Complete list of team abbreviations can be retrieved with the getMLBTeams call or various other calls. But, the best way to find specific game ID's are either from the "getMLBGamesForDate" call, or the "getMLBTeamSchedule" call. This will also calculate fantasy points earned for each player for the categories listed in the parameters tab. Enable this with fantasyPoints=true . This will give a "fantasyPointsDefault" element for each player that uses a default scoring method of: Batting: R, BB, RBI, TB 1 point each. Strikeout is -1 pt. Baserunning: SB 1 point. Pitching: 1 pt for strikeout, 3 pts for each Inning Pitched. -1 pt for H, BB, ER. 2 pts for Win, Save, and Hold. -2 pts for a Loss. You can customize all of the points for each parameter. If you do, you'll get a "fantasyPointsCustom" element for each player that calculates your custom scoring system.'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBBoxScore'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'gameID': gameID,
        'playerStatsFormat': playerStatsFormat,
        'startingLineups': startingLineups,
        'fantasyPoints': fantasyPoints,
        'battingR': battingR,
        'battingTB': battingTB,
        'battingRBI': battingRBI,
        'battingBB': battingBB,
        'battingSO': battingSO,
        'baseRunningSB': baseRunningSB,
        'pitchingIP': pitchingIP,
        'pitchingH': pitchingH,
        'pitchingER': pitchingER,
        'pitchingBB': pitchingBB,
        'pitchingSO': pitchingSO,
        'pitchingW': pitchingW,
        'pitchingL': pitchingL,
        'pitchingHold': pitchingHold,
        'pitchingSave': pitchingSave,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_line_score_real_time(gameID: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint provides the basic "line score" for a game, whether completed earlier this season, or currently happening now, in real time. A baseball line score consists of the basic R/H/E, plus the scores by inning and any pitching scoring decisions. Example: /getMLBLineScore?gameID=20220409_CHW@DET ..will return this: ``` { "statusCode":200 "body":"{"decisions": [{"name": "Dylan Cease", "team": "CHW", "decision": "W", "playerID": "28018152299"}, {"name": "Bennett Sousa", "team": "CHW", "decision": "HLD", "playerID": "28208115769"}, {"name": "Jose Ruiz", "team": "CHW", "decision": "HLD", "playerID": "28018056809"}, {"name": "Aaron Bummer", "team": "CHW", "decision": "S", "playerID": "28468725739"}, {"name": "Casey Mize", "team": "DET", "decision": "L", "playerID": "28618589089"}], "awayResult": "W", "gameStatus": "Completed", "homeResult": "L", "away": "CHW", "lineScore": {"away": {"H": "10", "R": "5", "team": "CHW", "scoresByInning": {"1": "2", "2": "0", "3": "0", "4": "0", "5": "0", "6": "2", "7": "1", "8": "0", "9": "0"}, "E": "1"}, "home": {"H": "7", "R": "2", "team": "DET", "scoresByInning": {"1": "0", "2": "0", "3": "0", "4": "0", "5": "0", "6": "2", "7": "0", "8": "0", "9": "0"}, "E": "0"}}, "gameDate": "20220409", "gameID": "20220409_CHW@DET", "home": "DET"}" } ```'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBLineScore'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'gameID': gameID,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_general_game_information(gameID: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This returns very basic information about each game. The some data points that you will get from this call which you won't get from other calls are the time that the game starts, the game ID and link for mlb.com and espn.com, and the game status (Postponed/scheduled/completed/in-progress/etc). All game start times are in Eastern time zone. Example: /getMLBGameInfo?gameID=20220409_CHW@DET will return: ``` { "statusCode":200 "body":"{"espnID": "401354266", "mlbLink": "https://www.mlb.com/gameday/white-sox-vs-tigers/2022/04/09/662864#game_tab=box,game=662864", "gameStatus": "Completed", "season": "2022", "gameDate": "20220409", "gameTime": "1:10p", "away": "CHW", "mlbID": "662864", "gameID": "20220409_CHW@DET", "espnLink": "https://www.espn.com/mlb/boxscore/_/gameId/401354266", "home": "DET"}" } ```'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBGameInfo'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'gameID': gameID,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_daily_schedule(gameDate: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get basic information on which games are being played during a day. Example call: /getMLBGamesForDate?gameDate=20220410 The above call will return all of the games from April 10th, 2022. Date must be in the format YYYYMMDD. Games are returned in a list like shown below: ``` {"statusCode":200 "body":"[{"gameID": "20220410_BAL@TB", "away": "BAL", "gameDate": "20220410", "home": "TB"}, {"gameID": "20220410_TEX@TOR", "away": "TEX", "gameDate": "20220410", "home": "TOR"}, {"gameID": "20220410_SD@ARI", "away": "SD", "gameDate": "20220410", "home": "ARI"}, {"gameID": "20220410_CHW@DET", "away": "CHW", "gameDate": "20220410", "home": "DET"}, {"gameID": "20220410_HOU@LAA", "away": "HOU", "gameDate": "20220410", "home": "LAA"}, {"gameID": "20220410_PIT@STL", "away": "PIT", "gameDate": "20220410", "home": "STL"}, {"gameID": "20220410_BOS@NYY", "away": "BOS", "gameDate": "20220410", "home": "NYY"}, {"gameID": "20220410_NYM@WAS", "away": "NYM", "gameDate": "20220410", "home": "WAS"}, {"gameID": "20220410_MIL@CHC", "away": "MIL", "gameDate": "20220410", "home": "CHC"}, {"gameID": "20220410_LAD@COL", "away": "LAD", "gameDate": "20220410", "home": "COL"}, {"gameID": "20220410_SEA@MIN", "away": "SEA", "gameDate": "20220410", "home": "MIN"}, {"gameID": "20220410_CLE@KC", "away": "CLE", "gameDate": "20220410", "home": "KC"}, {"gameID": "20220410_OAK@PHI", "away": "OAK", "gameDate": "20220410", "home": "PHI"}, {"gameID": "20220410_MIA@SF", "away": "MIA", "gameDate": "20220410", "home": "SF"}, {"gameID": "20220410_CIN@ATL", "away": "CIN", "gameDate": "20220410", "home": "ATL"}]" } ```'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBGamesForDate'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'gameDate': gameDate,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_team_schedule(teamID: Annotated[Union[str, None], Field(description='')] = None,
                      teamAbv: Annotated[Union[str, None], Field(description='')] = None,
                      season: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint returns the full season schedule for any MLB team identified in the parameters. Example: /getMLBTeamSchedule?teamID=6 or /getMLBTeamSchedule?teamAbv=CHW Calling it either way will return the same result, a list of the White Sox games this season, each game in it's own map. If the game has been played, the linescore and game result will be included in the game's map. You can also add the "season" parameter if you want to specify season. Right now we only have seasons 2022, 2023, and 2024. Default season is current season (2024).'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBTeamSchedule'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamID': teamID,
        'teamAbv': teamAbv,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_team_roster(teamID: Annotated[Union[str, None], Field(description='')] = None,
                    teamAbv: Annotated[Union[str, None], Field(description='')] = None,
                    archiveDate: Annotated[Union[str, None], Field(description='')] = None,
                    getStats: Annotated[Union[str, None], Field(description='getStats=true for player stats. Does not work with historical roster call.')] = None,
                    fantasyPoints: Annotated[Union[str, None], Field(description="set to true if you want fantasy points calculated for each player. This only works if you set getStats to true. This will give you a 'fantasyPointsDefault' element within each player's stats element. If you use any of the other parameters below for specific stats, then you'll also get a fantasyPointsCustom element, representing the specific custom scoring system you enter with those variables.")] = None,
                    battingR: Annotated[Union[str, None], Field(description='number, how many points a player should receive for scoring a run')] = None,
                    battingTB: Annotated[Union[str, None], Field(description='number, how many points a player should receive for each base hit')] = None,
                    battingRBI: Annotated[Union[str, None], Field(description='number, how many points a player should receive for each RBI')] = None,
                    battingBB: Annotated[Union[str, None], Field(description='number, how many points a player should receive for each walk')] = None,
                    battingSO: Annotated[Union[str, None], Field(description='number, how many points a player should receive for striking out (usually negative)')] = None,
                    baseRunningSB: Annotated[Union[str, None], Field(description='number, how many points a player should receive for stealing a base')] = None,
                    pitchingIP: Annotated[Union[str, None], Field(description='number, how many points a player should receive for each inning pitched. Usually a multiple of 3.')] = None,
                    pitchingH: Annotated[Union[str, None], Field(description='number, how many points a player should receive for each hit given up')] = None,
                    pitchingER: Annotated[Union[str, None], Field(description='number, how many points a player should receive for each ER charged')] = None,
                    pitchingBB: Annotated[Union[str, None], Field(description='number, how many points a player should receive for each walk given up')] = None,
                    pitchingSO: Annotated[Union[str, None], Field(description='number, how many points a player should receive for each strikeout thrown')] = None,
                    pitchingW: Annotated[Union[str, None], Field(description='number, how many points a player should receive for the win')] = None,
                    pitchingL: Annotated[Union[str, None], Field(description='number, how many points a player should receive for the loss')] = None,
                    pitchingHold: Annotated[Union[str, None], Field(description='number, how many points a player should receive for a hold')] = None,
                    pitchingSave: Annotated[Union[str, None], Field(description='number, how many points a player should receive for the save')] = None) -> dict: 
    '''This call returns the current or historical* roster of any team, using the teamID that can be found in "getMLBTeams" call. Rosters are updated hourly during the day. Historical rosters are saved on a daily basis as of 20230505 and moving forward. Here are examples of the two ways to call and get the White Sox roster: /getMLBTeamRoster?teamID=6 or /getMLBTeamRoster?teamAbv=CHW add getStats=true to get player stats. Add parameter archiveDate to the call to get a list of roster players (playerID's only) for that specific date. Historical roster dates only are kept as far back as 20230505. getStats does not work with the historical Roster'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBTeamRoster'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamID': teamID,
        'teamAbv': teamAbv,
        'archiveDate': archiveDate,
        'getStats': getStats,
        'fantasyPoints': fantasyPoints,
        'battingR': battingR,
        'battingTB': battingTB,
        'battingRBI': battingRBI,
        'battingBB': battingBB,
        'battingSO': battingSO,
        'baseRunningSB': baseRunningSB,
        'pitchingIP': pitchingIP,
        'pitchingH': pitchingH,
        'pitchingER': pitchingER,
        'pitchingBB': pitchingBB,
        'pitchingSO': pitchingSO,
        'pitchingW': pitchingW,
        'pitchingL': pitchingL,
        'pitchingHold': pitchingHold,
        'pitchingSave': pitchingSave,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_teams(teamStats: Annotated[Union[str, None], Field(description='teamStats=true to retrieve Team Level/season long statistics for each team.')] = None,
              topPerformers: Annotated[Union[str, None], Field(description='topPerformers=true to retrieve the best player in each category for each team')] = None,
              rosters: Annotated[Union[str, None], Field(description='rosters=true to pull back team rosters')] = None) -> dict: 
    '''This endpoint provides you with all teams, their cities, names, abbreviations, and some other general information. This endpoint isn't necessary to call very often, as the data here won't change much throughout the season. Perhaps make a point to call it once a week, as we will most likely be adding information to it every once in a while. This does not need parameters. It just returns the same full list every time. Optional parameters are... topPerformers=true This will return the best player for each statistical category on each team. teamStats=true This will return team level/season long stats for each team'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBTeams'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamStats': teamStats,
        'topPerformers': topPerformers,
        'rosters': rosters,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_player_list() -> dict: 
    '''One call grabs the FULL MLB player list. This is mainly used for associating players with their "playerID" which is what you'll want to use when cross referencing with box scores. No parameters, just make the call: /getMLBPlayerLIst'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBPlayerList'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_player_information(playerID: Annotated[Union[str, None], Field(description='')] = None,
                           playerName: Annotated[Union[str, None], Field(description='')] = None,
                           getStats: Annotated[Union[str, None], Field(description='getStats=true will bring back each current season stats for the returned players')] = None,
                           statsSeason: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Call this to get general information on each player (name, team, experience, birthday, college, image link, etc). This can accept either "playerID" or "playerName". If you use playerID then the body will return one object. playerID values can be found from performing a get on the team roster API. playerID is the unique identifier for each player, and is the preferred parameter to use in this call. If you use playerName then it will return a list of objects, since many players can have the same name. It acts as more of a search/scan than direct access, and will be a slower call than if you use playerID. Also, you don't have to call the full name with playerName. You can use partial name. For example, if you call with only playerName=smith then it will return all players with smith in their full name. getStats=true will bring back current season stats for the returned players statsSeason parameter lets you choose a previous season for stats. This goes back to 2023 only. This will be ignored if getStats is not "true". This defaults to current season if empty.'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBPlayerInfo'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerID': playerID,
        'playerName': playerName,
        'getStats': getStats,
        'statsSeason': statsSeason,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_injuries_by_date(injDate: Annotated[Union[str, None], Field(description='Should be a string in format YYYYMMDD. No injuries available before May 7 2025. Will default to current date if not passed in.')] = None,
                         team: Annotated[Union[str, None], Field(description='Will filter by team abbreviation if populated.')] = None) -> dict: 
    '''Gets the injury list for a date in format YYYYMMDD. Can be filtered by team abbreviation. List available on and after 5/7/2025.'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBInjuriesByDate'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'injDate': injDate,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_mlb_betting_odds(gameID: Annotated[Union[str, None], Field(description='')] = None,
                         gameDate: Annotated[Union[str, None], Field(description='')] = None,
                         playerProps: Annotated[Union[str, None], Field(description='')] = None,
                         playerID: Annotated[Union[str, None], Field(description='Allows you to pull back ONLY the player props for one playerID. This essentially is just an advanced filter. gameID or gameDate is required for this option.')] = None,
                         itemFormat: Annotated[Union[str, None], Field(description='this can be \\\\\\\\\\\\\\"list\\\\\\\\\\\\\\" or \\\\\\\\\\\\\\"map\\\\\\\\\\\\\\". Defaults to \\\\\\\\\\\\\\"map\\\\\\\\\\\\\\". Gives games and lines in list format instead of map/dictionary format.')] = None) -> dict: 
    '''This grabs MLB betting/gambling lines and odds from some of the most popular online sportsbooks (fanduel, betrivers, betmgm, caesars, pointsbet, etc). Player prop bets can be added by including playerProps=true parameter. Prop bets are new as of 7/4/2023. Happy 4th! You can call this for specific game or a specific date. Check out the example responses here for the type of data you can expect back. Some of the sportsbooks do not offer live betting, so data from those sportsbooks will not be returned after the game starts. Either gameDate or gameID is required. Examples of what the calls can look like: /getMLBBettingOdds?gameDate=20230410 /getMLBBettingOdds?gameID=20230410_HOU@PIT'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBBettingOdds'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'gameID': gameID,
        'gameDate': gameDate,
        'playerProps': playerProps,
        'playerID': playerID,
        'itemFormat': itemFormat,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def dfssalaries(date: Annotated[Union[str, None], Field(description='format YYYYMMDD')] = None) -> dict: 
    '''Enter the date (YYYYMMDD) and this will return DFS salaries for various DFS sites. Goes back as far as 20250316'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBDFS'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_batting_and_pitching_splits(playerID: Annotated[str, Field(description='')],
                                    splitType: Annotated[str, Field(description='')],
                                    season: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Enter the playerID and splitType of either batting or pitching. Both playerID and splitType are required. season is optional. season defaults to the current season.'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBSplits'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerID': playerID,
        'splitType': splitType,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def depth_charts() -> dict: 
    '''Updated daily, no parameters needed. Returns Depth Charts.'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBDepthCharts'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_adp(adpDate: Annotated[Union[str, None], Field(description='date in the format YYYYMMDD . Goes back as far as 20240924')] = None) -> dict: 
    '''Returns Current ADP in a list. ADPs updated hourly. no required parameters. optional parameter: adpDate: can be a date in format: YYYYMMDD and goes back as far as 20240924'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBADP'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'adpDate': adpDate,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def batter_vs_pitcher(playerID: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Enter a playerID to retrieve a list of players that he's pitched or hit against, and their head to head stats. Providing a pitcher's playerID will retrieve a list of hitters, and providing a hitter's playerID will retrieve a list of pitchers.'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBBatterVsPitcher'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerID': playerID,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_fantasy_stat_projections(projectionType: Annotated[Union[str, None], Field(description='can be 7, 14, or season')] = None,
                                 fantasyPoints: Annotated[Union[str, None], Field(description='set true to pull back a default fantasy point calculation for each projection. adds slightly to the response time.')] = None) -> dict: 
    '''This will retrieve stats projections, regular season only, for 7 days ahead, 14 days ahead, or rest of the regular season. /getMLBProjections. projectionType element is required. options are "season", "7", or "14". /getMLBProjections?projectionType=season /getMLBProjections?projectionType=7 /getMLBProjections?projectionType=14'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBProjections'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'projectionType': projectionType,
        'fantasyPoints': fantasyPoints,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_news_and_headlines(playerID: Annotated[Union[str, None], Field(description='playerID as can be found in many of the endpoints')] = None,
                           teamID: Annotated[Union[str, None], Field(description='Integer of the teamID which can be found in getMLBTeams endpoint')] = None,
                           teamAbv: Annotated[Union[str, None], Field(description="Team's abbreviation which can be found in the /getMLBTeams endpoint")] = None,
                           topNews: Annotated[Union[str, None], Field(description='true')] = None,
                           fantasyNews: Annotated[Union[str, None], Field(description='true')] = None,
                           recentNews: Annotated[Union[str, None], Field(description='true')] = None,
                           maxItems: Annotated[Union[str, None], Field(description='number')] = None) -> dict: 
    '''This endpoint will retrieve relevant news links. /getMLBNews Options: - playerID=xxx Enter a playerID here and get news for that player -teamID = {teamID} -teamAbv= {teamAbv} Enter a teamID or teamAbv to get news for that team, instead of player. - topNews=true Retrieves top news - fantasyNews=true Retrieves top fantasy-relevant news - recentNews=true Retrieves most recent news, whether it's really fantasy relevant or not - maxItems=xx Enter a number there to limit the number of responses you'll receive back. All news will have a "link" and "title" element. Some will have "image" and some will have playerID (single item) or playerIDs (list).'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBNews'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerID': playerID,
        'teamID': teamID,
        'teamAbv': teamAbv,
        'topNews': topNews,
        'fantasyNews': fantasyNews,
        'recentNews': recentNews,
        'maxItems': maxItems,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_mlb_games_and_stats_for_asingle_player(playerID: Annotated[Union[str, None], Field(description='')] = None,
                                               gameID: Annotated[Union[str, None], Field(description='')] = None,
                                               numberOfGames: Annotated[Union[str, None], Field(description='')] = None,
                                               season: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This call will grab a map of all of the games a player has played this season. playerID is a required parameter. You can also use gameID if you want to only pull back a specific game. season is an optional parameter. Currently only 2022, 2023 and 2024 (this season) are available. If you do not include season as a parameter, it will return this season's games. You can limit the amount of games returned with parameter: numberOfGames. For example: &numberOfGames=5 will return the last 5 games this player has an entry for. Example: Correct way to get the stats for Aaron Judge for the season opener against SF on 3/30/2023, would be this: /getMLBGamesForPlayer?playerID=592450&gameID=20230330_SF@NYY But if you wanted to get all of his games this season, you'd make this call /getMLBGamesForPlayer?playerID=592450 This call will not work without playerID. If you want stats for all players during a game, then use the getMLBBoxScore call with that specific gameID.'''
    url = 'https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com/getMLBGamesForPlayer'
    headers = {'x-rapidapi-host': 'tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerID': playerID,
        'gameID': gameID,
        'numberOfGames': numberOfGames,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
