import pybrarian as pyb

#The constructor takes two parameters, title and page count
the_alchemist = pyb.Book("The Alchemist", 163)

#You can also use None as the parameter for page count if you do not know it, pybrarian will find it for you
catcher = pyb.Book("Catcher in the Rye", None)

#If you want to give the user a summary of the book you can use the get_book_summary method
print(the_alchemist.get_book_summary())
"""
Output:
The Alchemist (Portuguese: O Alquimista) is a novel by Brazilian author Paulo Coelho which was first published in 1988. 
Originally written in Portuguese, it became an international bestseller translated into some 70 languages as of 2016. An allegorical novel, 
The Alchemist follows a young Andalusian shepherd in his journey to the pyramids of Egypt, after having a recurring dream of finding a treasure there.
Over the years there have been film and theatrical adaptations of the work and musical interpretations of it.
"""

#Although all methods in pybrarian will do so for you, you can also find the pages of a book if it weren't given as a parameter
print(catcher.get_book_pages())
"""
Output:
277
"""

#get_book_info will give the user a simple one liner about the book
print(the_alchemist.get_book_info())
"""
Output:
The title of this book is The Alchemist, and there are 163 pages to read!
"""
