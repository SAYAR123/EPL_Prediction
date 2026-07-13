import streamlit as st
import pandas as pd
import joblib as jb

from ui import hero, match_info

from ELO_pg import home_teams_all

from paths import DUMPED_MODELS_DIR

# Caching loaded resources
@st.cache_resource
def load_items():
    # team_history = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\team_history_all.joblib")
    # elo = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\elo_all.joblib")
    # team_history_xgb = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\team_history_xgb.joblib")

    # model_basic_rf = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\basic_rf_model.joblib")
    # model_rf_elo = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\rf_elo_model.joblib")
    # model_xgb = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\xgb_model.joblib")
    # mlp = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\nn_model.joblib")

    # home_goal_model = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\rf_home_goal_model.joblib")
    # away_goal_model = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\rf_away_goal_model.joblib")

    # home_goal_model_elo = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\rf_elo_home_goal_model.joblib")
    # away_goal_model_elo = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\rf_elo_away_goal_model.joblib")

    # home_goal_model_xgb = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\xgb_home_goal_model.joblib")
    # away_goal_model_xgb = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\xgb_away_goal_model.joblib")

    # home_goal_mlp = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\nn_home_goal.joblib")
    # away_goal_mlp = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\nn_away_goal.joblib")

    # scaler = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\nn_scaler.joblib")

    team_history = jb.load(DUMPED_MODELS_DIR/"team_history_all.joblib")
    elo = jb.load(DUMPED_MODELS_DIR/"elo_all.joblib")
    team_history_xgb = jb.load(DUMPED_MODELS_DIR/"team_history_xgb.joblib")

    model_basic_rf = jb.load(DUMPED_MODELS_DIR/"basic_rf_model.joblib")
    model_rf_elo = jb.load(DUMPED_MODELS_DIR/"rf_elo_model.joblib")
    model_xgb = jb.load(DUMPED_MODELS_DIR/"xgb_model.joblib")
    mlp = jb.load(DUMPED_MODELS_DIR/"nn_model.joblib")

    home_goal_model = jb.load(DUMPED_MODELS_DIR/"rf_home_goal_model.joblib")
    away_goal_model = jb.load(DUMPED_MODELS_DIR/"rf_away_goal_model.joblib")

    home_goal_model_elo = jb.load(DUMPED_MODELS_DIR/"rf_elo_home_goal_model.joblib")
    away_goal_model_elo = jb.load(DUMPED_MODELS_DIR/"rf_elo_away_goal_model.joblib")

    home_goal_model_xgb = jb.load(DUMPED_MODELS_DIR/"xgb_home_goal_model.joblib")
    away_goal_model_xgb = jb.load(DUMPED_MODELS_DIR/"xgb_away_goal_model.joblib")

    home_goal_mlp = jb.load(DUMPED_MODELS_DIR/"nn_home_goal.joblib")
    away_goal_mlp = jb.load(DUMPED_MODELS_DIR/"nn_away_goal.joblib")

    scaler = jb.load(DUMPED_MODELS_DIR/"nn_scaler.joblib")


    return team_history, elo, team_history_xgb, model_basic_rf, model_rf_elo, model_xgb, mlp, home_goal_model, away_goal_model, home_goal_model_elo, away_goal_model_elo, home_goal_model_xgb, away_goal_model_xgb, home_goal_mlp, away_goal_mlp, scaler

team_history, elo, team_history_xgb, model_basic_rf, model_rf_elo, model_xgb, mlp, home_goal_model, away_goal_model, home_goal_model_elo, away_goal_model_elo, home_goal_model_xgb, away_goal_model_xgb, home_goal_mlp, away_goal_mlp, scaler = load_items()

# functions

def get_last_n_stats(matches, n=5):
    last_matches = matches[-n:]
    
    wins, draws, losses = 0, 0, 0
    goals_scored, goals_conceded = 0, 0
    
    for m in last_matches:
        goals_scored += m['scored']
        goals_conceded += m['conceded']
        
        if m['result'] == 'W':
            wins += 1
        elif m['result'] == 'D':
            draws += 1
        else:
            losses += 1
    
    total = len(last_matches)
    
    if total == 0:
        return [0]*6
    
    return [
        wins,
        draws,
        losses,
        goals_scored / total,
        goals_conceded / total,
        (wins*3 + draws) / total   # avg points
    ]


