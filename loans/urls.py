from django.urls import path
from django.urls import include, re_path
# from .views import requery_loan_detail

from . import views

urlpatterns = [
    # path('', views.loan_list, name='loan_list'),
    path('sorgu/kredi-tipi=<loan_type>&tutar=<principal>&vade=<tenure>/', views.loan_query, name='loan_list'),
    # path('loan_detail', views.loan_detail, name='loan_detail'),
    path('detay/kredi-adi=<slug>&tutar=<principal>&vade=<tenure>/', views.loan_detail, name='loan_detail'), # loan detail page with slug name 
    path('detay/kredi-tipi=<loan_type>&banka-adi=<bank_slug>&tutar=<principal>&vade=<tenure>/', views.loan_detail_b, name='loan_detail_b'), # loan detail page with bank name
    # path('ajax/requery-loan-detail/', requery_loan_detail, name='ajax_requery_loan_detail'),  # <-- this one here
]