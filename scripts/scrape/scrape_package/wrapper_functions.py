import pandas as pd
import importlib

def run_bank(
        driver, #selenium Webdriver
        product_name, #string (GPL,Mortgage,CarLoan)
        class_name, #string (Garanti, YapiKredi etc.)
        campaign_list, #list
        principal_list, #list
        tenure_list #list
):
    scrp = importlib.import_module('scrape_package.{}.{}'.format(product_name, class_name))
    return scrp.run_scrape(driver, principal_list, tenure_list, campaign_list)


def run_product(
        driver, #selenium Webdriver
        product_id, #integer
        products, #dictionary
        banks, #list
        classes, #dictionary
        campaigns, #dictionary
        principal_list, #list
        tenure_list #list
):

    # empty result tables
    results = pd.DataFrame(columns=['product', 'bank', 'campaign', 'principal', 'tenure', 'interest'])
    alerts = pd.DataFrame(columns=['product', 'bank', 'alert_id'])
    scrape_results = pd.DataFrame(columns=['product', 'bank', 'scrape_status'])

    # loop on banks
    for bank in banks:
        class_name = classes[bank]
        campaign_list = campaigns[bank]
        product_name = products[product_id]
        bank_alert_log, bank_status, bank_results = run_bank(driver, product_name, class_name, campaign_list, principal_list, tenure_list)

        bank_alert_log = pd.DataFrame(bank_alert_log, columns=['alert_id'])
        bank_alert_log['product'] = product_id
        bank_alert_log['bank'] = bank
        bank_alert_log = bank_alert_log[['product', 'bank', 'alert_id']]
        alerts = alerts.append(bank_alert_log)

        bank_status = pd.DataFrame([[product_id, bank, bank_status]], columns=['product', 'bank', 'scrape_status'])
        scrape_results = scrape_results.append(bank_status)

        bank_results['product'] = product_id
        bank_results['bank'] = bank
        bank_results = bank_results[['product', 'bank', 'campaign', 'principal', 'tenure', 'interest']]
        results = results.append(bank_results)

        for df in [results, alerts, scrape_results]:
            df.reset_index(inplace=True, drop=True)

    return results, alerts, scrape_results


