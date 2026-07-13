
import streamlit as st

def hero(title, subtitle):
    html_content = (
        f'<div class="hero-card">'
        f'<div class="hero-title">{title}</div>'
        f'<div class="hero-subtitle">{subtitle}</div>'
        f'</div>'
    )
    st.markdown(html_content, unsafe_allow_html=True)

def match_info(text):
    """
    Renders a custom scoped info callout box that resizes to fit text length
    and matches the tactical broadcast UI theme.
    """
    html_content = (
        f'<div class="match-info-callout">'
        f'  <div class="match-info-content">'
        f'  <div class="match-info-text">{text}</div>'
        f'</div>'
    )
    st.markdown(html_content, unsafe_allow_html=True)

def dataset_source_badge(label, url):
    """
    Renders a compact, interactive data badge optimized for out-bound link references.
    """
    html_content = (
        f'<div class="data-source-badge">'
        f'  <div class="data-source-content">'
        f'      <span>Dataset Source: <a href="{url}" target="_blank">{label}</a></span>'
        f'  </div>'
        f'</div>'
    )
    st.markdown(html_content, unsafe_allow_html=True)