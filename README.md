# Solar Potential Dashboard

## Description
A Streamlit dashboard for comparing solar potential (GHI, DNI, DHI) across Benin, Togo, and Sierra Leone.

## Features
- Metric selection (GHI/DNI/DHI)
- Country filtering
- Boxplots and summary statistics

## To Run
```bash
streamlit run app/main.py
# Solar Irradiance Dashboard

## 🚀 Overview
This dashboard allows users to explore solar metrics (GHI, DNI, etc.) across Benin, Togo, and Sierra Leone.

## 📊 Features
- Interactive boxplots
- Country selector
- Summary statistics table

## 🔧 How to Run

```bash
pip install -r requirements.txt
streamlit run app/main.py
# 🌞 Solar Energy Dashboard

A Streamlit-powered web application for visualizing and exploring solar energy datasets from various African regions. This project aims to support solar energy analysis and decision-making using clean, structured data.

---

## 📁 Project Structure

olar-challenge-week1/
│
├── app/
│ ├── main.py # Streamlit app entry point
│ └── utils.py # Helper functions for data loading and processing
│
├── data/ # Raw and cleaned datasets (local use only)
│ ├── benin_clean.csv
│ ├── togo_clean.csv
│ └── sierra_leone_clean.csv
│
├── requirements.txt # Python dependencies
├── README.md # You're reading it!
└── .streamlit/ # Streamlit config files
. **Clone the repo:**

```bash
git clone https://github.com/yourusername/solar-challenge-week1.git
cd solar-challenge-week1
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/main.py
Datasets

Cleaned datasets used in the dashboard:

    benin_clean.csv

    togo_clean.csv

    sierra_leone_clean.csv

These files are processed versions of larger, raw data files and are stored in the data/ directory (not tracked on GitHub due to size or privacy).
Features

    Interactive charts and visualizations

    Country-specific solar performance data

    Caching for performance boost

    Modular design for easy scaling

Tech Stack

    Python

    Pandas

    Streamlit

    Git + GitHub

📌 Notes

    This is the main branch. For development or experimental features, check out the dashboard-dev branch.

    Make sure to keep sensitive or large datasets out of version control by using .gitignore.

🧑‍💻 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.
📄 License

MIT License
📬 Contact

Feel free to reach out if you have questions, suggestions, or want to collaborate!


---

Let me know if you'd like this tailored more specifically for the dev branch or want to include screenshots, badges (like Streamlit deployment status), or links.

