import pandas as pd

df = pd.read_csv('footprint.csv')

# Filter out countries with no data
east_african_countries = ['Kenya', 'Uganda', 'Tanzania', 'Rwanda']
df = df[df['Country/region'].isin(east_african_countries)]

df.to_csv('east_africa_footprint.csv', index=False)

