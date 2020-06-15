from rest_framework.routers import DefaultRouter

from Search.views import Invoices2020DocM01View

SearchRouter = DefaultRouter()
SearchRouter.register('invoices2020/m01', Invoices2020DocM01View, basename='invoices2020m01')
