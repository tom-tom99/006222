import streamlit as st
import streamlit.components.v1 as com
import time

# Mesurer le temps de début
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

com.html(""" <html>
  <head>
<style>
.animated_rainbow_2 {
    font-size = 42px;
    font-family: cursive;
    text-align :left;
    padding:1px;
    height: 100px;
    -webkit-animation: animatedBackground_b 3s linear infinite alternate;
}

@keyframes animatedBackground_b{
    0% {color: #ff8b00;}
    10% {color: #e8ff00}
    20% {color: #5dff00}
    30% {color: #00ff2e}
    40% {color: #00ffb9}
    50% {color: #00b9ff}
    60% {color: #002eff}
    70% {color: #5d00ff}
    80% {color: #e800ff}
    90% {color: #ff008b}
    100% {color: #ff0000}
}
</style>
  </head>
  
   <p class="animated_rainbow_2"> <font size =10> Bon anniversaire Laurelia   &#128512</font></p>
   <title> this is a title </title>
</body> 
</html>
""")

# Calculer le temps écoulé
elapsed_time = time.time() - st.session_state.start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

# Afficher le timer
st.write(f"⏰ Temps écoulé: {minutes:02d}:{seconds:02d}")

# Barre de progression
progress = elapsed_time / 300
st.progress(min(progress, 1.0))
# Faire des ballons seulement si moins de 5 minutes
if elapsed_time < 300:  # 300 secondes = 5 minutes
    st.balloons()
    # Ajouter un délai avant de redémarrer
    time.sleep(2)  # 2 secondes de délai
    st.rerun()  # Redémarrer pour continuer les ballons
else:
    st.success("🎉 Temps écoulé ! Bon anniversaire Laurelia ! 🎂")
    st.balloons()  # Un dernier set de ballons
    st.snow()  # Ajouter un effet de neige pour célébrer !