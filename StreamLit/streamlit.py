from datetime import date
import datetime
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

with open("/Users/antoninlefevre/Downloads/langages_informatiques/Python/Blog - MachineLearnia/Blog_site/StreamLit/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# À SAISIR :
###############################################################
start = "2020-05-25" # début des graphiques                   #
fenetre = 87  # jours pris en comptent à partir d'aujourd'hui#
###############################################################
# STREAMLIT :
###############################################################
st.title("Cours des actions de Apple, Microsoft, Intel et Tesla - fenêtre de {} jours\n".format(fenetre))
###############################################################



today = date.today()+ datetime.timedelta(days=1)
d1 = today.strftime("%Y-%m-%d")
current_year, current_month, current_day= today.strftime("%Y"), today.strftime("%m"), today.strftime("%d")

AAPL = yf.download("AAPL", start=start, end="{}".format(d1))
AAPL['Date']=AAPL.index
MSFT = yf.download("MSFT", start=start, end="{}".format(d1))
MSFT['Date']=MSFT.index
INTC = yf.download("INTC", start=start, end="{}".format(d1))
INTC['Date']=INTC.index
TSLA = yf.download("TSLA", start=start, end="{}".format(d1))
TSLA['Date']=TSLA.index

vert = '#599673'
rouge = '#e95142'

fig = make_subplots(rows=4, cols=2,
                    specs=[[{'type': 'xy'},{'type':'indicator'}],
                           [{'type':'xy'},{'type':'indicator'}],
                           [{'type':'xy'},{'type':'indicator'}],
                           [{'type':'xy'},{'type':'indicator'}]],
                    column_widths=[0.85, 0.15],
                    shared_xaxes=True,
                    subplot_titles=['APPLE', '', 'Microsoft', '','INTEL', '','Tesla',''])

# courbes #####################

def couleur(df):
    if df['Close'].iloc[-1*fenetre]-df['Close'].iloc[-1] < 0 :
        return vert
    else : return rouge


fig.add_trace(go.Scatter(
    y = AAPL['Close'],
    x = AAPL['Date'],
    line=dict(color=couleur(AAPL), width=1),
    name="",
    hovertemplate=
    "Date: %{x}<br>" +
    "Close: %{y}<br>"+
    "Volume: %{text}<br>",
    text = AAPL.Volume,
), row=1, col=1)

fig.add_trace(go.Scatter(
    y = MSFT['Close'],
    x = MSFT['Date'],
    line=dict(color=couleur(MSFT), width=1),
    name="",
    hovertemplate=
    "Date: %{x}<br>" +
    "Close: %{y}<br>"+
    "Volume: %{text}<br>",
    text = MSFT.Volume,
), row=2, col=1)

fig.add_trace(go.Scatter(
    y = INTC['Close'],
    x = INTC['Date'],
    line=dict(color=couleur(INTC), width=1),
    name="",
    hovertemplate=
    "Date: %{x}<br>" +
    "Close: %{y}<br>"+
    "Volume: %{text}<br>",
    text = INTC.Volume,
), row=3, col=1)


fig.add_trace(go.Scatter(
    y = TSLA['Close'],
    x = TSLA['Date'],
    line=dict(color=couleur(TSLA), width=1),
    name="",
    hovertemplate=
    "Date: %{x}<br>" +
    "Close: %{y}<br>"+
    "Volume: %{text}<br>",
    text = TSLA.Volume,
), row=4, col=1)


fig.add_hline(y=AAPL['Close'].iloc[0],
              line_dash="dot",
              annotation_text="{}".format(AAPL['Date'][0].date()),
              annotation_position="bottom left",
              line_width=2, line=dict(color='black'),
              annotation=dict(font_size=10),
              row=1, col=1)
fig.add_hline(y=MSFT['Close'].iloc[0],
              line_dash="dot",
              annotation_text="{}".format(MSFT['Date'][0].date()),
              annotation_position="bottom left",
              line_width=2, line=dict(color='black'),
              annotation=dict(font_size=10),
              row=2, col=1)
fig.add_hline(y=INTC['Close'].iloc[0],
              line_dash="dot",
              annotation_text="{}".format(INTC['Date'][0].date()),
              annotation_position="bottom left",
              line_width=2, line=dict(color='black'),
              annotation=dict(font_size=10),
              row=3, col=1)
fig.add_hline(y=TSLA['Close'].iloc[0],
              line_dash="dot",
              annotation_text="{}".format(TSLA['Date'][0].date()),
              annotation_position="bottom left",
              line_width=2, line=dict(color='black'),
              annotation=dict(font_size=10),
              row=4, col=1)

# Indicateurs #####################

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = round(AAPL['Close'].iloc[-1],4),
    number={'prefix': "$", 'font_size' : 40},
    delta = {"reference": AAPL['Close'].iloc[-1*fenetre], "valueformat": ".6f", "position" : "bottom", "relative":False},
    title = {"text": "Apple Since {}-days".format(fenetre)},
    domain = {'y': [0.5, 0.7], 'x': [0.55, 0.75]}),
