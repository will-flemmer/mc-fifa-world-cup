import random
from typing import List

from mc_fifa_worldcup.team import Team
from mc_fifa_worldcup.tournament import Tournament


class MCSimulation:
  def __init__(self, team_names: List[str], num_iterations):
    self.teams = [Team(name) for name in team_names]
    self.num_iterations = num_iterations

  def __simulate_single_tournament(self, iteration):
    if iteration % 100 == 0:
      print(f"Tourname Sim No. {iteration}")
    random.shuffle(self)
    tournament = Tournament(self.teams)
    winner = tournament.simulate()
    return winner
  
  def simulate_multiple_tournaments(self):
    winners = [self.__simulate_single_tournament(i) for i in range(self.num_iterations)]
    print(winners)

    