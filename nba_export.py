import pandas as pd
from nba_api.stats.endpoints import playercareerstats, teamgamelogs
from nba_api.live.nba.endpoints import scoreboard

OUT = "/mnt/c/Users/Jeqap/Files/BarryO/PowerBI"

regular = pd.read_csv('https://test.researchdata.tuwien.ac.at/files/ymgzs-z3s43/regular_train.csv')
regular.to_csv(f"{OUT}/historical_regular.csv", index=False)

playoffs = pd.read_csv('https://test.researchdata.tuwien.ac.at/files/ymgzs-z3s43/playoff_train.csv')
playoffs.to_csv(f"{OUT}/historical_playoffs.csv", index=False)

games = scoreboard.ScoreBoard()
pd.DataFrame(games.get_dict()['scoreboard']['games']).to_csv(f"{OUT}/live_scoreboard.csv", index=False)

print("Done. CSVs saved.")
