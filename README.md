# Cookie Forensic Tool

## Overview
The **Cookie Forensic Tool** is a Python-based solution designed for automated extraction, analysis, and forensic investigation of website cookies. The tool helps cybersecurity professionals, digital forensic investigators, and network security consultants analyze user behavior, detect vulnerabilities, and reconstruct session activities from web browser cookies.

## Features
- Extract cookies from major web browsers (Chrome, Firefox, Safari)
- Analyze cookies for security flags (Secure, HttpOnly, SameSite)
- Identify potential vulnerabilities (session hijacking risks, insecure storage)
- Generate structured reports in CSV format
- Reconstruct user activity timelines based on cookie data

## Prerequisites
Before running the tool, ensure you have the following installed:

- **Python** (Version 3.10 or later)
- **pip** (Python package manager)
- Web browsers (Chrome, Firefox, Safari) installed for testing

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/cookie-forensic-tool.git
   cd cookie-forensic-tool
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Extract Cookies from a Specific Browser
To extract cookies from a web browser, run:
```sh
python cookie_analysis_tool.py --browser Chrome
```
Supported browsers:
- `Chrome`
- `Firefox`
- `Safari`

### Generate Reports
To export extracted cookie data into a CSV file:
```sh
python cookie_analysis_tool.py --browser Firefox --export cookies_report.csv
```

### Sample Outputs

#### **Extracted Cookies Table**
| **Cookie Name** | **Domain** | **Secure** | **HttpOnly** | **Expiration Date** |
|---------------|-----------|----------|-----------|----------------|
| `_ga`        | example.com | Yes      | No        | 2025-02-02    |
| `_session`   | secure.com  | Yes      | Yes       | 2024-12-15    |
| `id`         | test.com    | No       | No        | 2025-06-01    |

#### **Cookie Vulnerability Analysis Output**
```sh
[INFO] Analyzing cookies...
[VULNERABILITY] Detected insecure cookie transmission: Cookie 'id' (test.com) missing Secure flag.
[VULNERABILITY] Cookie '_session' (secure.com) is HttpOnly protected.
[INFO] User activity timeline reconstructed successfully.
```

## Future Improvements
- Add support for additional browsers (Edge, Opera)
- Implement a GUI for easier use
- Enhance reporting with visualization features

## License
This project is open-source and distributed under the MIT License.

## Contributors
- Your Name (your.email@example.com)


