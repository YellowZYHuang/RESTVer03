from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.pagination import LimitOffsetPagination
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
    DefaultOrderingFilterBackend,
)

from Search.documents import Invoices2020M01Doc
from Search.serializers import Invoices2020M01DocSerializer


class Invoices2020DocM01View(DocumentViewSet):
    document = Invoices2020M01Doc
    serializer_class = Invoices2020M01DocSerializer
    pagination_class = LimitOffsetPagination

    # lookup_field = 'RetailerNo'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Define search fields
    search_fields = (
        'Date',
        'Amount',
    )
    # Define filtering fields
    filter_fields = {
        'Date': None,
        'Amount': None,
    }
    # Define ordering fields
    ordering_fields = {
        'Date': None,
        'Amount': None,
    }
    # Specify default ordering
    ordering = ('Date', 'Amount',)
