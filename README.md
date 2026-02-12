# Phonepe-Transaction-Insights
A data visualization and analytics project built using Python, Streamlit, Plotly, and SQL to analyze PhonePe transaction, user, and insurance data across Indian states.
# Project Overview
This project extracts PhonePe Pulse data and presents interactive dashboards to analyze:
- State-wise transaction amount
- Registered user growth
- Insurance contribution
- Top performing states
- Map-based visualization of data
  
The application provides dynamic filtering by year and interactive chart exploration
# Tech Stack
- Python - Data extraction and processing
- Streamlit - Web app for visualization
- Plotly - data visualization library
- Pandas - Data transformation
- SQL - Database Handling
- GitHub - Version control
# Features
- Interactive and user-friendly dashboard
- Year-wise filtering of transaction, user, and insurance data
- Choropleth map visualization for state-level analysis
- Top 10 state comparison using dynamic charts
- Treemap, Donut, and Horizontal Bar visualizations
- Real-time interactive hover insights
# 📊 Dashboard Sections

## 🏠 Home
- Overview of the project
- KPI summary metrics
- Transaction growth trend visualization

## 📈 Data Exploration
- State-wise map visualization
- Year filter selection
- Insurance, Transaction, and User analysis

## 🏆 Top Charts
- Top 10 States by Transaction Amount (Treemap)
- Top 10 States by Registered Users (Donut Chart)
- Top 10 States by Insurance Amount (Horizontal Bar Chart)

# 📂 Project Structure

```
Phonepe-Transaction-Insights/
│
├── data/                  # Extracted and processed data files
├── streamlit_app.py       # Main Streamlit dashboard
├── data_extraction.py     # Data extraction and cleaning script
├── requirements.txt       # Required Python libraries
└── README.md              # Project documentation
```


# ▶️ How to Run the Project

1. Clone the repository:
   git clone https://github.com/Prabha-1909/Phonepe-Transaction-Insights.git

2. Navigate to the project folder:
   cd Phonepe-Transaction-Insights

3. Install required libraries:
   pip install -r requirements.txt

4. Run the Streamlit application:
   streamlit run streamlit_app.py
   
# 🔮 Future Enhancements

- Quarter-wise data filtering
- Growth percentage analysis
- Deployment on Streamlit Cloud
- Advanced KPI analytics
- Predictive trend modeling
