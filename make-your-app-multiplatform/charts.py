import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly.offline import plot


# https://insights.stackoverflow.com/survey/2020#technology-developers-primary-operating-systems
dev_stats = [45.8, 27.5, 26.6, .1, 0]
user_stats = [75.6, 16.5, 4.06, 0, 3.89]
labels = ["Windows", "macOS", "Linux-based", "BSD", "Unknown"]

fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=user_stats, name="Desktop Market Share"),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=dev_stats, name="Developers Primary OS"),
              1, 2)

# fig.update_layout(title_text="Operating System Market Share", title_font_size=30)

fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=20)

fig.write_image("images/os_market_share.svg", width=700, height=400)
