# ScrapeAI

## Overview
The **ScrapeAI** is a powerful web scraping tool enhanced with AI capabilities to understand and interact with users seamlessly. By leveraging advanced scraping techniques and machine learning models, this project automates data extraction from websites while offering an intuitive interface for user interaction.

## Features
- **Automated Web Scraping**: Extracts relevant data from websites with minimal manual input.
- **AI-Powered Insights**: Integrates AI to summarize, analyze, and provide insights from scraped data.
- **Customizable Targets**: Easily configure scraping targets and data requirements.
- **User-Friendly Interface**: Simple and interactive UI for users to interact with the scraper and adjust settings.
- **Extensible Design**: Modular structure for easy feature addition and updates.

## Technologies Used
- **Python**: Core programming language for the scraper and AI integration.
- **BeautifulSoup**: For parsing HTML and extracting web data.
- **Selenium**: For interacting with dynamic web pages.

## Installation
Follow these steps to set up the project locally:

### Prerequisites
1. Python 3.9 or higher
2. pip (Python package installer)
3. A browser driver (e.g., ChromeDriver for Selenium)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/parasmunoli/ScrapeAI.git
   cd ScrapeAI
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download and set up the browser driver for Selenium. Place it in your system PATH or project directory.


### Starting the Application
Run the following command to start the Flask development server:
```bash
streamlit run main.py
```
Access the application at `http://127.0.0.1:5000`.

## Usage
1. Open the application in your browser.
2. Enter the URL of the website you wish to scrape.
3. Specify the data fields you are interested in (e.g., headings, links, tables).
4. Use the AI-powered assistant to:
   - **Summarize scraped data**
   - **Extract specific insights**
   - **Save results in a structured format (CSV, JSON, or database).**
5. Export or visualize the data using the provided tools.

## Project Structure
```
AI-Web-Scraper/
├── main.py               # Main 
├── scraper.py           # Core scraping logic
├── parser.py            # Paring content to LLM model
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
```

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b <feature-name>
   ```
3. Commit changes and push to your fork.
4. Submit a pull request.