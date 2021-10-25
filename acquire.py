import pandas as pd
from bs4 import BeautifulSoup


def get_codeup_articles(urls):
    """Scrape codeup.com
    Args:
        List of strings to modify site
    Out:
        List of dictionaries
    """
    site = "https://codeup.com/"
    soup = BeautifulSoup('html.parser')
    dicts = {'title': 'the title of the article',
             'content': 'the full text content of the article'}
    
    return dicts
    
    
def get_inshorts_articles(topics):
    """Scrape inshorts.com
    Args:
        List of strings to modify site
    Out:
        List of dictionaries
    """
    site = "https://inshorts.com/en/read/"
    soup = BeautifulSoup('html.parser')
    dicts = {'title': 'The article title',
             'content': 'The article content',
             'category': 'business'}
    
    return dicts


if __name__ == "__main__":
    
    urls = ["codeups-data-science-career-accelerator-is-here/,
            "data-science-myths/",
            "data-science-vs-data-analytics-whats-the-difference/",
            "10-tips-to-crush-it-at-the-sa-tech-job-fair/",
            "competitor-bootcamps-are-closing-is-the-model-in-danger/"]
    dicts = get_codeup_articles(urls)
    print(pd.DataFrame(dicts).head())
    
    topics = ["business","sports","technology","entertainment"]
    dicts = get_inshorts_articles(topics)
    print(pd.DataFrame(dicts).head())
    
    