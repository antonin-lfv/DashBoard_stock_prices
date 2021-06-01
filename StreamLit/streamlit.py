from datetime import date
import datetime
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# streamlit run StreamLit/streamlit.py

# À SAISIR :
###############################################################
start = "2020-05-25" # début des graphiques                   #
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
GOLD = yf.download("GC=F", start=start, end="{}".format(d1))
GOLD['Date']=GOLD.index
GOOG = yf.download("GOOG", start=start, end="{}".format(d1))
GOOG['Date']=GOOG.index
NTDOY = yf.download("NTDOY", start=start, end="{}".format(d1))
NTDOY['Date']=NTDOY.index

SP = {
    'Apple': AAPL,
    'Microsoft':MSFT,
    'Intel':INTC,
    'Tesla':TSLA,
    'Gold':GOLD,
    'Google':GOOG,
    'Nintendo':NTDOY,
}

# STREAMLIT :
###############################################################
# selectbox à gauche :
slider_1 = st.sidebar.selectbox(
    'Choisissez un 1er cours',
    ('Apple', 'Microsoft', 'Intel', 'Tesla', 'Gold', 'Google', 'Nintendo'),
)

slider_2 = st.sidebar.selectbox(
    'Choisissez un 2e cours',
    ('Microsoft', 'Apple', 'Intel', 'Tesla', 'Gold', 'Google', 'Nintendo')
)

slider_3 = st.sidebar.selectbox(
    'Choisissez un 3er cours',
    ('Intel', 'Apple', 'Microsoft', 'Tesla', 'Gold', 'Google', 'Nintendo')
)

slider_4 = st.sidebar.selectbox(
    'Choisissez un 4e cours',
    ('Tesla', 'Apple', 'Microsoft', 'Intel', 'Gold', 'Google', 'Nintendo')
)

df1 = SP[slider_1]
df2 = SP[slider_2]
df3 = SP[slider_3]
df4 = SP[slider_4]

# choix fenetre
fenetre = st.sidebar.slider('Saisir une fenêtre (jours)', min_value=0,max_value=len(df1['Close']), value=50)


st.title('Cours des actions de '+slider_1+', '+slider_2+', '+slider_3+', '+slider_4+' sur une fenêtre de '+str(fenetre)+' jours\n')
###############################################################


vert = '#599673'
rouge = '#e95142'

fig = make_subplots(rows=4, cols=2,
                    specs=[[{'type': 'xy'},{'type':'indicator'}],
                           [{'type':'xy'},{'type':'indicator'}],
                           [{'type':'xy'},{'type':'indicator'}],
                           [{'type':'xy'},{'type':'indicator'}]],
                    column_widths=[0.85, 0.15],
                    shared_xaxes=True,
                    subplot_titles=[slider_1, '', slider_2, '',slider_3, '',slider_4,''])

# courbes #####################

def couleur(df):
    if df['Close'].iloc[-1*fenetre]-df['Close'].iloc[-1] < 0 :
        return vert
    else : return rouge

fig.add_trace(go.Scatter(
    y = df1['Close'],
    x = df1['Date'],
    line=dict(color=couleur(df1), width=1),
    name="",
    hovertemplate=
    "Date: %{x}<br>" +
    "Close: %{y}<br>"+
    "Volume: %{text}<br>",
    text = df1.Volume,
), row=1, col=1)

fig.add_trace(go.Scatter(
    y = df2['Close'],
    x = df2['Date'],
    line=dict(color=couleur(df2), width=1),
    name="",
    hovertemplate=
    "Date: %{x}<br>" +
    "Close: %{y}<br>"+
    "Volume: %{text}<br>",
    text = df2.Volume,
), row=2, col=1)

fig.add_trace(go.Scatter(
    y = df3['Close'],
    x = df3['Date'],
    line=dict(color=couleur(df3), width=1),
    name="",
    hovertemplate=
    "Date: %{x}<br>" +
    "Close: %{y}<br>"+
    "Volume: %{text}<br>",
    text = df3.Volume,
), row=3, col=1)


fig.add_trace(go.Scatter(
    y = df4['Close'],
    x = df4['Date'],
    line=dict(color=couleur(df4), width=1),
    name="",
    hovertemplate=
    "Date: %{x}<br>" +
    "Close: %{y}<br>"+
    "Volume: %{text}<br>",
    text = df4.Volume,
), row=4, col=1)


