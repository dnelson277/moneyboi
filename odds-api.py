import requests
import json

MARKETS = 'totals'
ODDS_FORMAT = 'american'
DATE_FORMAT = 'iso'
REGIONS = 'us'
API_KEY = 'f35f162d5439e776172c2cb8e53f2068'
SPORT = 'basketball_nba'

odds_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds', 
    params={
        'api_key': API_KEY,
        'regions': REGIONS,
        'markets': MARKETS,
        'oddsFormat': ODDS_FORMAT,
        'dateFormat': DATE_FORMAT,
    }
)

if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

else:
    odds_json = odds_response.json()
    print('Number of events:', len(odds_json))
    print(odds_json)
    

    # Check the usage quota
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])