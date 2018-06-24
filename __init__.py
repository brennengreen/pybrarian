try:
    import wikipedia as wiki
except ImportError:
    print("Error importing 'wikipedia', no module exists")


class Book:
    def __init__(self, title, pages):
        self.book_title = title
        self.wiki_page = wiki.WikipediaPage(self.book_title)
        try:
            self.page_count = pages
        except:
            print("Page count not supplied, searching...")
        self.book_summary = wiki.summary(self.book_title)

    def get_book_pages(self):
        page_html = self.wiki_page.html()
        page_count = page_html.count("pages=")
        if page_count >= 1:
            index = page_html.find("pages=")
            count_index = index + len("pages") + 1
            count = None
            for i in range(4):
                next_index = count_index + i
                try:
                    int(page_html[next_index])
                except ValueError:
                    self.page_count = count
                    return count

                if count == None:
                    count = page_html[next_index]
                else:
                    count = count + page_html[next_index]

    def get_book_summary(self):
        return self.book_summary

    def getBookInfo(self):
        msg = "The title of this book is {0}, and there are {1} pages to read!"
        return (msg.format(self.book_title, self.page_count))

tfios = Book("The Fault in Our Stars", None)
print(tfios.get_book_pages())