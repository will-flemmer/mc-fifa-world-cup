
from mc_fifa_worldcup.mc_simulation import MCSimulation

def get_top_8_teams():
  pass

if __name__ == "__main__":
  NUM_SIMULATION = 10
  top_8_teams = get_top_8_teams()
  
  MCSimulation(top_8_teams, NUM_SIMULATION)