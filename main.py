import streamlit as st
from generator import generate_password

st.title("Password Generator")

# Creer des colonnes pour l'affichage du bouton et du mot de passe
col1, col2 = st.columns([4, 1])

# Placeholder pour le mot de passe
with col1:
    password_placeholder = st.empty()

# Bouton pour générer le mot de passe
with col2:
    # Ajout d'un style pour modifier la taille du bouton
    with st.container():
        st.markdown(
            """
            <style>
            .stButton > button {
                width: 100px;
                height: 40px;
                font-size: 24px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.button("♻️", on_click=lambda: password_placeholder.empty())

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

# Générer le mot de passe
password = generate_password(
    length=st.session_state.password_length,
    include_uppercase=include_uppercase,
    include_lowercase=include_lowercase,
    include_numbers=include_numbers,
    include_symbols=include_symbols
)

# Afficher le mot de passe généré
with password_placeholder:
    st.code(password, language='plaintext')