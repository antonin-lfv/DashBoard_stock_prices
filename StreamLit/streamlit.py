from datetime import date
import datetime
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import pandas as pd
import numpy as np
from fastdist import fastdist
import random as rd
from sklearn.datasets import make_blobs


st.set_page_config(layout="wide", )
# streamlit run StreamLit/streamlit.py
st.markdown("""
<style>
.first_titre {
    font-size:40px !important;
    font-weight: bold;
    box-sizing: border-box;
    text-align: center;
    width: 100%;
    border: solid #008000 4px;
    padding: 4px;
}
.intro{
    text-align: justify;
    font-size:20px !important;
}
.grand_titre {
    font-size:30px !important;
    font-weight: bold;
    text-decoration: underline;
    text-decoration-color: #2782CD;
    text-decoration-thickness: 5px;
}
.section{
    font-size:20px !important;
    font-weight: bold;
    text-decoration: underline;
    text-decoration-color: #258813;
    text-decoration-thickness: 3px;
}
.petite_section{
    font-size:16px !important;
    font-weight: bold;
}
.caract{
    font-size:11px !important;
}
</style>
""", unsafe_allow_html=True)

# Pages
PAGES = ["Accueil", "DashBoard StockPrices", "Simulation épidémie"]
st.sidebar.title('Mes projets :bulb:')
choix_page = st.sidebar.selectbox(label="Choisissez un projet", options=PAGES)

if choix_page=="Accueil":
    st.markdown('<p class="first_titre">Bienvenue sur mon site Streamlit</p>', unsafe_allow_html=True)
    st.write("##")
    st.write("Ici vous retrouverez les Dashboards liés à mes projets disponibles sur mon site web https://antonin-lfv.github.io/. ")

