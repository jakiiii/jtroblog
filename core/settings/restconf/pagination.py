from rest_framework import pagination


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 20
    limit_query_param = 'lim'
