import dash_core_components as dcc
import plotly.graph_objects as go

x = ['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2, 5, 1, 9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder': 'array', 'categoryarray': ['d', 'a', 'c', 'b']})

bar_chart = dcc.Graph(id="bar-chart-graph", figure=fig)
