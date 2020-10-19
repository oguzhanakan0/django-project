from scrape_package.scrape_tools import initiate_driver
from scrape_package.wrapper_functions import run_bank, run_product
import datetime

FFdriver = initiate_driver('D:\hook\scripts\scrape\geckodriver.exe')

'''
a,b,c = run_bank(
        FFdriver, #selenium Webdriver
        'CarLoan', #string (GPL,Mortgage,CarLoan)
        'Garanti', #string (Garanti, YapiKredi etc.)
        ['das','aaaaa'], #list
        [10000,20000], #list
        [12,24] #list
)

'''

a,b,c =  run_product(
        FFdriver, #selenium Webdriver
        3, #integer
		{1:'GPL',2:'Mortgage',3:'CarLoan'}, #dictionary
		[1,2], #list
		{1:'Garanti',2:'YapiKredi'}, #dictionary
		{1:['0 KM DİJİTAL TAŞIT KREDİSİ','MİNOTO 0 KM TAŞIT KREDİSİ'], 2:['HONDA','HYUNDAİ','OPEL']}, #dictionary
        [100000,200000], #list
        [12,24] #list
)


a.to_pickle('data/'+datetime.date.today().strftime('%Y%m%d')+'_loans.pkl')
b.to_pickle('data/'+datetime.date.today().strftime('%Y%m%d')+'_alertlog.pkl')
c.to_pickle('data/'+datetime.date.today().strftime('%Y%m%d')+'_scrapelog.pkl')

print(a)
print(b)
print(c)