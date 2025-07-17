## ControlUP - Automation Home Test ##
This project contains UI and API automated tests.
`HomeTest/test_ui.py` , `HomeTest/test_api.py`
The UI tests use Selenium WebDriver, and the API tests use Requests.
All tests are written in Python using the pytest framework.

## Instructions ## 
1. Clone the repository:
    * bash `git clone https://github.com/GaliGit2/ControlUP-HomeTest.git`

2. Install dependencies:
    * bash `pip install -r requirements.txt`
    * Make sure you have Python 3.7+ and Chrome browser installed.

3. Running the Tests:
    * Run bash `cd HomeTest`
    * Run all tests: bash `python -m pytest` 
    * Run UI tests only: bash `python -m pytest tests\test_ui.py` 
    * Run API tests only: bash `python -m pytest tests\test_api.py`

4. Notes:
    * ChromeDriver must match your Chrome version.
    * `--headless` mode is available in test_ui (commented out in the code) for CI/CD use.
    * Credentials, and URLs, and constants are stored in `config.py`.
    * Locators are centralized in `locators.py`.
    * The `ui_helpers.py` file contains reusable helper functions for interacting with UI elements using Selenium.
    * The `api_helpers.py` file contains reusable helper functions for API requests.
