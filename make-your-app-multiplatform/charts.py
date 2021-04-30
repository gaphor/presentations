import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly.offline import plot


# https://gs.statcounter.com/os-market-share/desktop/worldwide/#monthly-202003-202103
user_stats = [75.6, 16.5, 4.06, 3.89]
# https://insights.stackoverflow.com/survey/2020#technology-developers-primary-operating-systems
dev_stats = [45.8, 27.5, 26.6, 0]
labels = ["Windows", "macOS", "Linux-based", "Unknown"]

fig = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "domain"}, {"type": "domain"}]],
    subplot_titles=["Desktop Market Share", "Developer's Primary OS"],
)
fig.add_trace(go.Pie(labels=labels, values=user_stats, name="overall market"), 1, 1)
fig.add_trace(go.Pie(labels=labels, values=dev_stats, name="developer market"), 1, 2)
fig.add_annotation(
    x=0,
    y=-0.1,
    text="https://gs.statcounter.com/os-market-share/desktop/",
    showarrow=False,
    font=dict(size=8),
)
fig.add_annotation(
    x=1,
    y=-0.1,
    text="https://insights.stackoverflow.com/survey/2020",
    showarrow=False,
    font=dict(size=8),
)

fig.update_traces(textposition="inside", textinfo="percent+label")

fig.write_image("images/os_market_share.svg", width=700, height=400)