feature_cols_basic_rf = [
    'home_wins', 'home_draws', 'home_losses',
    'home_avg_scored', 'home_avg_conceded', 'home_avg_points',
    
    'away_wins', 'away_draws', 'away_losses',
    'away_avg_scored', 'away_avg_conceded', 'away_avg_points'
]


feature_cols = [
    'home_wins', 'home_draws', 'home_losses',
    'home_avg_scored', 'home_avg_conceded', 'home_avg_points',
    
    'away_wins', 'away_draws', 'away_losses',
    'away_avg_scored', 'away_avg_conceded', 'away_avg_points',
    
    'home_elo', 'away_elo', 'elo_diff'
]


def create_match_features_basic_rf(home_team, away_team):

    home_stats = get_last_n_stats(team_history[home_team])
    away_stats = get_last_n_stats(team_history[away_team])

    features = home_stats + away_stats

    return pd.DataFrame(
        [features],
        columns=feature_cols_basic_rf
    )

def create_match_features_elo(home_team, away_team): # for both rf_elo and nn

    home_stats = get_last_n_stats(team_history[home_team])
    away_stats = get_last_n_stats(team_history[away_team])

    # Same home advantage used during training
    home_elo = elo[home_team] + 100
    away_elo = elo[away_team]

    elo_diff = home_elo - away_elo

    features = (
        home_stats
        + away_stats
        + [home_elo, away_elo, elo_diff]
    )

    return pd.DataFrame(
        [features],
        columns=feature_cols
    )

def create_match_features_xgb(home_team, away_team):

    home_stats = get_last_n_stats(
        team_history_xgb[home_team]['home']
    )

    away_stats = get_last_n_stats(
        team_history_xgb[away_team]['away']
    )

    home_elo = elo[home_team] + 100
    away_elo = elo[away_team]

    elo_diff = home_elo - away_elo

    features = (
        home_stats
        + away_stats
        + [home_elo, away_elo, elo_diff]
    )

    return pd.DataFrame(
        [features],
        columns=feature_cols
    )

def predict_match_st(home_team, away_team):

    features_st = create_match_features_basic_rf(home_team, away_team)

    # Classification probabilities
    probs_st = model_basic_rf.predict_proba(features_st)[0]

    home_win_prob_st = round(probs_st[0], 2)
    draw_prob_st = round(probs_st[1], 2)
    away_win_prob_st = round(probs_st[2], 2)

    # Goal predictions
    home_goals_st = home_goal_model.predict(features_st)[0]
    away_goals_st = away_goal_model.predict(features_st)[0]

    # Make score realistic
    predicted_home_st = max(0, round(home_goals_st))
    predicted_away_st = max(0, round(away_goals_st))

    return[
        home_win_prob_st,
        draw_prob_st,
        away_win_prob_st,
        predicted_home_st,
        predicted_away_st
    ]

def predict_match_elo_st(home_team, away_team):
    features_st = create_match_features_elo(home_team, away_team)

    # Classification probabilities
    probs_st = model_rf_elo.predict_proba(features_st)[0]

    home_win_prob_st = round(probs_st[0], 2)
    draw_prob_st = round(probs_st[1], 2)
    away_win_prob_st = round(probs_st[2], 2)

    # Goal predictions
    home_goals_st = home_goal_model_elo.predict(features_st)[0]
    away_goals_st = away_goal_model_elo.predict(features_st)[0]

    # Make score realistic
    predicted_home_st = max(0, round(home_goals_st))
    predicted_away_st = max(0, round(away_goals_st))

    return[
        home_win_prob_st,
        draw_prob_st,
        away_win_prob_st,
        predicted_home_st,
        predicted_away_st
    ]

def predict_match_xgb_st(home_team, away_team):
    features_st = create_match_features_xgb(home_team, away_team)

    # Classification probabilities
    probs_st = model_xgb.predict_proba(features_st)[0]

    home_win_prob_st = round(probs_st[0], 2)
    draw_prob_st = round(probs_st[1], 2)
    away_win_prob_st = round(probs_st[2], 2)

    # Goal predictions
    home_goals_st = home_goal_model_xgb.predict(features_st)[0]
    away_goals_st = away_goal_model_xgb.predict(features_st)[0]

    # Make score realistic
    predicted_home_st = max(0, round(home_goals_st))
    predicted_away_st = max(0, round(away_goals_st))

    return[
        home_win_prob_st,
        draw_prob_st,
        away_win_prob_st,
        predicted_home_st,
        predicted_away_st
    ]

