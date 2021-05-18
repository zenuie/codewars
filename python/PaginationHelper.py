# TODO: complete this class
import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if self.collection[-1] % self.items_per_page != 0:
            return (self.collection[-1] // self.items_per_page) + 1
        else:
            return self.collection[-1] // self.items_per_page

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < (self.collection[-1] // self.items_per_page):
            return self.items_per_page
        elif page_index == (self.collection[-1] // self.items_per_page):
            return self.collection[-1] - self.items_per_page * page_index
        else:
            return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range

    def page_index(self, item_index):
        if item_index in self.collection[1:-1] and item_index != 0:
            return math.ceil(item_index / self.items_per_page) - 1
        elif item_index == 0 and self.collection:
            return 0
        else:
            return -1


collection = range(1, 25)
helper = PaginationHelper(collection, 10)
# helper.item_count()
helper.page_item_count(3)
# helper.page_index(0)
