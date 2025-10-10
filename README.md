# 🎬 Netflix Viewing Habits Analyzer

A comprehensive Python tool to analyze your Netflix viewing history and uncover fascinating insights about your streaming habits. Discover your most-watched shows, viewing patterns, binge sessions, and more!

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-orange.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📊 What This Project Does

This project transforms your raw Netflix viewing history into beautiful visualizations and actionable insights:

- **📈 Viewing Patterns**: Discover when you watch most (days, hours, months)
- **🏆 Top Content**: Identify your most-watched shows and movies
- **🍿 Binge Analysis**: Detect marathon viewing sessions
- **🎬 Content Preferences**: Movies vs TV shows breakdown
- **📅 Trends Over Time**: See how your habits change month-to-month

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- 100MB free disk space

### Installation

1. **Clone or Download this project**
```bash
git clone https://github.com/yourusername/netflix-analysis.git
cd netflix-analysis
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Get your Netflix data**
   - Go to [Netflix Account](https://www.netflix.com/account)
   - Click "Get your personal information"
   - Request "Viewing Activity"
   - Download when ready (takes 24-48 hours)
   - Extract the ZIP file and place `NetflixViewingHistory.csv` in the project folder

4. **Run the analysis**
```bash
python netflix_analyzer.py
```

## 🛠️ Usage Methods

### Method 1: Command Line Script (Recommended)
```bash
# Run the complete analysis
python netflix_analyzer.py

# Output includes:
# - Console statistics and insights
# - Visual charts saved as PNG files
# - CSV reports with detailed data
```

### Method 2: Jupyter Notebook (Best for Beginners)
```bash
# Launch Jupyter
jupyter notebook

# Open and run Netflix_Analysis_Notebook.ipynb
# Follow the step-by-step cells for interactive analysis
```

### Method 3: Interactive Web Dashboard
```bash
# Launch Streamlit app (if implemented)
streamlit run app.py
```

## 📁 Project Structure

```
netflix-analysis/
│
├── netflix_analyzer.py          # Main analysis script
├── requirements.txt             # Python dependencies
├── README.md                   # This file
│
├── NetflixViewingHistory.csv   # Your data (after export)
├── sample_data.csv            # Sample data for testing
│
├── notebooks/
│   └── Netflix_Analysis_Notebook.ipynb  # Interactive notebook
│
└── outputs/                    # Generated files
    ├── netflix_analysis.png    # Main dashboard chart
    ├── viewing_patterns.csv    # Statistical summary
    ├── top_titles.csv         # Most watched content
    └── analysis_summary.json   # Insights report
```

## 🎯 Features

### 🔍 Core Analysis
- **Basic Statistics**: Total views, date range, active days
- **Content Analysis**: Movies vs TV shows, genre preferences
- **Temporal Patterns**: Daily, weekly, monthly viewing habits
- **Top Content**: Most frequently watched titles

### 📊 Visualizations
- **Multi-panel Dashboard**: Comprehensive overview charts
- **Time Series**: Monthly viewing trends
- **Pattern Analysis**: Day-of-week and hourly distributions
- **Content Breakdown**: Movies vs TV shows pie chart

### 🍿 Advanced Insights
- **Binge Detection**: Identify marathon viewing sessions
- **Genre Analysis**: Content category preferences
- **Seasonal Trends**: Viewing patterns throughout the year
- **Personalized Reports**: Custom insights based on your data

## 📸 Sample Output

### Console Insights
```
🎬 NETFLIX VIEWING HABITS REPORT
==================================================
Total viewing sessions: 247
Date range: 2023-01-15 to 2023-10-15
Active days: 89
Average views per day: 2.78

🎬 Movies watched: 54 (21.9%)
📺 TV episodes watched: 193 (78.1%)

🏆 TOP 5 MOST WATCHED TITLES
• The Office: 45 views
• Stranger Things: 32 views  
• Breaking Bad: 28 views
• Avengers: Endgame: 12 views
• The Queen's Gambit: 10 views
```

### Generated Visualizations
The tool creates several charts including:
- Most watched titles horizontal bar chart
- Weekly viewing patterns
- Hourly distribution heatmap
- Monthly trends over time
- Content type breakdown

## 🛠️ Customization

### Modify Analysis Parameters
Edit `netflix_analyzer.py` to customize:

```python
# Change binge detection threshold (hours)
binge_threshold = 6  # Default: 6 hours between views

# Adjust top titles count
top_n_titles = 10    # Default: 10 most watched

# Modify date ranges for comparison
start_date = '2023-01-01'
end_date = '2023-12-31'
```

### Add New Analysis Features
Extend the project by adding:

```python
# Genre analysis
def analyze_genres(df):
    genre_keywords = {
        'Comedy': ['office', 'friends', 'comedy'],
        'Drama': ['breaking bad', 'crown', 'drama'],
        'Sci-Fi': ['stranger things', 'dark', 'black mirror']
    }
    # Your implementation here
```

## 🐛 Troubleshooting

### Common Issues

**"File not found" error**
- Ensure `NetflixViewingHistory.csv` is in the project folder
- Check the file name matches exactly
- Try using the sample data first

**Module import errors**
```bash
# Reinstall requirements
pip install --upgrade -r requirements.txt
```

**Date parsing issues**
- The script handles multiple date formats automatically
- Check your Netflix export uses standard date formatting

**Memory errors with large datasets**
- The script includes chunked processing for large files
- Reduce the `chunk_size` parameter if needed

### Getting Help
1. Check the `sample_data.csv` works first
2. Run with `--verbose` flag for detailed logs
3. Open an issue on GitHub with your error message

## 🚀 Advanced Usage

### API Integration
```python
# Add movie ratings from OMDB API
import requests
def get_movie_rating(title):
    api_key = "your_omdb_api_key"
    # Implementation here
```

### Database Storage
```python
# Save results to SQLite
import sqlite3
def save_to_database(df, insights):
    conn = sqlite3.connect('netflix_analysis.db')
    df.to_sql('viewing_history', conn, if_exists='replace')
```

### Automated Reporting
```python
# Generate PDF reports
from matplotlib.backends.backend_pdf import PdfPages
def create_pdf_report(figures, filename):
    with PdfPages(filename) as pdf:
        for fig in figures:
            pdf.savefig(fig)
```

## 📈 Example Insights You Might Discover

- "You watch 73% more Netflix on Fridays than Mondays"
- "Your most active viewing hour is 9 PM"
- "Longest binge session: 8 episodes of Stranger Things in one day"
- "82% of your viewing is TV shows vs 18% movies"
- "October was your most active month with 67 views"

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Areas for Contribution
- New visualization types
- Additional data sources (other streaming services)
- Machine learning recommendations
- Web interface improvements
- Performance optimizations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Netflix for providing personal data exports
- Pandas, Matplotlib, and Seaborn communities
- Inspired by the growing field of personal analytics

## 📞 Support

If you encounter any problems or have questions:

1. Check the [Troubleshooting](#🐛-troubleshooting) section
2. Search existing [GitHub Issues][(https://github.com/yourusername/netflix-analysis/issues)](https://github.com/Rakeshln222/-Analyze-Your-Netflix-Data)
3. Create a new issue with your problem and system information

