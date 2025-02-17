import plotly.graph_objects as go
import numpy as np

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

ax = 10 * np.outer(np.cos(u), np.sin(v))
ay = 10 * np.outer(np.sin(u), np.sin(v))
az = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

fig = go.Figure(data = [go.Surface(x = ax, y = ay, z = az)])

fig.update_layout(title = dict(text = 'Sphere'), autosize = False,
                  width = 500, height = 500,
                  margin = dict(l=65, r=50, b=65, t=90))
fig.show()