def predict_match_mlp_st(home_team, away_team):
    features_st = create_match_features_elo(
        home_team,
        away_team
    )

    features_scaled_st = scaler.transform(features_st)

    probs_st = mlp.predict_proba(
        features_scaled_st
    )[0]

    home_win_prob_st = round(probs_st[0], 2)
    draw_prob_st = round(probs_st[1], 2)
    away_win_prob_st = round(probs_st[2], 2)

    home_goals_st = home_goal_mlp.predict(
        features_scaled_st
    )[0]

    away_goals_st = away_goal_mlp.predict(
        features_scaled_st
    )[0]

    predicted_home_st = max(0, round(home_goals_st))
    predicted_away_st = max(0, round(away_goals_st))

    return[
        home_win_prob_st,
        draw_prob_st,
        away_win_prob_st,
        predicted_home_st,
        predicted_away_st
    ]

# from here starts homepage code

def home_page():

    hero(
        "Score & stats prediction for English Premier League matches",
        "Select teams, get prediction of full-time scores, win probabilities and match statistics using Machine Learning."
    )

    st.write('---')

    home_teams = home_teams_all

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_home = st.selectbox(
            label="Select Home Team",
            options=home_teams,
            index=None,
            placeholder="Choose Home Team...",
        )

    with col2:
        # Filtering the selected team so a team cannot be its own rival
        away_options = [team for team in home_teams if team != selected_home]

        selected_away = st.selectbox(
            label="Select Away Team",
            options=away_options,
            index=None,
            placeholder="Choose Away team...",
            disabled=(selected_home is None),  # Lock until first team is chosen
        )

    with col3:
        selected_algo = st.selectbox(
            label="Select Prediction Algorithm",
            options=[
                "Basic Random Forest", 
                "Random Forest with ELO Ratings", 
                "XGBoost Classifier/Regressor", 
                "Neural Network (MLP)"
            ],
            index=None,
            placeholder="Choose algorithm...",
            disabled=(selected_home is None or selected_away is None) # Lock until teams are selected
        )


    if selected_home and selected_away and selected_algo:
        if st.button("Predict Match Outcome", type="primary"):
            st.write("---")
            st.subheader("Prediction Summary:")
            st.caption(f'{selected_home} vs {selected_away}')
            
            # 1. Initialize variables safely
            h_prob, d_prob, a_prob, h_goals, a_goals = 0, 0, 0, 0, 0
            
            # 2. Unpack the returned list values into separate variables
            if selected_algo == "Basic Random Forest":
                match_info("Using Basic Random Forest Model")
                h_prob, d_prob, a_prob, h_goals, a_goals = predict_match_st(selected_home, selected_away)
                
            elif selected_algo == "Random Forest with ELO Ratings":
                match_info("Using Random Forest with ELO Model")
                h_prob, d_prob, a_prob, h_goals, a_goals = predict_match_elo_st(selected_home, selected_away)
                
            elif selected_algo == "XGBoost Classifier/Regressor":
                match_info("Using XGBoost Model")
                h_prob, d_prob, a_prob, h_goals, a_goals = predict_match_xgb_st(selected_home, selected_away)
                
            elif selected_algo == "Neural Network (MLP)":
                match_info("Using Multi-Layer Perceptron (Neural Network) Model")
                h_prob, d_prob, a_prob, h_goals, a_goals = predict_match_mlp_st(selected_home, selected_away)

            # 3. Display the Win/Draw/Loss distribution
            # ... Inside your homepage prediction execution block:
            st.write("### Match Outcome Probabilities")
            prob_col1, prob_col2, prob_col3 = st.columns(3)
            with prob_col1:
                st.metric(label=f"{selected_home} Win\n(Home)", value=f"{int(h_prob * 100)}%")
                st.progress(float(h_prob))
            with prob_col2:
                st.metric(label="Draw", value=f"{int(d_prob * 100)}%")
                st.progress(float(d_prob))
            with prob_col3:
                st.metric(label=f"{selected_away} Win\n(Away)", value=f"{int(a_prob * 100)}%")
                st.progress(float(a_prob))

            st.write("---")

            # 4. Display the Predicted Goals side-by-side using Streamlit Columns
            st.write("### Expected Full-Time Score")
            score_col1, score_col2 = st.columns(2)
            with score_col1:
                st.metric(label=f"{selected_home} Goals", value=int(h_goals))
            with score_col2:
                st.metric(label=f"{selected_away} Goals", value=int(a_goals))
                