# Hacker News Scraper

This is a Python script that scrapes the top news stories from Hacker News and sends an automated email with the news articles to a recipient.

## Dependencies

The script requires the following Python libraries to be installed:

- requests
- BeautifulSoup
- smtplib

These libraries can be installed using pip. For example, to install requests, run the following command:

```
pip install requests
pip install beautifulsoup4
```


## Usage

To use the script, follow these steps:

1. Clone the repository to your local machine.
2. Open the script `hacker_news_scraper.py` in a text editor.
3. Modify the `FROM`, `TO`, and `PASS` variables to match your email account details.
4. Run the script using the following command:

`python hacker_news_scraper.py`


The script will scrape the top news articles from Hacker News and send an automated email to the recipient specified in the `TO` variable. The email will contain the news articles as HTML text.

