from django_elasticsearch_dsl import Index
from django_elasticsearch_dsl.documents import DocType

from Search.models import Invoices2020M01

invoices2020 = Index('invoices2020')


@invoices2020.doc_type
class Invoices2020M01Doc(DocType):
    class Django:
        model = Invoices2020M01
        fields = [
            'Date'
            , 'Amount'
        ]
