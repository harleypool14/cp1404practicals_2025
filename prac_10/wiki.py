import wikipedia

def main():
    search_title = input("Enter page title: ")
    while search_title:
        try:
            page = wikipedia.page(search_title, autosuggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)