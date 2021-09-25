<p align="center">
	<img src="https://user-images.githubusercontent.com/63207451/120532141-a814f080-c3df-11eb-9aac-f342eaf20a44.png" height="80">
	<p/>

<h1 align="center">Cours de la bourse en temps réel</h1>

<br/>

<p align="center">
  <a href="https://share.streamlit.io/antonin-lfv/dashboard_stock_prices/main/StreamLit/streamlit.py"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"/></a>
  </p>
     
<p align="center">
   Ce projet conciste en la création d'un dashboard qui récupère en temps réel les cours des actions de différentes entreprises et devises. On peut empiler 4 courbes à la fois sur 4 lignes, et selectionner une fenêtre pour savoir si sur cette période le cours a diminué ou non, et de combien.
	Pour lancer le script il faut taper dans le cmd <b>'streamlit run path_file/streamlit.py'</b>. <br/>
     <p/>
     
<br/>

> Ce projet est apparu dans les [recommandations de la semaine](https://discuss.streamlit.io/t/weekly-roundup-dbt-dashboards-instagram-profile-analyzers-medium-stats-and-more/14081) le 23 juin 2021.
     
<br/>

L'app est réalisée avec StreamLit et Plotly :

<br/>
<br/>

<img width="1440" alt="Capture d’écran 2021-06-02 à 12 00 01" src="https://user-images.githubusercontent.com/63207451/120461182-13d46a80-c39a-11eb-98d1-b24a046b590b.png">

<br/>

Pour accéder au DashBoard c'est ici -> [DashBoard](https://share.streamlit.io/antonin-lfv/app_stock_prices/main/StreamLit/streamlit.py)

<br/>

# Configuration

<br/>

Le fichier __config.toml__ du dossier __.streamlit__ contient les éléments du thème de l'application telles que la couleur du fond, et la couleur des boutons. <br/>
exemple :
```txt
[theme]
backgroundColor="#FFF"
font="sans serif"
```

<br/>

Le fichier __requirements.txt__ contient les packages python non natif, tel que Plotly. <br/>
exemple :
```txt
yfinance
plotly
sklearn
```

<br/>

Pour mettre en ligne le dashboard il faut mettre tous ces fichiers dans un repo GitHub public, et avoir un compte validé sur [streamlit](https://streamlit.io). A partir de là la configuration est faite automatiquement :

![Capture d’écran 2021-06-02 à 20 13 44](https://user-images.githubusercontent.com/63207451/120531546-09888f80-c3df-11eb-81a8-93883337b424.png)

<br/>

<p align="center">
	  <a href="https://antonin-lfv.github.io" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/127334786-f48498e4-7aa1-4fbd-b7b4-cd78b43972b8.png" title="Web Page" width="38" height="38"></a>
  <a href="https://github.com/antonin-lfv" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97302854-e484da80-1859-11eb-9374-5b319ca51197.png" title="GitHub" width="40" height="40"></a>
  <a href="https://www.linkedin.com/in/antonin-lefevre-565b8b141" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303444-b2c04380-185a-11eb-8cfc-864c33a64e4b.png" title="LinkedIn" width="40" height="40"></a>
  <a href="mailto:antoninlefevre45@icloud.com" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303543-cec3e500-185a-11eb-8adc-c1364e2054a9.png" title="Mail" width="40" height="40"></a>
</p>

<br/>

-----------------------------
