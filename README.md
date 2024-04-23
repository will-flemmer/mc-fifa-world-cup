# Problem Breakdown
**Predict which team is going to win the world cup**

## Assumptions
- For simplicity, we assume that the top 8 teams from the previous world cup make it to the quarter finals. This is where the simulation starts
- Matchups are randomly generated, including matchups in the semi finals

### Predict the outcome of a game
Which ever team has greater "strength" will win.

#### Modelling Strength of a Team
strength = avg_finish_position + random(-1 -> 1) * 2 * std_of_finish_position