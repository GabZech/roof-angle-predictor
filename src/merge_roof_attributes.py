import pandas as pd

# import both datasets
df_roof = pd.read_csv("./ignore/hamburg_roofCalc_DBexport.csv")
df_base = pd.read_csv("./ignore/hamburg_data_raw.csv")

df_merged = pd.merge(df_base, 
                     df_roof, 
                     how = "left", 
                     left_on = "",
                     right_on = ""
                     )

