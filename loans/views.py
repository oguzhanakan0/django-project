from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Loan, LoanRequest, Principal, Bank, LoanType
from .forms import LoanRequestForm
from django.urls import reverse
from scripts.py.payment_plan import payment_plan
import pandas as pd
import pprint

def calculate_installment(principal, tenure, interest, bsmv=0.05, kkdf=0.15):
	total_interest = interest + interest * kkdf + interest * bsmv
	installment = (total_interest * principal) / (1 - (1 + total_interest) ** (-1 * tenure))
	return round(installment,2)

def calculate_loan_details(loan, principal, tenure):
	loan.principal = Principal(principal=principal)
	loan.installment = calculate_installment(principal, tenure, loan.interest)
	loan.allocation_fee = round(principal*0.005,2)
	loan.total_payment = round(loan.installment * tenure +  loan.allocation_fee,2)
	loan.total_interest = round(loan.total_payment - principal - loan.allocation_fee,2)
	# loan.interest_str = "{:.2%}".format(loan.interest)
	return loan

# Create your views here.
def loan_query(request, loan_type, principal, tenure):
	if (request.method == "GET"):
		loans = Loan.objects.filter(loan_type=loan_type,tenure__gte=tenure,principal__gte=principal).order_by('bank','tenure','principal').distinct('bank')
		loans = Loan.objects.filter(id__in=loans).order_by('interest')
		available_tenures = LoanType.objects.get(loan_type=loan_type).tenures.all().exclude(tenure=0).order_by('tenure')
		print("available_tenures:")
		print(available_tenures)
		for loan in loans:
			loan = calculate_loan_details(loan, int(principal), int(tenure))
		return render(request, 'loans/loan_query_page.html', {
			'loans':loans,
			'principal':principal,
			'tenure':tenure,
			'available_tenures':available_tenures,
			'at_least_one_loan':True if len(loans)>0 else False, 
			'form':LoanRequestForm(initial={'principal': principal,'tenure':tenure})})
	elif (request.method == "POST"):
		print(request.POST)
		if ("detail-button" in request.POST):
			request_post = request.POST.copy()
			return redirect_to_loan_detail_page(request_post)
			

def loan_detail(request, slug, principal, tenure):
	print("== LOAN.VIEWS.LOAN_DETAIL ==")
	print("== rendering loan detail ==")
	if (request.method == "GET"):
		print("slug: "+str(slug))
		print("principal: "+str(principal))
		print("tenure: "+str(tenure))
		loan = Loan.objects.filter(tenure__gte=tenure,principal__gte=principal,slug=slug).order_by('tenure','principal').first()
		print("== query result ==")
		print("returned type of: "+str(type(loan)))
		
		loan = calculate_loan_details(loan, int(principal), int(tenure))

		loan.payment_plan = payment_plan(amount=int(principal), maturity=int(tenure), interest=0.05, bsmv=0.005, kkdf=0.005)
		loan.payment_plan.nrows = loan.payment_plan.shape[0]


		return render(request, 'loans/loan_detail_page.html', {
			'loan': loan,
			'principal':principal,
			'tenure':tenure,
			'form':LoanRequestForm(initial={'principal': principal,'tenure':tenure})
			})
	elif (request.method == "POST"):
		if ("detail-button" in request.POST):
			request_post = request.POST.copy()
			print(request_post)
			return redirect_to_loan_detail_page(request_post)

def loan_detail_b(request, loan_type, bank_slug, principal, tenure):
	print("== LOAN.VIEWS.LOAN_DETAIL_B ==")
	print("== rendering loan detail ==")
	if (request.method == "GET"):
		print("bank_slug: "+str(bank_slug))
		print("principal: "+str(principal))
		print("tenure: "+str(tenure))
		loan = Loan.objects.filter(tenure__gte=tenure,principal__gte=principal,bank=Bank.objects.get(slug=bank_slug),loan_type=loan_type).order_by('tenure','principal').first()
		print("== query result ==")
		print("returned type of: "+str(type(loan)))
		
		loan = calculate_loan_details(loan, int(principal), int(tenure))

		loan.payment_plan = payment_plan(amount=int(principal), maturity=int(tenure), interest=0.05, bsmv=0.005, kkdf=0.005)
		loan.payment_plan.nrows = loan.payment_plan.shape[0]

		return render(request, 'loans/loan_detail_page.html', {
			'loan': loan,
			'principal':principal,
			'tenure':tenure,
			'form':LoanRequestForm(initial={'principal': principal,'tenure':tenure})
			})

	elif (request.method == "POST"):
		if ("detail-button" in request.POST):
			request_post = request.POST.copy()
			print(request_post)
			return redirect_to_loan_detail_page(request_post)


def redirect_to_loan_detail_page(request_post):
	
	request_post['principal'] = request_post['principal'].replace(',','')
	redirect_to = reverse('loan_detail',
				kwargs={
					'slug':request_post.get('slug'),
					'principal':request_post.get('principal'),
					'tenure':request_post.get('tenure'),
				})
	print('hereee')
	return HttpResponseRedirect(redirect_to)