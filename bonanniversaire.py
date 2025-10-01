import streamlit as st
import streamlit.components.v1 as com
import time

# Mesurer le temps de début
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Calculer le temps écoulé
elapsed_time = time.time() - st.session_state.start_time
minutes = int(elapsed_time // 60)

# Changer l'émoji selon le temps (plus de variété)
time_segments = [
    (30, "🥳"),      # 0-30s : Ballon
    (60, "🎂"),      # 30-60s : Gâteau
    (90, "🎁"),      # 1-1.5min : Cadeau
    (120, "✨"),     # 1.5-2min : Étincelles
    (150, "❤️"),     # 2-2.5min : Cœur
    (180, "🌟"),     # 2.5-3min : Étoile brillante
    (210, "🥂"),     # 3-3.5min : Verre à champagne
    (240, "🎊"),     # 3.5-4min : Confetti
    (270, "🦄"),     # 4-4.5min : Licorne
    (300, "🎉"),     # 4.5-5min : Confetti
    (float('inf'), "🥳")  # 5min+ : Tête qui fête
]

emoji = "🎈"  # Par défaut
for time_limit, e in time_segments:
    if elapsed_time < time_limit:
        emoji = e
        break

com.html(f""" <html>
  <head>
<style>
.animated_rainbow_2 {{
    font-size = 42px;
    font-family: cursive;
    text-align :left;
    padding:1px;
    height: 100px;
    -webkit-animation: animatedBackground_b 3s linear infinite alternate;
}}

@keyframes animatedBackground_b{{
    0% {{color: #ff8b00;}}
    10% {{color: #e8ff00}}
    20% {{color: #5dff00}}
    30% {{color: #00ff2e}}
    40% {{color: #00ffb9}}
    50% {{color: #00b9ff}}
    60% {{color: #002eff}}
    70% {{color: #5d00ff}}
    80% {{color: #e800ff}}
    90% {{color: #ff008b}}
    100% {{color: #ff0000}}
}}
</style>
  </head>
  
   <p class="animated_rainbow_2"> <font size =10> Bon anniversaire Laurelia {emoji}</font></p>
   <title> this is a title </title>
</body> 
</html>
""")

# Afficher le timer
st.write(f"⏰ Temps écoulé: {minutes:02d}:{int(elapsed_time % 60):02d} - Émoji: {emoji}")

# Barre de progression
progress = elapsed_time / 300
st.progress(min(progress, 1.0))

# Faire des ballons seulement si moins de 5 minutes
if elapsed_time < 300:
    st.balloons()
    time.sleep(2)
    st.rerun()
else:
    st.success("🎉 Temps écoulé ! Bon anniversaire Laurelia ! 🎂")
    st.balloons()
    st.snow()