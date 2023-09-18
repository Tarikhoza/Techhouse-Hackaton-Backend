from plotly.subplots import make_subplots
import plotly.graph_objects as go
from skimage import io
import os


def plot(filepath):
    img = io.imread(filepath)
    path = os.path.normpath(filepath)
    fig = make_subplots()
    fig.add_trace(go.Image(z=img))
    fig.write_html("static/plots/"+path.split(os.sep)[-1]+".html")
