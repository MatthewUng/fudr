from bokeh.charts import Donut
from bokeh.embed import components
import pandas as pd
from app import db
from app.models import Group, Restaurant

def create_chart(group):
    names = []
    counts = []
    for r in group.restaurants:
        names.append(r.name)
        counts.append(r.count)
    print(names)
    print(counts)
    data = pd.Series(counts, index=names)
    chart = Donut(data)
    return components(chart)
