import streamlit as st
import joblib as jb

import pandas as pd

from ui import hero

from paths import DUMPED_MODELS_DIR

@st.cache_resource()
def acc():
    # accuracy_basic_rf = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\basic_rf_acc.joblib")
    # accuracy_rf_elo = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\rf_elo_acc.joblib")
    # accuracy_XGBoost = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\xgb_acc.joblib")
    # accuracy_nn = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\nn_acc.joblib")

    # mae_basic_rf = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\mae_basic_rf.joblib")

    # mae_rf_elo = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\mae_rf_elo.joblib")

    # mae_xgb = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\mae_xgb.joblib")

    # mae_nn = jb.load(r"C:\Projects\football_final\training\dumped_models_vars\mae_nn.joblib")

    accuracy_basic_rf = jb.load(DUMPED_MODELS_DIR/"basic_rf_acc.joblib")
    accuracy_rf_elo = jb.load(DUMPED_MODELS_DIR/"rf_elo_acc.joblib")
    accuracy_XGBoost = jb.load(DUMPED_MODELS_DIR/"xgb_acc.joblib")
    accuracy_nn = jb.load(DUMPED_MODELS_DIR/"nn_acc.joblib")

    mae_basic_rf = jb.load(DUMPED_MODELS_DIR/"mae_basic_rf.joblib")

    mae_rf_elo = jb.load(DUMPED_MODELS_DIR/"mae_rf_elo.joblib")

    mae_xgb = jb.load(DUMPED_MODELS_DIR/"mae_xgb.joblib")

    mae_nn = jb.load(DUMPED_MODELS_DIR/"mae_nn.joblib")

    return accuracy_basic_rf, accuracy_rf_elo, accuracy_XGBoost, accuracy_nn, mae_basic_rf, mae_rf_elo, mae_xgb, mae_nn


accuracy_basic_rf, accuracy_rf_elo, accuracy_XGBoost, accuracy_nn, mae_basic_rf, mae_rf_elo, mae_xgb, mae_nn = acc()

def model_accuracy():

    hero(
        "Model Performance",
        "Compare the prediction accuracy of all Machine Learning models."
    )

    st.subheader("Match Outcome Accuracy [Classification]")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Basic Random Forest",
            f"{accuracy_basic_rf*100:.2f}%"
        )

    with col2:
        st.metric(
            "Random Forest with ELO",
            f"{accuracy_rf_elo*100:.2f}%"
        )

    with col3:
        st.metric(
            "XGBoost",
            f"{accuracy_XGBoost*100:.2f}%"
        )

    with col4:
        st.metric(
            "Neural Network (MLP)",
            f"{accuracy_nn*100:.2f}%"
        )

    st.divider()

    st.subheader("Goal Prediction NMAE(Negative Mean Absolute Error) Value [Regression]")
    st.caption("By how many goals is the model prediction off")
    st.caption("Lower values indicate better performance")

    mae_df = pd.DataFrame({
        "Model": [
            "Basic Random Forest",
            "Random Forest with ELO",
            "XGBoost",
            "Neural Network (MLP)"
        ],
        "Home Goals NMAE Value": [
            mae_basic_rf[0],
            mae_rf_elo[0],
            mae_xgb[0],
            mae_nn[0]
        ],
        "Away Goals NMAE Value": [
            mae_basic_rf[1],
            mae_rf_elo[1],
            mae_xgb[1],
            mae_nn[1]
        ]
    })

    st.dataframe(
        mae_df.style.format({
            "Home Goals NMAE Value": "{:.2f}",
            "Away Goals NMAE Value": "{:.2f}"
        }),
        use_container_width=True,
        hide_index=True
    )