# netflix_analyzer.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

print("🎬 Netflix Data Analyzer - Starting...")

# Step 1: Load the data
def load_data():
    """Load Netflix data from CSV file"""
    # Try different possible file names
    possible_files = [
        'NetflixViewingHistory.csv',
        'netflix-viewing-history.csv', 
        'sample_data.csv',
        'viewing-history.csv'
    ]
    
    for file in possible_files:
        if os.path.exists(file):
            df = pd.read_csv(file)
            print(f"✅ Successfully loaded {file}")
            print(f"📊 Found {len(df)} viewing records")
            return df
    
    print("❌ No Netflix data file found!")
    print("Please make sure your CSV file is in the same folder as this script")
    return None

# Step 2: Clean and prepare the data
def clean_data(df):
    """Clean and preprocess the Netflix data"""
    print("🧹 Cleaning data...")
    
    # Make a copy
    clean_df = df.copy()
    
    # Display original columns
    print(f"Original columns: {clean_df.columns.tolist()}")
    
    # Standardize column names (Netflix exports can vary)
    column_mapping = {
        'Title': 'title',
        'Date': 'date',
        'Profile Name': 'profile_name',
        'title': 'title',
        'date': 'date'
    }
    
    for old_col, new_col in column_mapping.items():
        if old_col in clean_df.columns:
            clean_df.rename(columns={old_col: new_col}, inplace=True)
    
    # Convert date to datetime
    clean_df['date'] = pd.to_datetime(clean_df['date'])
    
    # Extract time features
    clean_df['year'] = clean_df['date'].dt.year
    clean_df['month'] = clean_df['date'].dt.month
    clean_df['day_of_week'] = clean_df['date'].dt.day_name()
    clean_df['hour'] = clean_df['date'].dt.hour
    
    # Basic content type detection
    clean_df['is_movie'] = clean_df['title'].str.contains(r'\(\d{4}\)', na=False)
    clean_df['is_tv_show'] = ~clean_df['is_movie']
    
    print("✅ Data cleaning completed!")
    return clean_df

# Step 3: Basic analysis functions
def show_basic_stats(df):
    """Display basic statistics about viewing habits"""
    print("\n" + "="*50)
    print("📈 BASIC VIEWING STATISTICS")
    print("="*50)
    
    total_views = len(df)
    date_range = f"{df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}"
    active_days = df['date'].dt.date.nunique()
    
    print(f"Total viewing sessions: {total_views}")
    print(f"Date range: {date_range}")
    print(f"Days with activity: {active_days}")
    print(f"Average views per day: {total_views/active_days:.2f}")
    
    # Content type breakdown
    movies = df['is_movie'].sum()
    tv_shows = df['is_tv_show'].sum()
    
    print(f"\n🎬 Movies watched: {movies} ({movies/total_views*100:.1f}%)")
    print(f"📺 TV episodes watched: {tv_shows} ({tv_shows/total_views*100:.1f}%)")

def find_top_titles(df, top_n=10):
    """Find most frequently watched titles"""
    print(f"\n🏆 TOP {top_n} MOST WATCHED TITLES")
    print("-" * 30)
    
    top_titles = df['title'].value_counts().head(top_n)
    
    for i, (title, count) in enumerate(top_titles.items(), 1):
        print(f"{i}. {title}: {count} views")
    
    return top_titles

