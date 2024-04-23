import random
import pandas as pd

from mc_fifa_worldcup.team import Team

class Match:
  def __init__(self, team_a: Team, team_b: Team, df: pd.DataFrame):
    self.team_a = team_a
    self.team_b = team_b
    self.df = df
    
  def simulate(self):
    self.team_a.calculate_stength_stats()
    self.team_b.calculate_stength_stats()

    return self.winning_team()
  
  def winning_team(self):
    if self.team_a.strength > self.team_b:
      return self.team_a
    elif self.team_a.strength < self.team_b:
      return self.team_b
    else:
      return random.choice([self.team_a, self.team_b])