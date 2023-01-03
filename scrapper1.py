import requests, re
from bs4 import BeautifulSoup


def search_text(text,term):
    results = []
    term = str(term).lower()
    try:
        for line in text.split(". "):
            if re.search(term,line.lower()):
                results.append(line)
    except Exception as ex:
        print(f"The following error occurred while searching the text: '{ex}'")
    return results


def scrap(link,term):
    try:
        result = requests.get(link)

        soup = BeautifulSoup(result.text, "html.parser")
        soup.prettify()

        print(f"Searching {soup.title.string}<{link}>")

        text = soup.text

        search_results = search_text(text,term)
        return search_results
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    print("Welcome to Ugo's Web Scrapper!\n\n")
    while True:
        url = input("Please provide the url you want to scrape: ")
        search_term = input("What are you looking for in this link? ")
        print(scrap(url,search_term))
