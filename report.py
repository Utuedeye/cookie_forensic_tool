import pandas as pd

def save_report(cookie_df, filename="cookie_report.csv"):
    """Save analyzed cookies to a CSV file."""
    try:
        cookie_df.to_csv(filename, index=False)
        print(f"Report saved as {filename}")
    except Exception as e:
        print(f"Error saving report: {e}")
      
