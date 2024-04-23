import os
import re
import pandas as pd

# Saves a DF like the one below to the file `aggregate.csv`
#      | Argentinata |   France   |
# 2023 | <position>  | <position> |
# 2024 | <position>  | <position> |

def reshape_df(df):
    df.set_index("Team", inplace=True)
    df_t = df.T
    df_t.index.names = ['Year']
    return df_t.rename(index={"Position": year})


if __name__ == "__main__":
  files = os.listdir("data")
  df_list = []
  for file_name in files:
    if file_name == "aggregate.csv":
       continue
    
    year = re.findall(r'\d+', file_name)[0]
    df = pd.read_csv(f"data/{file_name}")[["Position", "Team"]]

    reshaped_df = reshape_df(df)
    df_list.append(reshaped_df)
  
  agg_df = pd.concat(df_list)
  agg_df.fillna(999, inplace=True)
  agg_df.to_csv("data/aggregate.csv")
  print(agg_df)