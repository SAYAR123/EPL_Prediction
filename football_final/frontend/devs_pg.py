import streamlit as st
from ui import hero, match_info

def dev_names():
    hero(
        "Meet the Developers",
        "Developed as a Machine Learning project for EPL match prediction."
    )
    
    match_info("⚡ Built with Python, Streamlit, Scikit-Learn, XGBoost, and MLP architectures.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("• **[Sawmik Pal](https://github.com/SawmikPal)**\n\n• **[Sarthak Mukherjee](https://github.com/GoldenHeart2000)**\n\n• **[Sayar Sekhar Ghosh](https://github.com/SAYAR123)**")
        
    with col2:
        st.markdown("• **[Pramiti Ghosh](https://github.com/PRAMITI-GHOSH)**\n\n• **[Soumik Mandal](https://github.com/Rony0387)**")