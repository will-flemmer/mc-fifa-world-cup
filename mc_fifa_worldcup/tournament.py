from typing import List
import random

from mc_fifa_worldcup.match import Match
from mc_fifa_worldcup.team import Team


class Tournament:
  def __init__(self, teams: List[Team]):
    self.quarter_final_contestants = teams
    self.semi_final_contestants = []
    self.final_contestants = []

  def simulate(self):
    self.__simulate_quarters()
    self.__simulate_semis()
    return self.__simulate_final()

  def __simulate_quarters(self):
    matches = self.__build_match_ups(self.quarter_final_contestants)
    self.semi_final_contestants = [m.simulate() for m in matches]
    # for match in matches:
    #   winning_team = match.simulate()
    #   self.semi_final_contestants.append(winning_team)

  def __simulate_semis(self):
    matches = self.__build_match_ups(self.semi_final_contestants)
    self.final_contestants = [m.simulate() for m in matches]
    # for match in matches:
    #   winning_team = match.simulate()
    #   self.semi_final_contestants.append(winning_team)

  def __simulate_final(self):
    match = Match(self.semi_final_contestants[0], self.semi_final_contestants[1])
    winner = match.simulate()
    print(f"The winner is {winner}")

  def __build_match_ups(self, team_list) -> List[Match]:
    random.shuffle(team_list)
    match_count = len(team_list) / 2
    matches = []

    for match_number in range(match_count - 1):
      match = self.__create_match(team_list[match_number], team_list[match_number + 1])
      matches.append(match)

    return match
    

  def __create_match(self, team_a, team_b) -> Match:
    return Match(team_a, team_b)