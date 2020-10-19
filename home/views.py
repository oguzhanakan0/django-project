from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from home.serializers import UserSerializer, GroupSerializer
from loans.models import Loan, LoanRequest, Tenure, LoanType, LoanSummary, LoanMatrixTable
from seo.models import FAQItem
from loans.forms import LoanRequestForm
from blog.models import BlogPage
from django.urls import reverse
from django.db.models import Min, Max
from datetime import date as dt
from datetime import datetime as dtm
from datetime import timedelta
from loans.views import calculate_loan_details, calculate_installment
import pprint

# Create your views here.
def index(request):
    """
    Homepage renderer function. Redirection depends on request type, otherwise will render default index page.
    << TODO: This function needs reorganization. >>
    # currently request.method == 'POST' is being redirected only to loan query page. We will change the condition to request.POST['request_type'] == xyz.
    """
    print("="*5,"SESSION","="*5)
    pprint.pprint(request.session.__dict__)
    if (request.method=='POST'):
        
        request_post = request.POST.copy()
        if request_post['request_type'] == "main_request":
            request_post['principal'] = request_post['principal'].replace(',','')
            print("=====REQUEST====")
            print(request_post)
            form = LoanRequestForm(request_post)
            if (form.is_valid()):
                form.save(loan_type=request_post['loan_type'])
                redirect_to = reverse('loan_list',
    				kwargs={
    					'principal':request_post['principal'],
    					'loan_type':request_post['loan_type'],
                        'tenure':request_post['tenure'],}
    			)
                print("redirecting to: "+redirect_to)
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponse('form is not valid')
        elif request_post['request_type'] == "request_from_loan_summary_table":
            request_post['principal'] = request_post['principal'].replace(',','')
            print("=====REQUEST====")
            print(request_post)
            # TODO: NEW FORM CREATE & SAVE METHOD IS MISSING
            redirect_to = reverse('loan_detail_b',
                kwargs={
                    'loan_type':request_post['loan_type'],
                    'bank_slug':request_post['bank_slug'],
                    'principal':request_post['principal'],
                    'loan_type':request_post['loan_type'],
                    'tenure':request_post['tenure'],}
            )
            print("redirecting to: "+redirect_to)
            return HttpResponseRedirect(redirect_to)

    else:
        # Homepage is rendered with the code below
        blogs = BlogPage.objects.all().order_by('-date')[:4]
        faqs  = FAQItem.objects.filter(relevant_to='homepage')
        today = dt.today() if dtm.now().hour>5 else dt.today()+timedelta(days=-1)
        
        loan_summary = LoanSummary.objects.filter(date=today).order_by('-min_interest')
        loan_summary_tenures = dict(zip([e.id for e in loan_summary],[list(e.tenures.all().order_by('tenure')) for e in loan_summary]))
        loan_matrix_tables = LoanMatrixTable.objects.filter(date=today)
        featured_loans = [calculate_loan_details(e, int(e.principal.principal), int(e.tenure.tenure)) for e in Loan.objects.filter(is_featured=True).order_by('feature_order')]
        for blog in blogs:
            blog.title = blog.title if len(blog.title)<=50 else blog.title[:50]+" ..."
            blog.intro = blog.intro[:100]+" ..."
        form = LoanRequestForm()
        print(form._meta.fields)
        return render(request, 'index.html', {'form':form, 'blogs':blogs, 'faqs':faqs, 'loan_summary':loan_summary, 'loan_summary_tenures':loan_summary_tenures, 'loan_matrix_tables':loan_matrix_tables, 'featured_loans':featured_loans})

def load_tenures(request):
    """
    Filters dropdown options depending on *request*. Tenure options may be filtered according to either "slug" of the loan or "loan_type"
    << TODO: This function needs reorganization. >>
    """
    if request.GET.get('slug')==None:
        loan_type = request.GET.get('loan_type')
        print('load_tenures running with loan_type = '+ str(loan_type))
        tenures = LoanType.objects.get(loan_type=loan_type).tenures.all().exclude(tenure=0).order_by('tenure')
    else:
        tenure_ids = Loan.objects.filter(slug=request.GET.get('slug')).values_list('tenure', flat=True)
        print("tenure_ids")
        print(tenure_ids)
        tenures = Tenure.objects.filter(tenure__in=set(tenure_ids))
    limits = tenures.aggregate(Min('tenure'),Max('tenure'))
    return render(request, 'hr/tenure_dropdown_list_options.html', {'tenures': tenures, 'min': limits['tenure__min'], 'max':limits['tenure__max'], 'initial_tenure':request.GET.get('initial_tenure')})

def get_principal_limits(request):
    print('get_principal_limits running')
    if request.GET.get('slug')==None:
        principals = Loan.objects.filter(loan_type=request.GET.get('loan_type')).aggregate(Min('principal'),Max('principal'))
    else:
        principals = Loan.objects.filter(slug=request.GET.get('slug')).aggregate(Min('principal'),Max('principal'))
    return render(request, 'loans/widgets/principal_input_widget.html', {'min':str(principals['principal__min']),'max': str(principals['principal__max']), 'initial_principal':request.GET.get('initial_principal')})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer