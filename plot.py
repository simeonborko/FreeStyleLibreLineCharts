from typing import List

import plotly.graph_objs as go
from datetime import datetime
from plotly.offline import plot


def plot_it(data):
    plot_config = [
        go.Scatter(
            x=data["historic"]["x"],
            y=data["historic"]["y"],
            mode="lines+markers",
            name="Historic Glucose",
            line=dict(shape="spline"),
        ),
        go.Scatter(
            x=data["scan"]["x"],
            y=data["scan"]["y"],
            mode="markers",
            name="Scan Glucose",
        ),
    ]

    for type_ in ["no food", "insulin_short", "insulin_long"]:
        if not data.get(type_):
            continue

        plot_config.append(
            go.Scatter(
                x=data[type_]["x"],
                y=data[type_]["y"],
                mode="markers",
                name=type_,
            ),
        )

    return plot(plot_config, include_plotlyjs="cdn", output_type="div")
