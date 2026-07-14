# EPL MatchVision — AI-Powered English Premier League Match Prediction System

**Enterprise-grade machine learning application for predicting English Premier League match outcomes, final scores, win/draw/loss probabilities, expected goals, and team statistics using historical match data, ELO ratings, and multiple machine learning models through an interactive Streamlit interface.**

### 🔴 Live Demo

**[https://epl-prediction-yxf5.onrender.com/](https://epl-prediction-yxf5.onrender.com/)**

> Hosted on Render's free tier — the app may take **30–60 seconds** to wake up on first load if it has been idle. Subsequent navigation will be fast.

EPL MatchVision leverages decades of English Premier League historical data to generate intelligent football predictions. By combining feature engineering, dynamic ELO ratings, historical team performance, and multiple machine learning algorithms, the application predicts match winners, expected goals, final scorelines, and win/draw/loss probabilities. Alongside predictions, users can explore detailed club histories, Premier League information, model performances, and historical datasets through a modern Streamlit web application.

Machine learning powered predictions &nbsp;·&nbsp; Multi-model comparison &nbsp;·&nbsp; ELO rating integration &nbsp;·&nbsp; Win/Draw/Loss probabilities &nbsp;·&nbsp; Final score prediction &nbsp;·&nbsp; Interactive Streamlit dashboard

---

# Features

## Match Outcome Prediction
- Predicts the final outcome as **Home Win**, **Draw**, or **Away Win**
- Supports multiple machine learning models for prediction
- Generates confidence-based predictions using historical match statistics
- Allows users to compare predictions across different models

## Final Score Prediction
- Predicts the expected number of goals scored by both teams
- Uses dedicated regression models for Home Goals and Away Goals
- Displays the projected final scoreline
- Provides realistic score estimates using historical team performances

## Win / Draw / Loss Probability Estimation
- Calculates probabilities for every possible match outcome
- Displays prediction confidence through probability distributions
- Helps users interpret model certainty instead of relying on a single prediction
- Supports better analytical decision-making

## ELO Rating Integration
- Incorporates dynamic ELO ratings into prediction models
- Measures relative team strength based on historical performances
- Improves prediction accuracy by considering long-term consistency
- Dedicated page explaining ELO ratings and team rankings

## Historical Team Statistics
- Retrieves historical performance statistics for every club
- Displays team strengths before prediction
- Uses engineered historical features during model inference
- Supports comparative analysis between competing teams

## About Premier League & Clubs
- Brief history of the English Premier League
- League structure and competition format
- Trophy history and major milestones
- Information about all clubs present in the dataset
- Club foundation details, historical achievements, legendary players, and current status

## Dataset Explorer
- Interactive viewer for the complete historical dataset
- Allows users to inspect the data used during model training
- Displays historical match records in tabular format
- Enhances transparency of the prediction pipeline

## Model Performance Dashboard
- Displays classification accuracy of every prediction model
- Shows Mean Absolute Error (MAE) for Home Goal and Away Goal regressors
- Enables easy comparison between different machine learning models
- Helps users understand the strengths of each approach

## Multiple Machine Learning Models
- Random Forest Classifier
- Random Forest with ELO features
- XGBoost Classifier
- Neural Network Classifier
- Dedicated regression models for Home Goals and Away Goals

## Interactive Streamlit Interface
- Clean and responsive user interface
- Multi-page navigation
- Team logos integrated throughout the application
- Modern layout with intuitive workflow
- Easy-to-use prediction forms

---

# Application Preview

## Home Page
<img width="1912" height="785" alt="Home Page" src="https://github.com/user-attachments/assets/aba90166-f7a2-4ac5-b731-6b9399347868" />

## Match Prediction
<img width="1907" height="787" alt="Match Prediction" src="https://github.com/user-attachments/assets/06daeb83-6d6f-4bef-a5e6-83d3784d062b" />

## Final Score Prediction
<img width="1915" height="818" alt="Final Score Prediction" src="https://github.com/user-attachments/assets/279d4753-10b7-4546-abe9-8621d77acf05" />

## Win / Draw / Loss Probabilities
<img width="1918" height="767" alt="Win Draw Loss Probabilities" src="https://github.com/user-attachments/assets/00cedc2c-290d-487b-9ec8-7364afadfc48" />

## Team ELO Ratings
<img width="1907" height="803" alt="Team ELO Ratings" src="https://github.com/user-attachments/assets/52448d61-6213-432e-8e8b-bd789acb030b" />

## About EPL & Teams
<img width="1903" height="810" alt="About EPL and Teams" src="https://github.com/user-attachments/assets/8eaa491e-b799-4550-b399-6dd0e81b088f" />

## Dataset Explorer
<img width="1905" height="807" alt="Dataset Explorer" src="https://github.com/user-attachments/assets/4bfcdf6c-28b1-4b2a-aab9-725d6da35a10" />

## Model Performance
<img width="1911" height="807" alt="Model Performance" src="https://github.com/user-attachments/assets/d7bb9973-1801-4741-9bc3-995fb2c1fa86" />

---

# How It Works

## Prediction Workflow

```text
                 Historical EPL Dataset
                          │
                          ▼
            Data Cleaning & Preprocessing
                          │
                          ▼
                Feature Engineering
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
Historical Team Statistics           Dynamic ELO Ratings
        │                                   │
        └─────────────────┬─────────────────┘
                          ▼
               Prediction Feature Vector
                          │
        ┌─────────────────┼──────────────────┐
        ▼                 ▼                  ▼
 Random Forest        XGBoost         Neural Network
 Classifier           Classifier        Classifier
        │                 │                  │
        └─────────────────┼──────────────────┘
                          ▼
              Match Outcome Prediction
                          │
                          ▼
             Goal Regression Models
      (Home Goals & Away Goals Prediction)
                          │
                          ▼
     Win Probability • Draw Probability • Away Probability
                          │
                          ▼
             Final Score & Match Statistics
                          │
                          ▼
              Interactive Streamlit Interface
```

### Step-by-Step Process

1. The user selects the **Home Team** and **Away Team** from the prediction interface.
2. Historical statistics of both clubs are retrieved from the preprocessed dataset.
3. Latest ELO ratings are incorporated into the feature vector.
4. Feature engineering generates the complete input required by the machine learning models.
5. The selected classification model predicts the match outcome as **Home Win**, **Draw**, or **Away Win**.
6. Dedicated regression models estimate the expected Home Goals and Away Goals independently.
7. The system computes win, draw, and loss probabilities based on model outputs.
8. Results are displayed through the Streamlit interface along with the predicted scoreline, probabilities, model information, and supporting statistics.

---

# Model Evaluation

The project evaluates every machine learning model using both **classification** and **regression** metrics to measure prediction quality across different tasks.

Classification models are evaluated based on their ability to correctly predict the match outcome, while regression models are assessed on how accurately they estimate the number of goals scored by each team.

## Classification Evaluation

The following metric is used for match outcome prediction.

| Metric | Description |
|---------|-------------|
| Accuracy Score | Percentage of correctly predicted Home Win, Draw, and Away Win outcomes |

Higher accuracy indicates better overall classification performance.

## Regression Evaluation

Separate regression models predict Home Goals and Away Goals.

Each regression model is evaluated using Mean Absolute Error (MAE).

| Metric | Description |
|---------|-------------|
| Home Goal MAE | Average prediction error for home team goals |
| Away Goal MAE | Average prediction error for away team goals |

A lower MAE indicates more accurate goal prediction.

## Model Comparison

The application provides a dedicated **Model Performance** page where users can compare all implemented models.

The comparison includes:

- Classification Accuracy
- Home Goal MAE
- Away Goal MAE
- Overall model performance

This allows users to understand the trade-offs between different machine learning approaches.

---

# Streamlit Application

The project is a multi-page Streamlit application that enables users to interact with the prediction models without requiring any programming knowledge. It is deployed and publicly accessible on **Render**.

## Application Modules

| Module | Purpose |
|---------|---------|
| Home | Introduction and navigation |
| Match Prediction | Predict match outcome and final score |
| About EPL | Premier League history and competition format |
| Teams | Information about all clubs in the dataset |
| ELO Ratings | Team ELO rankings and explanation |
| Dataset Explorer | View the historical dataset |
| Model Performance | Compare machine learning models |
| Developers | Project information |

---

# Application Workflow

```text
Launch Streamlit
        │
        ▼
Select Prediction Model
        │
        ▼
Choose Home Team
        │
        ▼
Choose Away Team
        │
        ▼
Load Historical Statistics
        │
        ▼
Generate Feature Vector
        │
        ▼
Run Classification Model
        │
        ▼
Run Goal Regression Models
        │
        ▼
Calculate Match Probabilities
        │
        ▼
Display Prediction Results
```

---

# Technologies Used

## Programming Languages
- Python

## Machine Learning
- Scikit-learn
- XGBoost
- Multi-layer Perceptron (MLP)
- Joblib

## Data Processing
- Pandas
- NumPy

## Data Visualisation
- Matplotlib
- Plotly

## Web Framework
- Streamlit

## Deployment
- Render

## Development Environment
- Visual Studio Code
- Jupyter Notebook

---

# Getting Started

## Option 1 — Use the Live App (Recommended)

No installation required. Simply open the deployed application:

**[https://epl-prediction-yxf5.onrender.com/](https://epl-prediction-yxf5.onrender.com/)**

> Note: Render's free-tier instances spin down after periods of inactivity. If the app appears blank or slow on first visit, wait 30–60 seconds and refresh.

## Option 2 — Run Locally

### Requirements

Before running the application locally, ensure the following software is installed.

- Python 3.10 or later
- pip
- Git

### Clone Repository

```bash
git clone https://github.com/SAYAR123/EPL_Prediction.git

cd EPL_Prediction
```

### Install Dependencies

```bash
pip install -r req.txt
```

### Run the Application

```bash
streamlit run frontend/app.py
```

The Streamlit application will launch in your default web browser at `http://localhost:8501`.

---

# Usage

1. Open the [live application](https://epl-prediction-yxf5.onrender.com/) or launch it locally.
2. Navigate to the **Match Prediction** page.
3. Select the preferred machine learning model.
4. Choose the Home Team.
5. Choose the Away Team.
6. Click the prediction button.
7. View:
   - Match Winner
   - Home Win Probability
   - Draw Probability
   - Away Win Probability
   - Predicted Home Goals
   - Predicted Away Goals
   - Expected Final Score

Users can also explore:

- Historical club information
- Premier League history
- ELO ratings
- Dataset viewer
- Model performance dashboard

---

# Use Cases

This project can be applied in several domains of sports analytics and machine learning.

- Football match prediction
- Sports analytics research
- Machine learning portfolio demonstration
- Feature engineering case study
- Educational project for predictive analytics
- Model comparison and evaluation
- Football statistics exploration
- Data science learning
- Streamlit application development
- Sports AI experimentation

---

# Repository Highlights

- Multi-model prediction system
- Classification and regression pipeline
- ELO rating integration
- Historical team statistics
- Interactive Streamlit interface
- Modular application architecture
- Serialized machine learning models using Joblib
- Separate training and inference workflow
- User-friendly prediction dashboard
- Comprehensive Premier League information pages
- Live public deployment on Render

---

# Future Improvements

The project can be further enhanced by incorporating more advanced machine learning techniques, real-time football data, and explainable AI methods.

### Model Improvements
- Ensemble voting framework combining predictions from multiple machine learning models
- Hyperparameter optimisation using Bayesian Optimization or Optuna
- Automated model retraining with newly available Premier League seasons
- Feature selection using SHAP and permutation importance
- Cross-validation with rolling time-series splits
- Integration of advanced deep learning architectures

### Data Enhancements
- Real-time fixture and results integration through football APIs
- Player-level statistics and performance metrics
- Injury reports and suspension information
- Team lineup prediction
- Expected Goals (xG) and Expected Assists (xA) integration
- Weather and stadium condition analysis
- Referee statistics and historical officiating trends

### User Interface Improvements
- Interactive probability visualisations
- Head-to-head comparison dashboard
- Team performance trend graphs
- Season-wise filtering options
- Match history timeline
- Responsive mobile interface

### Explainable AI
- SHAP-based feature importance visualisation
- Prediction explanation dashboard
- Confidence analysis for every prediction
- Comparison of feature contributions across different models

### Deployment
- Custom domain and paid Render tier to eliminate cold-start delays
- Docker containerisation
- CI/CD pipeline using GitHub Actions
- REST API for prediction services
- Authentication and user profile support

---

# Performance Optimisations

Future versions may include several optimisations to improve scalability and responsiveness.

- Faster inference using model caching
- Lazy loading of machine learning models
- Parallel prediction pipeline
- Efficient memory management
- Reduced application startup and cold-start time on Render
- Optimised feature computation
- GPU-accelerated model inference where applicable

---

# Learning Outcomes

This project demonstrates practical implementation of several data science and software engineering concepts.

## Machine Learning
- Classification algorithms
- Regression algorithms
- Ensemble learning
- Neural networks
- Model evaluation
- Hyperparameter tuning

## Data Science
- Data preprocessing
- Feature engineering
- Historical data analysis
- Model comparison
- Performance evaluation

## Software Development
- Streamlit application development
- Modular project architecture
- Object serialization using Joblib
- Interactive dashboard development
- User interface design
- Cloud deployment on Render

## Football Analytics
- ELO rating systems
- Match outcome prediction
- Goal prediction
- Team performance analysis
- Probability estimation

---

# Project Highlights

- Predicts English Premier League match outcomes using multiple machine learning models.
- Estimates Home Goals and Away Goals through dedicated regression models.
- Generates Win, Draw, and Away Win probabilities.
- Incorporates dynamic ELO ratings to improve predictive performance.
- Utilises historical team statistics and engineered features.
- Interactive multi-page Streamlit web application.
- Publicly deployed and accessible via Render.
- Includes comprehensive information about the Premier League and participating clubs.
- Supports comparison between different machine learning models.
- Displays model evaluation metrics for both classification and regression.
- Modular and extensible project architecture suitable for future enhancements.

---

# Acknowledgements

This project was developed as an academic machine learning and sports analytics project.

Special thanks to:

- The open-source Python community
- Scikit-learn contributors
- XGBoost developers
- Streamlit development team
- Kaggle community for publicly available football datasets
- The football analytics community for inspiring predictive modelling approaches

---

# Developers

**Sawmik Pal**

**Sarthak Mukherjee**

**Sayar Sekhar Ghosh**

**Pramiti Ghosh**

**Soumik Mandal**

(Computer Science Engineering Students)

Githubs: Below(Contact/ Developer Profiles)

---

# License

This project is intended for educational, research, and portfolio purposes.

Please refer to the repository's `LICENSE` file for licensing information.

---

# Contributing

Contributions are welcome and greatly appreciated.

If you would like to contribute:

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes.

```bash
git commit -m "Add YourFeature"
```

4. Push to your branch.

```bash
git push origin feature/YourFeature
```

5. Open a Pull Request describing your proposed improvements.

Please ensure that:

- Code follows consistent formatting.
- New features are properly documented.
- Existing functionality is not broken.
- Appropriate testing is performed before submission.

---

# Contact

For suggestions, collaborations, or feedback, feel free to connect through GitHub.

**Live App:** https://epl-prediction-yxf5.onrender.com/

**Repository:** https://github.com/SAYAR123/EPL_Prediction

**Developer Profiles:**

Sawmik Pal, Sarthak Mukherjee, Sayar Sekhar Ghosh, Pramiti Ghosh, Soumik Mandal

- https://github.com/SawmikPal
- https://github.com/GoldenHeart2000
- https://github.com/SAYAR123
- https://github.com/PRAMITI-GHOSH
- https://github.com/Rony0387

---

## Citation

If you find this project useful in your work or research, please consider citing or starring the repository.

```text
Sawmik Pal, Sarthak Mukherjee, Sayar Sekhar Ghosh, Pramiti Ghosh, Soumik Mandal
EPL MatchVision: AI-Powered English Premier League Match Prediction System.
GitHub Repository: https://github.com/SAYAR123/EPL_Prediction
Live Demo: https://epl-prediction-yxf5.onrender.com/
```

---

## Repository Statistics

| Category | Description |
|----------|-------------|
| Domain | Sports Analytics |
| Application | English Premier League Match Prediction |
| Framework | Streamlit |
| Language | Python |
| Machine Learning | Scikit-learn, XGBoost, Neural Network |
| Prediction Type | Classification & Regression |
| Outcome Prediction | Home Win / Draw / Away Win |
| Goal Prediction | Home Goals & Away Goals |
| Probability Prediction | Win / Draw / Loss |
| Deployment | Render |
| Additional Features | ELO Ratings, Team Statistics, Club Information |

---

This repository showcases the application of machine learning, feature engineering, football analytics, and interactive web development to create an end-to-end prediction system for English Premier League matches. It serves as both a practical sports analytics application and a demonstration of modern data science techniques for predictive modelling.
