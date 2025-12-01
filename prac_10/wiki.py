import wikipedia


def main():
    search_title = input("Enter page title: ")
    while search_title:
        try:
            page = wikipedia.page(search_title, autosuggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.Error as e:
            print(f"We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.PageError:
            print(f"Page id \"{search_title}\" does not match any pages. Try another id!")
        print()
        search_title = input("Enter page title: ")
    print("Thank you.")


if __name__ == "__main__":
    main()
