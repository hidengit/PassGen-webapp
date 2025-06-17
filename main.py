import streamlit as st

st.title("Password Generator")

# Initialiser les variables de session si elles n'existent pas
if "password_length" not in st.session_state:
    st.session_state.password_length = 16
if "num_input" not in st.session_state:
    st.session_state.num_input = 16

# Mettre à jour le slider
def update_slider():
    st.session_state.password_length = st.session_state.num_input

# Mettre à jour le number_input
def update_number_input():
    st.session_state.num_input = st.session_state.password_length

# Créer des colonnes pour l'affichage
col1, col2, col3 = st.columns([1,3,1])

# Entrées pour la longueur du mot de passe
with col1:
    st.number_input("Password Length", min_value=8, max_value=32, key="num_input", on_change=update_slider, step=1)

# Slider pour la longueur du mot de passe
with col2:
    st.slider("", min_value=8, max_value=32, key="password_length", on_change=update_number_input)

# Options pour les caractères du mot de passe
with col3:
    include_uppercase = st.checkbox("Uppercase", value=True)
    include_lowercase = st.checkbox("Lowercase", value=True)
    include_numbers = st.checkbox("Numbers", value=True)
    include_symbols = st.checkbox("Symbols", value=True)