import streamlit as st
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium
from streamlit_folium import st_folium

df_airports = pd.read_csv("airports.csv")
# keep only French airports
df_airports = df_airports[df_airports["country"] == "France"]
# Create the geodataframe for airports:
gdf_airports = gpd.GeoDataFrame(
    df_airports,
    geometry=[Point(xy) for xy in zip(df_airports.lon, df_airports.lat)],
    crs="EPSG:4326",
)

# Create a special dataframe to display listof airports as a table:
df_airports_display = df_airports[["name", "iata", "icao", "country", "alt"]]

df_airports_display.set_index("name", inplace=True)
st.header("Airports of France with Folium Maps on Streamlit")

st.dataframe(df_airports_display.style.hide(axis="index"))


m_draw: folium.Map = folium.Map(location=[46.7111, 1.7191], zoom_start=5)
for i, row in gdf_airports.iterrows():
    folium.Marker(location=[row["lat"], row["lon"]], tooltip=row["name"]).add_to(m_draw)

output: st_folium(m_draw, width=700, height=500)
