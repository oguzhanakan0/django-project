import pandas as pd

table_products = pd.DataFrame({'product_id':[1,2,3], 'product':['GPL','Mortgage','CarLoan']})
table_principal = pd.DataFrame({'product_id':sorted([1,2,3]*2),'principal':[20000,30000,100000,200000,50000,100000]})
table_tenure = pd.DataFrame({'product_id':sorted([1,2,3]*2),'tenure':[12,24,24,36,48,60]})
table_class = pd.DataFrame({'product_id':sorted([1,2,3]*2), 'bank_id':[1,2]*3, 'class_name':['Garanti','YapiKredi']*3})

table_campaigns = pd.DataFrame([
	[1, 2, 'BİREYSEL İHTİYAÇ KREDİSİ'],
	[1, 2, '3 AY ERTELEMELİ BAYRAM KREDİSİ'],
	[2, 2, 'KONUT KREDİSİ'],
	[3, 1, '0 KM DİJİTAL TAŞIT KREDİSİ'],
	[3, 1, 'MİNOTO 0 KM TAŞIT KREDİSİ'],
	[3, 1, 'ELEKTRİKLİ VE HYBRİD TAŞIT KREDİSİ'],
	[3, 1, 'MOTOSİKLET KREDİSİ'],
	[3, 2, 'ALFA ROMEO'],
	[3, 2, 'AUDİ'],
	[3, 2, 'BORUSAN'],
	[3, 2, 'CHEVROLET'],
	[3, 2, 'CİTROEN'],
	[3, 2, 'FİAT'],
	[3, 2, 'FORD'],
	[3, 2, 'HONDA'],
	[3, 2, 'HYUNDAİ'],
	[3, 2, 'ISUZU'],
	[3, 2, 'JAGUAR'],
	[3, 2, 'KIA'],
	[3, 2, 'MAN'],
	[3, 2, 'MAZDA'],
	[3, 2, 'MERCEDES'],
	[3, 2, 'NİSSAN'],
	[3, 2, 'OPEL'],
	[3, 2, 'PEUGEOT'],
	[3, 2, 'PRİMSİZ BAYİ'],
	[3, 2, 'RENAULT/DACİA'],
	[3, 2, 'SCANİA'],
	[3, 2, 'SEAT'],
	[3, 2, 'SKODA'],
	[3, 2, 'SUBARU'],
	[3, 2, 'SUZUKİ'],
	[3, 2, 'TATA'],
	[3, 2, 'TIRSAN'],
	[3, 2, 'TOYOTA'],
	[3, 2, 'VOLKSWAGEN'],
	[3, 2, 'VOLVO']
],
columns=['product_id','bank_id','campaign'])

table_alert_defs = pd.DataFrame([
	[1, 'Unknown error', 'STOP'],
	[2, 'Address not found', 'STOP'],
	[3, '404 in bank domain', 'STOP'],
	[4, 'Page control element not visible', 'STOP'],
	[5, 'Product element not found', 'STOP'],
	[6, 'Campaign element not found', 'STOP'],
	[7, 'Additional campaign', 'CONTINUE'],
	[8, 'Removed campaign', 'CONTINUE'],
	[9, 'No campaign left', 'STOP'],
	[10, 'Principal/tenure element not found', 'STOP'],
	[11, 'Interest element not found', 'STOP'],
	[12, 'Submit element not found', 'STOP']
],
columns=['alert_id', 'definition', 'action'])

for df in [table_products, table_principal, table_tenure, table_class, table_campaigns, table_alert_defs]:
	print(df)


