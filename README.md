# Web Automation with Selenium and Chrome WebDriver
This project demonstrates web automation using Selenium WebDriver with Python and Chrome browser.

## Prerequisites

- Python 3.x installed
- Google Chrome browser installed
- pip (Python package manager)

## Installation Steps

# Create and activate virtual environment(recommended):
    python -m venv venv
# On Windows
    venv\Scripts\activate
# On macOS/Linux
    source venv/bin/activate
    
# Install the packages:
    pip install selenium
    pip install webdriver-manager

**Running the Project:**
# Navigate to project directory:
    cd project-directory
# Run main script:  
    python src/main.py

  
# Common Issues and Solutions: <br>
  **1)ChromeDriver Version Mismatch:** <br>
      The WebDriver Manager automatically handles this, but if using manual installation, ensure ChromeDriver version matches your Chrome browser version. <br>
  **2)Element Not Found Exceptions:**
  <br>
      Use appropriate waits (explicit or implicit) <br>
      Verify element selectors <br>
      Check if element is inside an iframe <br>
  **3)Element Not Clickable:** <br>
      Ensure element is visible and not covered by other elements <br>
      Scroll element into view before clicking <br>
