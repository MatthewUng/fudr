from bokeh.charts import Donut
from bokeh.embed import components
import pandas as pd

def create_chart(group):
    names = []
    counts = []
    for r in group.restaurants:
        if r.count > 0:
            names.append(r.name)
            counts.append(r.count)
    if len(names) == 0:
        return "", ""
    data = pd.Series(counts, index=names)
    chart = Donut(data)
    return components(chart)
