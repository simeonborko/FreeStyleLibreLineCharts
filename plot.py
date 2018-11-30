from typing import List

import plotly.graph_objs as go
from datetime import datetime
from plotly.offline import plot


def get_div(historic: (List[datetime], List[float]), scan: (List[datetime], List[float])):

    data = [
        go.Scatter(
            x=historic[0],
            y=historic[1],
            mode='lines+markers',
            name='Historic Glucose',
            line=dict(
                shape='spline'
            )
        ),
        go.Scatter(
            x=scan[0],
            y=scan[1],
            mode='markers',
            name='Scan Glucose'
        ),
    ]

    return plot(data, include_plotlyjs='cdn', output_type='div')
