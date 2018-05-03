from rest_framework_json_api.pagination \
    import PageNumberPagination as BasePageNumberPagination
from django.conf import settings


class PageNumberPagination(BasePageNumberPagination):

    # because DJA uses page_size and DREST uses per_page
    # so we have to explicitly choose 1 over the other
    # and links and meta are displayed by DJA which in turn only work if
    # paginate_by is set
    page_size_query_param = settings.DYNAMIC_REST['PAGE_SIZE_QUERY_PARAM']

    def get_paginated_response(self, data):
        if isinstance(data, dict):
            data = data.get('results', data)
        return super().get_paginated_response(data)