fig.add_hline(y=df1['Close'].iloc[0],
              line_dash="dot",
              annotation_text="{}".format(df1['Date'][0].date()),
              annotation_position="bottom left",
              line_width=2, line=dict(color='black'),
              annotation=dict(font_size=10),
              row=1, col=1)
fig.add_hline(y=df2['Close'].iloc[0],
              line_dash="dot",
              annotation_text="{}".format(df2['Date'][0].date()),
              annotation_position="bottom left",
              line_width=2, line=dict(color='black'),
              annotation=dict(font_size=10),
              row=2, col=1)
fig.add_hline(y=df3['Close'].iloc[0],
              line_dash="dot",
              annotation_text="{}".format(df3['Date'][0].date()),
              annotation_position="bottom left",
              line_width=2, line=dict(color='black'),
              annotation=dict(font_size=10),
              row=3, col=1)
fig.add_hline(y=df4['Close'].iloc[0],
              line_dash="dot",
              annotation_text="{}".format(df4['Date'][0].date()),
              annotation_position="bottom left",
              line_width=2, line=dict(color='black'),
              annotation=dict(font_size=10),
              row=4, col=1)

# Indicateurs #####################

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = round(df1['Close'].iloc[-1],4),
    number={'prefix': "$", 'font_size' : 40},
    delta = {"reference": df1['Close'].iloc[-1*fenetre], "valueformat": ".6f", "position" : "bottom", "relative":False},
    title = {"text": slider_1+" Since {}-days".format(fenetre)},
    domain = {'y': [0.5, 0.7], 'x': [0.55, 0.75]}),
row=1, col=2)

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = round(df2['Close'].iloc[-1],4),
    number={'prefix': "$", 'font_size' : 40},
    delta = {"reference": df2['Close'].iloc[-1*fenetre], "valueformat": ".6f", "position" : "bottom", "relative":False},
    title = {"text": slider_2+" Since {}-days".format(fenetre)},
    domain = {'y': [0.5, 0.7], 'x': [0.55, 0.75]}),
row=2, col=2)

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = round(df3['Close'].iloc[-1],4),
    number={'prefix': "$", 'font_size' : 40},
    delta = {"reference": df3['Close'].iloc[-1*fenetre], "valueformat": ".6f", "position" : "bottom", "relative":False},
    title = {"text": slider_3+" Since {}-days".format(fenetre)},
    domain = {'y': [0.5, 0.7], 'x': [0.55, 0.75]}),
row=3, col=2)

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = round(df4['Close'].iloc[-1],4),
    number={'prefix': "$", 'font_size' : 40},
    delta = {"reference": df4['Close'].iloc[-1*fenetre], "valueformat": ".6f", "position" : "bottom", "relative":False},
    title = {"text": slider_4+" Since {}-days".format(fenetre)},
    domain = {'y': [0.5, 0.7], 'x': [0.55, 0.75]}),
    row=4, col=2)

# Rectangle des i (fenetre) derniers jours

if fenetre > 1 :
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=df1['Date'].iloc[-1*fenetre].date().strftime('%Y-%m-%d'), y0=df1['Close'].min(),
                  x1=d1, y1=df1['Close'].max(),
                  fillcolor=couleur(df1),
                  row=1, col=1
                  )
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=df2['Date'].iloc[-1*fenetre].date().strftime('%Y-%m-%d'), y0=df2['Close'].min(),
                  x1=d1, y1=df2['Close'].max(),
                  fillcolor=couleur(df2),
                  row=2, col=1
                  )
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=df3['Date'].iloc[-1*fenetre].date().strftime('%Y-%m-%d'), y0=df3['Close'].min(),
                  x1=d1, y1=df3['Close'].max(),
                  fillcolor=couleur(df3),
                  row=3, col=1
                  )
    fig.add_shape(type="rect",
                  xref="x", yref="y",
                  x0=df4['Date'].iloc[-1*fenetre].date().strftime('%Y-%m-%d'), y0=df4['Close'].min(),
                  x1=d1, y1=df4['Close'].max(),
                  fillcolor=couleur(df4),
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
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_showticklabels=True,
    xaxis2_showticklabels = True,
    xaxis3_showticklabels=True,
)

st.plotly_chart(fig)

