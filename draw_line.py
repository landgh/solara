import pandas as pd
import solara
import plotly.express as px

import debugpy
debugpy.listen(('localhost', 9223))
print("Waiting for debugger attach...")
debugpy.wait_for_client()

def get_data():
    df = pd.DataFrame({'x': range(10), 'y': [i*2 for i in range(10)]})
    return df

@solara.component
def Page():
    solara.Markdown("# Draw a line chart")
    fig = px.line(get_data(), x = 'x', y = 'y', title='simple line chart', labels={'x': 'x-axis', 'y': 'y-axis'})
    solara.FigurePlotly(fig)

@solara.component
def Page2():
    solara.Markdown("# Draw a line chart from page2")
    fig = px.line(get_data(), x = 'x', y = 'y', title='simple line chart', labels={'x': 'x-axis', 'y': 'y-axis'})
    solara.FigurePlotly(fig)
