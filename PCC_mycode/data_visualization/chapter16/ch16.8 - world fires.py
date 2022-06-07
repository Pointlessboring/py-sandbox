import csv
from matplotlib.pyplot import viridis

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Put headers in list so we can search on them later.
    headers = []      
    for index, column_header in enumerate(header_row):
        headers.append(column_header)

    mags, lons, lats, hover_texts = [], [], [], []

    for row in reader:
        mags.append(row[headers.index('brightness')])
        lons.append(row[headers.index('longitude')])
        lats.append(row[headers.index('latitude')])
        hover_texts.append(row)

# Map the earthquqkes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    # 'text': hover_texts,
    'marker': {
        'size': [(float(mag)/300)*5 for mag in mags],
        'color': 'red',
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'},
    },
}]

print(type(data[0]['marker']['size'][0]))

my_layout = Layout(title='Global Active Fires')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')