row=1, col=2)

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = round(MSFT['Close'].iloc[-1],4),
    number={'prefix': "$", 'font_size' : 40},
    delta = {"reference": MSFT['Close'].iloc[-1*fenetre], "valueformat": ".6f", "position" : "bottom", "relative":False},
    title = {"text": "Microsoft Since {}-days".format(fenetre)},
    domain = {'y': [0.5, 0.7], 'x': [0.55, 0.75]}),
row=2, col=2)

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = round(INTC['Close'].iloc[-1],4),
    number={'prefix': "$", 'font_size' : 40},
    delta = {"reference": INTC['Close'].iloc[-1*fenetre], "valueformat": ".6f", "position" : "bottom", "relative":False},
    title = {"text": "Intel Since {}-days".format(fenetre)},
    domain = {'y': [0.5, 0.7], 'x': [0.55, 0.75]}),
row=3, col=2)

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = round(TSLA['Close'].iloc[-1],4),
    number={'prefix': "$", 'font_size' : 40},
    delta = {"reference": TSLA['Close'].iloc[-1*fenetre], "valueformat": ".6f", "position" : "bottom", "relative":False},
    title = {"text": "Tesla Since {}-days".format(fenetre)},
    domain = {'y': [0.5, 0.7], 'x': [0.55, 0.75]}),
    row=4, col=2)

# Rectangle des i (fenetre) derniers jours

if fenetre > 1 :
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=AAPL['Date'].iloc[-1*fenetre].date().strftime('%Y-%m-%d'), y0=AAPL['Close'].min(),
                  x1=d1, y1=AAPL['Close'].max(),
                  fillcolor=couleur(AAPL),
                  row=1, col=1
                  )
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=MSFT['Date'].iloc[-1*fenetre].date().strftime('%Y-%m-%d'), y0=MSFT['Close'].min(),
                  x1=d1, y1=MSFT['Close'].max(),
                  fillcolor=couleur(MSFT),
                  row=2, col=1
                  )
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=INTC['Date'].iloc[-1*fenetre].date().strftime('%Y-%m-%d'), y0=INTC['Close'].min(),
                  x1=d1, y1=INTC['Close'].max(),
                  fillcolor=couleur(INTC),
                  row=3, col=1
                  )
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=TSLA['Date'].iloc[-1*fenetre].date().strftime('%Y-%m-%d'), y0=TSLA['Close'].min(),
                  x1=d1, y1=TSLA['Close'].max(),
                  fillcolor=couleur(TSLA),
                  row=4, col=1
                  )

# layout #############

fig.update_layout(
    template='simple_white',
    showlegend=False,
    font=dict(size=10),
    autosize=False,
    width=1500, height=1000,
    margin=dict(l=40, r=800, b=40, t=40),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig)

