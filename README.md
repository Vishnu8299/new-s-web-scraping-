# Article Scraper Flask Application

This Flask application scrapes articles from the Hindustan Times website, extracts their titles, summaries, publication dates, and images, and provides the data in a downloadable JSON format.

## Features

- **Article Scraping**: Fetches articles from various categories like Technology, Sports, Education, and Latest News.
- **Article Extraction**: Extracts and summarizes articles using the `newspaper3k` library.
- **JSON Download**: Allows users to download the scraped articles as a JSON file.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/article-scraper.git
    cd article-scraper
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK resources**:
    ```python
    import nltk
    nltk.download('punkt')
    ```

## Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/` to view the list of articles.

3. **Download the JSON file** by visiting `http://127.0.0.1:5000/download`.

## Dependencies

- Flask
- requests
- newspaper3k
- nltk
- beautifulsoup4

To install these dependencies, you can use the provided `requirements.txt` file:

```plaintext
Flask==2.2.3
requests==2.28.1
newspaper3k==0.2.8
nltk==3.8.1
beautifulsoup4==4.11.2
