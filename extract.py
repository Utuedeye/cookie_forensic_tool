import browser_cookie3
import pandas as pd

def extract_cookies(browser="chrome"):
    """Extract cookies from the specified browser."""
    try:
        if browser.lower() == "chrome":
            cookies = browser_cookie3.chrome()
        elif browser.lower() == "firefox":
            cookies = browser_cookie3.firefox()
        else:
            raise ValueError("Unsupported browser")

        cookie_data = []
        for cookie in cookies:
            cookie_data.append({
                "name": cookie.name,
                "domain": cookie.domain,
                "secure": cookie.secure,
                "httpOnly": cookie.has_nonstandard_attr('httponly'),
                "expiration": cookie.expires
            })

        return pd.DataFrame(cookie_data)

    except Exception as e:
        print(f"Error extracting cookies: {e}")
        return None
      
