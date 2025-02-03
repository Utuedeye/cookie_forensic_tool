import pandas as pd

def analyze_cookies(cookie_df):
    """Analyze cookies for security vulnerabilities and behavior tracking."""
    if cookie_df is None or cookie_df.empty:
        print("No cookies found for analysis.")
        return None

    # Flag insecure cookies
    cookie_df["insecure_flag"] = cookie_df.apply(
        lambda row: not row["secure"] or not row["httpOnly"], axis=1
    )

    # Generate user activity timeline
    timeline = cookie_df.sort_values(by="expiration")[["name", "domain", "expiration"]]
    
    return cookie_df, timeline
  
