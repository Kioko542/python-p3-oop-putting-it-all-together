#!/usr/bin/env python3


class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count
        self.current_page = 1

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self.current_page += 1
        if self.current_page > self.page_count:
            print("Reached the end of the book!")

        