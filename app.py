import pandas as pd
import streamlit as st


read_and_cache_csv = st.cache(pd.read_csv)


data = read_and_cache_csv("https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2018.csv")

out_df = data.groupby('passer_player_name').filter(lambda x: len(x) >= 20)
out_df['success'] = out_df.epa >0

out_df = out_df.groupby('passer_player_name')[['epa','success']].mean()


st.write(data.columns)
