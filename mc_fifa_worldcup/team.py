import numpy as np

class Team:
  def __init__(self, name):
    self.name = name

  def calculate_stength_stats(self):
    avg_finish_position = self.__calculate_avg_finish_position()
    finish_position_std = self.__calculate_std_of_strength()
    self.strength = np.random.normal(
      avg_finish_position, 2 * finish_position_std
    )

  def __calculate_avg_finish_position(self, matches_df):
    return 1
  
  def __calculate_std_of_strength(self, matches_df):
    return 1
