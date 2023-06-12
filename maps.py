import folium
import pandas as pd

eco_footprint = pd.read_csv('east_africa_footprint.csv')

political_countries_url = (
    'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson'
)

m = folium.Map(
    location=[30, 10],
    zoom_start=3,
    tiles='cartodbpositron'
    )

folium.Choropleth(
    geo_data=political_countries_url,
    name='choropleth',
    data=eco_footprint,
    columns=["Country/region", "Ecological footprint"],
    key_on='feature.properties.name',
    fill_color="RdYlGn_r",
    fill_opacity=0.8,
    line_opacity=0.3,
    nan_fill_color="white",
    legend_name='Countries we are working in',
    highlight=True
).add_to(m)

m.save('index.html')