# Step 4: Visualization functions
def create_visualizations(df):
    """Create various charts and graphs"""
    print("\n📊 Creating visualizations...")
    
    # Set up the plotting style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create a 2x2 grid of plots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Netflix Viewing Analysis', fontsize=16, fontweight='bold')
    
    # Plot 1: Most watched titles
    top_titles = df['title'].value_counts().head(8)
    axes[0, 0].barh(range(len(top_titles)), top_titles.values)
    axes[0, 0].set_yticks(range(len(top_titles)))
    axes[0, 0].set_yticklabels([title[:30] + '...' if len(title) > 30 else title for title in top_titles.index])
    axes[0, 0].set_title('Most Watched Titles')
    axes[0, 0].set_xlabel('View Count')
    
    # Plot 2: Viewing by day of week
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_counts = df['day_of_week'].value_counts().reindex(day_order)
    axes[0, 1].bar(day_order, day_counts.values, color='skyblue')
    axes[0, 1].set_title('Viewing by Day of Week')
    axes[0, 1].set_xlabel('Day')
    axes[0, 1].set_ylabel('View Count')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # Plot 3: Viewing by hour
    hour_counts = df['hour'].value_counts().sort_index()
    axes[1, 0].bar(hour_counts.index, hour_counts.values, color='lightcoral')
    axes[1, 0].set_title('Viewing by Hour of Day')
    axes[1, 0].set_xlabel('Hour (24h)')
    axes[1, 0].set_ylabel('View Count')
    
    # Plot 4: Content type pie chart
    content_types = ['TV Shows', 'Movies']
    content_counts = [df['is_tv_show'].sum(), df['is_movie'].sum()]
    axes[1, 1].pie(content_counts, labels=content_types, autopct='%1.1f%%', startangle=90)
    axes[1, 1].set_title('Movies vs TV Shows')
    
    plt.tight_layout()
    plt.savefig('netflix_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Visualizations saved as 'netflix_analysis.png'")

def viewing_timeline(df):
    """Show viewing activity over time"""
    print("\n📅 Creating viewing timeline...")
    
    # Group by month
    monthly_views = df.groupby(df['date'].dt.to_period('M')).size()
    
    plt.figure(figsize=(12, 6))
    monthly_views.plot(kind='line', marker='o', linewidth=2, markersize=6)
    plt.title('Monthly Viewing Activity')
    plt.xlabel('Month')
    plt.ylabel('Number of Views')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Step 5: Advanced analysis
def binge_analysis(df):
    """Analyze potential binge-watching behavior"""
    print("\n🍿 Binge Watching Analysis")
    print("-" * 25)
    
    # Sort by date
    df_sorted = df.sort_values('date').copy()
    
    # Calculate time between views
    df_sorted['time_diff'] = df_sorted['date'].diff()
    
    # Define binge sessions (multiple views within 6 hours)
    binge_threshold = pd.Timedelta(hours=6)
    df_sorted['new_session'] = df_sorted['time_diff'] > binge_threshold
    df_sorted['session_id'] = df_sorted['new_session'].cumsum()
    
    # Analyze sessions
    session_stats = df_sorted.groupby('session_id').agg({
        'title': 'count',
        'date': ['min', 'max']
    })
    
    # Flatten column names
    session_stats.columns = ['views_count', 'session_start', 'session_end']
    session_stats['duration_hours'] = (session_stats['session_end'] - session_stats['session_start']).dt.total_seconds() / 3600
    
    # Filter out single-view sessions
    binge_sessions = session_stats[session_stats['views_count'] > 1]
    
    if len(binge_sessions) > 0:
        print(f"Found {len(binge_sessions)} potential binge sessions!")
        print(f"Longest binge: {binge_sessions['views_count'].max()} episodes")
        print(f"Average binge: {binge_sessions['views_count'].mean():.1f} episodes")
    else:
        print("No significant binge sessions detected.")
    
    return binge_sessions

# Step 6: Main execution function
def main():
    """Main function to run the complete analysis"""
    print("🎬 NETFLIX DATA ANALYZER")
    print("=" * 50)
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Clean data
    cleaned_df = clean_data(df)
    
    # Show basic stats
    show_basic_stats(cleaned_df)
    
    # Find top titles
    top_titles = find_top_titles(cleaned_df, 8)
    
    # Create visualizations
    create_visualizations(cleaned_df)
    
    # Show timeline
    viewing_timeline(cleaned_df)
    
    # Binge analysis
    binge_sessions = binge_analysis(cleaned_df)
    
    print("\n" + "="*50)
    print("✅ ANALYSIS COMPLETE!")
    print("="*50)
    print("\nCheck the generated charts for visual insights!")
    print("Files created:")
    print("  - netflix_analysis.png (main charts)")
    print("\nYou can modify the script to add more analyses!")

# Run the script
if __name__ == "__main__":
    main()