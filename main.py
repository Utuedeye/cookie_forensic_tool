from extract import extract_cookies
from analyze import analyze_cookies
from report import save_report

def main():
    browser = input("Enter browser (chrome/firefox): ").strip().lower()
    cookies = extract_cookies(browser)
    analyzed_cookies, timeline = analyze_cookies(cookies)
    
    if analyzed_cookies is not None:
        save_report(analyzed_cookies)

if __name__ == "__main__":
    main()
  
