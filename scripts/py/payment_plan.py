import pandas as pd

def payment_plan(amount, maturity, interest, bsmv, kkdf):
    total_interest = interest + interest * kkdf + interest * bsmv
    monthly_payment = (total_interest * amount) / (1 - (1 + total_interest) ** (-1 * maturity))
    payment_plan = pd.DataFrame(index=range(maturity), columns=['month','monthly_pay','principal_before','principal_paid','interest_paid','kkdf','bsmv','principal_left'])

    for i in range(maturity):
        if i == 0:
            principal_before = amount
        else:
            principal_before = payment_plan.loc[i-1, 'principal_left']

        interest_paid = principal_before * interest
        kkdf_paid = interest_paid * kkdf
        bsmv_paid = interest_paid * bsmv
        principal_paid = monthly_payment - interest_paid - kkdf_paid - bsmv_paid
        principal_left = principal_before - principal_paid

        payment_plan.loc[i] = [i+1,monthly_payment, principal_before, principal_paid, interest_paid, kkdf_paid, bsmv_paid, principal_left]
        payment_plan = payment_plan.astype('float')

    payment_plan.drop('principal_before', axis=1, inplace=True)
    payment_plan = payment_plan.round(0)
    payment_plan.iloc[-1,-1]=0
    payment_plan.columns=['Ay','Taksit','Anapara','Faiz','KKDF','BSMV','Kalan Ödeme']
    return payment_plan