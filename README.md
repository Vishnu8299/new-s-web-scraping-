# News Article Scraper and Downloader

This Flask application scrapes news articles from the Hindustan Times website and provides a downloadable JSON file containing the article details, including title, summary, publish date, and image URL.

## Features

- **Article Scraping**: Scrapes articles from categories like Technology, Sports, Education, and Latest News.
- **Article Summarization**: Uses the `newspaper3k` library to summarize articles.
- **JSON Export**: Allows users to download the scraped articles as a JSON file.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/news-article-scraper.git
    cd news-article-scraper
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install requests flask newspaper3k beautifulsoup4 nltk
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

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/` to view the scraped articles.

3. **Download the JSON file** containing article details by navigating to `http://127.0.0.1:5000/download`.

## Project Structure

news-article-scraper/
- app.py # Main Flask application script
- requirements.txt # List of dependencies
- news.html # HTML template for displaying articles
- README.md # This file

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
If you have suggestions or improvements, please fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any questions or feedback, please reach out to vishnuvardhanv046@gmail.com.
  
## Dependencies

- Flask
- Requests
- Newspaper3k
- BeautifulSoup4
- NLTK

To install these dependencies, use the `requirements.txt` file:

```plaintext
Flask==2.2.3
requests==2.28.2
newspaper3k==0.2.8
beautifulsoup4==4.12.2
nltk==3.8.1
