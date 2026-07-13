import streamlit as st
import pandas as pd
import joblib as jb
import os
import base64  # Added to convert local files to table-readable strings

from ui import hero, match_info

from paths import DUMPED_MODELS_DIR, LOGOS_DIR

@st.cache_resource
def elos():
    # elo_teams = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\elo_all.joblib")
    elo_teams = jb.load(DUMPED_MODELS_DIR/"elo_all.joblib")
    return elo_teams

elo_teams = elos()
elo_teams_sorted = dict(sorted(elo_teams.items()))

home_teams_all = list(elo_teams_sorted.keys())
# logo_folder = r"C:\Projects\football_final\frontend\logos" 
logo_folder = LOGOS_DIR

# Helper function to convert a local image into an inline Data URL string
def get_base64_image(image_path):
    if os.path.exists(image_path):
        try:
            with open(image_path, "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode()
            return f"data:image/png;base64,{encoded_string}"
        except Exception:
            pass
    # Return None if file is missing or unreadable so Streamlit handles fallback cleanly
    return None

data_rows = []
for team in home_teams_all:
    logo_path = os.path.join(logo_folder, f"{team}.png")
    
    # Convert local image to Base64 data string
    final_logo = get_base64_image(logo_path)
    elo_score = round(elo_teams_sorted[team], 2)
    
    data_rows.append({
        "Logo": final_logo,
        "EPL Team": team,
        "ELO Rating": elo_score
    })

df = pd.DataFrame(data_rows)

def elo_rating():

    hero(
        "Team ELO Ratings",
        "ELO ratings of every Premier League team generated using historical match performance."
    )

    match_info(
    "Custom Team ELO rating system is the unique and key feature of the project, which continuously updates team strengths based on match results to enhance prediction performance."
    )

    st.dataframe(
        df,
        column_config={
            "Logo": st.column_config.ImageColumn(
                "Logo", 
                help="Team Crest Logo",
                width="small",
                alignment="center"
            ),
            "EPL Team": st.column_config.TextColumn(
                "EPL Team"
            ),
            "ELO Rating": st.column_config.NumberColumn(
                "ELO Rating",
                format="%.2f",
                alignment="left"
            )
        },
        hide_index=True,
        use_container_width=True
    )