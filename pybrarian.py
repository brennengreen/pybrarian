import wikipedia as wiki


class Book:
    def __init__(self, title, pages):
        self.book_title = title
        self.page_count = pages
        
        
    def get_refined_title(self):
        search = wiki.search(self.book_title,1)
        refined_title = search[0]
        #This returns a pylint error saying refined_title is an instance of 'list', I have no clue why if you know please discord me @Drey#0001
        if refined_title.find("book") > -1 or refined_title.find("novel") > -1:
            self.book_title = refined_title
            print(refined_title)
            return refined_title
        else:
            search = wiki.search(self.book_title, 10)
            for i in range(len(search)):
                if search[i].find("book") > -1 or search[i].find("novel") > -1:
                    refined_title = search[i]
                    self.book_title = refined_title
                    print(refined_title)
                    return refined_title



    def get_book_pages(self):
        self.wiki_page = wiki.WikipediaPage(self.get_refined_title())
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
            return count

    def get_book_summary(self):
        self.book_summary = wiki.summary(self.get_refined_title())
        return self.book_summary

    def get_book_info(self):
        if self.page_count == None:
            self.get_book_pages()
        msg = "The title of this book is {0}, and there are {1} pages to read!"
        
        return (msg.format(self.book_title, self.page_count))
