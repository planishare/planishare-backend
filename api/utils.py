from rest_framework.pagination import PageNumberPagination

# Like PageNumberPagination but can recieve a page size
class CustomPageNumberPagination(PageNumberPagination):
    def __init__(self, page_size=10):
        self.page_size = page_size
    
    page_size_query_param = 'page_size'