from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from Search.documents import Invoices2020M01Doc


class Invoices2020M01DocSerializer(DocumentSerializer):
    class Meta(object):
        document = Invoices2020M01Doc
        fields = (
            'Date',
            'Amount',
        )
