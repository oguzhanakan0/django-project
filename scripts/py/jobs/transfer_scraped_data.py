"""
run script via:
> python manage.py shell < scripts/py/jobs/transfer_scraped_data.py >> scripts/scrape/data/data_transfer_log/data_transfer_log.txt 
"""
import pandas as pd
import os
import datetime
from unicode_tr import unicode_tr
from unicode_tr.extras import slugify
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from loans.models import *
from scraping.models import *
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
loans_data_path = 'scripts/scrape/data/'+datetime.date.today().strftime('%Y%m%d')+'_loans.pkl'
scrapelog_data_path = 'scripts/scrape/data/'+datetime.date.today().strftime('%Y%m%d')+'_scrapelog.pkl'
alertlog_data_path = 'scripts/scrape/data/'+datetime.date.today().strftime('%Y%m%d')+'_alertlog.pkl'
User = auth.get_user_model()
# ### Functions
def save_loan(row):
    loan = Loan()
    try:
        loan = Loan.objects.get(name=unicode_tr(row.campaign).title(),tenure=Tenure.objects.get(tenure=row.tenure),principal=Principal.objects.get(principal=row.principal))
        print(str(row.name)+": loan object exists with id="+str(loan.id)+". updating.")
        if not loan.interest == row.interest:
            loan.interest = row.interest
            loan.save()
        else:
            print(str(row.name)+": interest is still the same. passing update.")
    except ObjectDoesNotExist:
        print(str(row.name)+": loan object for name='"+unicode_tr(row.campaign).title()+"', tenure="+str(Tenure.objects.get(tenure=row.tenure))+", principal="+str(Principal.objects.get(principal=row.principal))+" does not exist. inserting.")
        try:
            loan.name        = unicode_tr(row.campaign).title()
            loan.principal   = Principal.objects.get(principal=row.principal)
            loan.tenure      = Tenure.objects.get(tenure=row.tenure)
            loan.loan_type   = LoanType.objects.get(loan_type=row.loan_type)
            loan.bank        = Bank.objects.get(id=row.bank)
            loan.slug        = slugify(str(loan.bank)+"-"+row.campaign)
            loan.interest    = row.interest
            loan.is_base     = False
            loan.upd_user    = User.objects.get(username='admin')
            loan.upd_program = Program.objects.get(program='python@transfer_scraped_data.py')
            loan.save()
            print(str(row.name)+": loan saved")
        except Exception as e:
            print(str(row.name)+": failed")
            print(str(row.name)+": "+str(e))
            
def save_scrapelog(row):
    scrapelog = ScrapeLog()
    try:
        scrapelog.bank        = Bank.objects.get(id=row.bank)
        scrapelog.loan_type   = LoanType.objects.get(loan_type=row['product'])
        scrapelog.result      = Result.objects.get(result=row.scrape_status)
        scrapelog.upd_user    = User.objects.get(username='admin')
        scrapelog.upd_program = Program.objects.get(program='python@transfer_scraped_data.py')
        scrapelog.save()
        print(str(row.name)+": scrapelog saved")
    except Exception as e:
        print(str(row.name)+": failed")
        print(str(row.name)+": "+str(e))
        
def save_alertlog(row):
    alertlog = AlertLog()
    try:
        alertlog.alert_type  = AlertType.objects.get(alert_type=row.alert_id)
        alertlog.bank        = Bank.objects.get(id=row.bank)
        alertlog.loan_type   = LoanType.objects.get(loan_type=row['product'])
        alertlog.upd_user    = User.objects.get(username='admin')
        alertlog.upd_program = Program.objects.get(program='python@transfer_scraped_data.py')
        alertlog.save()
        print(str(row.name)+": alertlog saved")
    except Exception as e:
        print(str(row.name)+": failed")
        print(str(row.name)+": "+str(e))

def summarize_loans(df):
    print("> shape = "+str(df.shape))
    print("> unique bank # = "+str(len(df.bank.unique())))

# ### Import Loans Data
s_loans = pd.read_pickle(loans_data_path)
s_scrapelog = pd.read_pickle(scrapelog_data_path)
s_alertlog = pd.read_pickle(alertlog_data_path)

# DELETE LATER
s_loans.bank.replace({1:'5fcfd4fa-b615-11ea-b6e6-d0c63746edcc',2:'5c43ee94-b615-11ea-bdde-d0c63746edcc'},inplace=True)
s_loans['loan_type'] = 'CAR'


s_scrapelog.bank.replace({1:'5fcfd4fa-b615-11ea-b6e6-d0c63746edcc',2:'5c43ee94-b615-11ea-bdde-d0c63746edcc'},inplace=True)
s_scrapelog['product'].replace({1:'GPL',2:'MOR',3:'CAR',4:'CA2'}, inplace=True)

s_alertlog.bank.replace({1:'5fcfd4fa-b615-11ea-b6e6-d0c63746edcc',2:'5c43ee94-b615-11ea-bdde-d0c63746edcc'},inplace=True)
s_alertlog['product'].replace({1:'GPL',2:'MOR',3:'CAR',4:'CA2'}, inplace=True)


# ### Save Loans
print("="*40)
print("> date: "+datetime.date.today().strftime('%Y-%m-%d'))
summarize_loans(s_loans)
print("> loans data insertion started.")
for row in s_loans.index:
    save_loan(s_loans.loc[row])
print("> loans data insertion finished.")
print("> scrapelog insertion started.")
for row in s_scrapelog.index:
    save_scrapelog(s_scrapelog.loc[row])
print("> scrapelog insertion finished.")
print("> alertlog insertion started.")
for row in s_alertlog.index:
    save_alertlog(s_alertlog.loc[row])
print("> alertlog insertion finished.")

