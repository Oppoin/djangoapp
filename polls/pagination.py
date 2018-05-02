from rest_framework_json_api.pagination import PageNumberPagination as BasePageNumberPagination


class PageNumberPagination(BasePageNumberPagination):

    def get_paginated_response(self, data):
        if isinstance(data, dict):
            data = data.get('results', data)
        return super().get_paginated_response(data)
