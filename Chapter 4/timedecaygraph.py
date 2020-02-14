# Shows different formula for time decay for use in a game
# The first uses a linear decay which results in a fast decay
# The Improved version uses a formula giving a decay that slows down over time
# This is based on the formula f(x) = x / x + h
# To run first install plotly using:
# pip3 install plotly

import plotly
from plotly import tools
import plotly.graph_objs as go

num_plots = 50
start_value = 10

x_axis= list(range(1,num_plots))

y_axis_linear = list()
for i in range (1,num_plots):
    y_axis_linear.append(start_value + 0.9 - (0.2*i))


linear = go.Scatter(
    x = x_axis,
    y = y_axis_linear,
    name = "Linear"
)


y_axis_new = list()
for i in range (1,num_plots):
    y_axis_new.append(start_value + 1.5 - (start_value * (i/ (i + 10))))


# Function is x / x + h
# function that tends towards, but never reaches 1
# h determines how quickly reach the half way point
# multiple it by the maximum we want to decrement our time by
new = go.Scatter(
    x = x_axis,
    y = y_axis_new,
    name = "Improved"
)

data = [linear, new]

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Different timers")
    }, auto_open=True)
