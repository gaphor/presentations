import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly.offline import plot


# https://insights.stackoverflow.com/survey/2020#technology-developers-primary-operating-systems
so_percentages = [45.8, 27.5, 26.6, .1]
operating_systems = ["Windows", "macOS", "Linux-based", "BSD"]

user_stats = [75.6, 16.5, 4.06, 3.89]
operating_systems = ["Windows", "macOS", "Linux-based", "Unknown"]
fig = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "pie"}, {"type": "pie"}]],
    subplot_titles=("Desktop OS Share", "Developers' Primary OS")
)
fig.add_trace(go.Pie(
    values=user_stats,
    labels=operating_systems,
    name="Desktop Market Share"),
    row=1, col=1)
fig.add_trace(go.Pie(
    values=so_percentages,
    labels=operating_systems,
    name="Developers' Primary Operating Systems"),
    row=1, col=2)

fig.update_layout(title_text="Operating System Market Share", title_font_size=30)

fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=20)

fig.write_image("images/os_market_share.svg")

