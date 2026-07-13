import streamlit as st
from pathlib import Path
from paths import EPL_LOGO

# ALWAYS execute set_page_config first before any components or markdown loads
st.set_page_config(
    page_title="EPL MatchVision",
    layout="wide",
    # page_icon=r"C:\Projects\football_final\frontend\EPL_logo.png",
    page_icon=str(EPL_LOGO),
    initial_sidebar_state="expanded"
)

# Load the styling sheets dynamically
def load_css():
    css_file = Path(__file__).parent / "style.css"
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

load_css()

# Import pages safely downstream
from homepage import home_page
from model_acc_pg import model_accuracy
from devs_pg import dev_names
from dataset import data_set
from ELO_pg import elo_rating
from about_epl import show_about_page

# Logo and Title Layout Structure
with st.container():
    col1, col2 = st.columns([1, 6])
    with col1:
        # st.image(r"C:\Projects\football_final\frontend\EPL_logo.png", width=110) 
        st.image(str(EPL_LOGO), width=110)
    with col2:
        st.title("EPL MatchVision")

st.markdown("<br>", unsafe_allow_html=True)

home = st.Page(home_page, title="» Score Prediction", default=True)
mod_acc = st.Page(model_accuracy, title="» Model Accuracy")
dev_nm = st.Page(dev_names, title="» Devs")
data = st.Page(data_set, title="» Dataset")
elo_r = st.Page(elo_rating, title="» Team ELO Rating")
elo_r = st.Page(elo_rating, title="» Team ELO Rating")
about = st.Page(show_about_page, title="» About EPL")

pages_dict = {
    "**𝐍𝐀𝐕𝐈𝐆𝐀𝐓𝐈𝐎𝐍 𝐌𝐄𝐍𝐔**": [home, elo_r, mod_acc, about, data, dev_nm]
}

pg = st.navigation(pages_dict, position="sidebar")

pg.run()