if choix_page=="DashBoard StockPrices":

    st.markdown('<p class="first_titre">DashBoard StockPrices</p>', unsafe_allow_html=True)
    st.write('##')
    st.sidebar.write('---')
    st.sidebar.title('Options du projet  :control_knobs:')
    st.sidebar.write('##')
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
        'Apple':AAPL,
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
    fenetre = st.sidebar.slider('Saisir une fenêtre (jours)', min_value=2,max_value=268, value=50)
    st.subheader('Cours des actions de '+slider_1+', '+slider_2+', '+slider_3+', '+slider_4+' sur une fenêtre de '+str(fenetre)+' jours\n')
    ###############################################################

    vert = '#599673'
    rouge = '#e95142'

    fig = make_subplots(rows=4, cols=2,
                        specs=[[{'type': 'xy'},{'type':'indicator'}] for i in range (4)],
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

    # Rectangle des i (fenetre) derniers jours + moyenne

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
        width=1600, height=1000,
        margin=dict(l=40, r=500, b=40, t=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_showticklabels=True,
        xaxis2_showticklabels = True,
        xaxis3_showticklabels=True,
    )

    st.plotly_chart(fig)

if choix_page=="Simulation épidémie":
    st.markdown('<p class="first_titre">Simulation épidémiologique</p>', unsafe_allow_html=True)
    st.write('##')
    st.sidebar.write('---')
    st.sidebar.title('Options du projet  :control_knobs:')
    st.sidebar.write('##')


    def distance_e(x, y):  # distance entre 2 points du plan cartésien
        return fastdist.euclidean(np.array(x), np.array(y))


    def remove_(a, l):  # enlever les éléments de l dans a
        for i in range(len(l)):
            a.remove(l[i])
        return a


    def chance_infecte(p):  # return True si il devient infecté avec une proba p
        return rd.randint(0, 100) < int(p * 100)


    def immuniser(l, l2, p):  # l: infectés; l2: immunisés précédents
        drop = 0
        for i in range(len(l)):
            if rd.randint(0, 100) < int(p * 100):
                l2.append(l[i - drop])
                l.remove(l[i - drop])
                drop += 1
        return l, l2


    def deces(l, l2, l3, p):  # l: infectés; l2: décès précédents; l3: immunisés
        l_p = l[:]  # création d'une copie pour éviter d'erreur d'indice
        for i in range(len(l_p)):
            if rd.randint(0, 100) < int(p * 100) and not any(list == l_p[i] for list in l3):
                l2.append(l_p[i])
                l.remove(l_p[i])
        return l, l2


    global list

    with st.sidebar.form(key='Parametres de la simulation'):
        nb_individu = st.slider(label="Nombre d'individus", min_value=10, max_value=2500, value=1000)
        variance_pop = st.slider(label="Éloignement des individus", min_value=0.4, max_value=10., step=0.2, value=1.)
        rayon_contamination = st.slider(label="Rayon de contamination", min_value=0.3, max_value=5.9, step=0.2, value=0.5)
        infectiosite = st.slider(label="Taux d'infection", min_value=0., max_value=1., value=0.1, step=0.05)
        p = st.slider(label="Taux de guérison", min_value=0., max_value=1., value=0.1, step=0.05)
        d = st.slider(label="Taux de décès", min_value=0., max_value=1., value=0.05, step=0.05)
        submit_button = st.form_submit_button(label='Lancer la simulation')

    st.sidebar.subheader("La simulation prend quelques secondes à s'éxecuter")

    # création des figures
    fig = make_subplots(rows=2, cols=2, column_widths=[0.8, 0.2], row_heights=[0.5, 0.5],
                        subplot_titles=["population", "", ""],
                        specs=[[{'type': 'xy'}, {'type': 'domain'}], [{'type': 'xy', 'colspan': 2}, None]],
                        horizontal_spacing=0.05, vertical_spacing=0.05)

    # dataset
    x, y = make_blobs(n_samples=nb_individu, centers=1, cluster_std=variance_pop)
    df = pd.DataFrame(dict(x=x[:, 0],
                           y=x[:, 1]))

    # création des courbes finales et listes des coordonnées
    data = dict(courbe_sains=[], courbe_infectes=[], courbe_immunises=[], courbe_deces=[], courbe_removed=[],
                coord_infectes=[], coord_sains=[], coord_immunises=[], coord_deces=[])

    numero_infecte_1 = rd.randint(0, nb_individu - 1)  # on choisit le premier individu infecté au hasard
    coord_1er_infecte = [df['x'][numero_infecte_1], df['y'][numero_infecte_1]]  # coordonnées du 1er infecté

    # Remplissage des listes

    for k in range(nb_individu):
        if k == numero_infecte_1:
            data['coord_infectes'].append(coord_1er_infecte)
        else:
            data['coord_sains'].append([df['x'][k], df['y'][k]])

    data['courbe_sains'].append(nb_individu - 1)
    data['courbe_infectes'].append(1)
    data['courbe_immunises'].append(0)
    data['courbe_deces'].append(0)
    data['courbe_removed'].append(0)

    # Jours 2 à n

    while len(data['coord_infectes']) > 0.08 * nb_individu or len(data['courbe_sains']) < 10:  # condition d'arrêt

        for k in range(len(data['coord_infectes'])):
            non_sains = 0
            for j in range(len(data['coord_sains'])):
                if distance_e(data['coord_infectes'][k],
                              data['coord_sains'][j - non_sains]) < rayon_contamination and not any(
                        list == data['coord_sains'][j - non_sains] for list in
                        data['coord_infectes']) and chance_infecte(infectiosite):
                    buf = data['coord_sains'][j - non_sains]
                    data['coord_infectes'].append(buf)
                    data['coord_sains'].remove(buf)
                    non_sains += 1

        coord_infectes1, data['coord_immunises'] = immuniser(data['coord_infectes'], data['coord_immunises'], p)
        data['coord_infectes'], data['coord_deces'] = deces(coord_infectes1, data['coord_deces'],
                                                            data['coord_immunises'], d)

        # pour les courbes finales
        data['courbe_sains'].append(len(data['coord_sains']))
        data['courbe_infectes'].append(len(data['coord_infectes']))
        data['courbe_immunises'].append(len(data['coord_immunises']))
        data['courbe_deces'].append(len(data['coord_deces']))
        data['courbe_removed'].append(len(data['coord_immunises']) + len(data['coord_deces']))

    if data['coord_sains']:
        fig.add_trace(
            go.Scatter(x=np.array(data['coord_sains'])[:, 0], y=np.array(data['coord_sains'])[:, 1], name="sain",
                       mode="markers",
                       marker=dict(
                           color='#636EFA',
                           size=5,
                           line=dict(
                               width=0.4,
                               color='#636EFA')
                       ), marker_line=dict(width=1), showlegend=False), 1, 1)
    if data['coord_infectes']:
        fig.add_trace(go.Scatter(x=np.array(data['coord_infectes'])[:, 0], y=np.array(data['coord_infectes'])[:, 1],
                                 name="infecté", mode="markers",
                                 marker=dict(
                                     color='#EF553B',
                                     size=5,
                                     line=dict(
                                         width=0.4,
                                         color='#EF553B')
                                 ), marker_line=dict(width=1), showlegend=False), 1, 1)
    if data['coord_immunises']:
        fig.add_trace(
            go.Scatter(x=np.array(data['coord_immunises'])[:, 0], y=np.array(data['coord_immunises'])[:, 1],
                       name='immunisé', mode="markers",
                       marker=dict(
                           color='#00CC96',
                           size=5,
                           line=dict(
                               width=0.4,
                               color='#00CC96')
                       ), marker_line=dict(width=1), showlegend=False), 1, 1)
    if data['coord_deces']:
        fig.add_trace(
            go.Scatter(x=np.array(data['coord_deces'])[:, 0], y=np.array(data['coord_deces'])[:, 1], name="décédé",
                       mode="markers",
                       marker=dict(
                           color='#AB63FA',
                           size=5,
                           line=dict(
                               width=0.4,
                               color='#AB63FA')
                       ), marker_line=dict(width=1), showlegend=False), 1, 1)
    fig.update_traces(hoverinfo="name")
    fig.update_xaxes(showgrid=False, visible=False, row=1, col=1)
    fig.update_yaxes(showgrid=False, visible=False, row=1, col=1)
    labels = ["sains", "infectés", "immunisés", "décédés"]
    fig.add_trace(go.Pie(
        values=[len(data['coord_sains']), len(data['coord_infectes']), len(data['coord_immunises']),
                len(data['coord_deces'])], labels=labels, sort=False), 1, 2)

    x_courbe = list(np.arange(0, len(data['courbe_sains'])))
    fig.add_trace(
        go.Scatter(x=x_courbe, y=data['courbe_sains'], marker=dict(color='#636EFA'), marker_line=dict(width=2),
                   showlegend=False, name="sains", yaxis="y", ), 2, 1)
    fig.add_trace(
        go.Scatter(x=x_courbe, y=data['courbe_infectes'], marker=dict(color='#EF553B'), marker_line=dict(width=1),
                   showlegend=False, name="infectés", yaxis="y2", ), 2, 1)
    fig.add_trace(
        go.Scatter(x=x_courbe, y=data['courbe_immunises'], marker=dict(color='#00CC96'), marker_line=dict(width=1),
                   showlegend=False, name="immunisés", yaxis="y3", ), 2, 1)
    fig.add_trace(
        go.Scatter(x=x_courbe, y=data['courbe_deces'], marker=dict(color='#AB63FA'), marker_line=dict(width=1),
                   showlegend=False, name="décédés", yaxis="y4", ), 2, 1)
    fig.add_trace(
        go.Scatter(x=x_courbe, y=data['courbe_removed'], marker=dict(color='#000000'), marker_line=dict(width=1),
                   showlegend=False, name="removed", yaxis="y5", ), 2, 1)
    fig.update_xaxes(title_text="jours", row=2, col=1)
    fig.update_yaxes(title_text="nombre d'individus", row=2, col=1)
    fig.add_annotation(text="Maximum d'infectés", x=data['courbe_infectes'].index(max(data['courbe_infectes'])),
                       # ajouter un texte avec une flèche
                       y=max(data['courbe_infectes']) + 0.03 * nb_individu, arrowhead=1, showarrow=True, row=2,
                       col=1)
    fig.update_traces(
        hoverinfo="name+x+y",
        line={"width": 1.3},
        marker={"size": 2},
        mode="lines+markers",
        showlegend=False, row=2, col=1)

    fig.update_layout(hovermode="x")
    fig.update_layout(
        template='simple_white',
        font=dict(size=10),
        autosize=False,
        width=1600, height=1000,
        margin=dict(l=40, r=500, b=40, t=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig)

