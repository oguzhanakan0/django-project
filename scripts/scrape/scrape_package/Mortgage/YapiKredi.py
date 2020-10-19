from scrape_package import scrape_tools
from scrape_package.scrape_tools import BaseScrape
from scrape_package.scrape_tools import CampaignControl

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time

class YapiKredi(BaseScrape):

    def _control_product_locator(self):
        if scrape_tools._element_found(self.driver, ('id','select2-ctl00_ContentPlaceHolder1_ddlClientType-container')):
            self.alert_log.append(5)
        if scrape_tools._element_found(self.driver, ('id', 'select2-ctl00_ContentPlaceHolder1_ddlCreditType-container')):
            self.alert_log.append(5)

    def _set_product(self):
        self.driver.find_element_by_id('select2-ctl00_ContentPlaceHolder1_ddlClientType-container').click()
        customer_list = self.driver.find_elements_by_xpath('//ul[@id="select2-ctl00_ContentPlaceHolder1_ddlClientType-results"]/li')
        if 'Bireysel' in [x.text for x in customer_list]:
            idx = [x.text for x in customer_list].index('Bireysel')
            customer_list[idx].click()
        else:
            self.alert_log.append(5)

        self.driver.find_element_by_id('select2-ctl00_ContentPlaceHolder1_ddlCreditType-container').click()
        product_list = self.driver.find_elements_by_xpath('//ul[@id="select2-ctl00_ContentPlaceHolder1_ddlCreditType-results"]/li')
        if 'Konut' in [x.text for x in product_list]:
            idx = [x.text for x in product_list].index('Konut')
            product_list[idx].click()
        else:
            self.alert_log.append(5)

    def _control_campaign_locator(self):
        if scrape_tools._element_found(self.driver, ('id','select2-ctl00_ContentPlaceHolder1_ddlCreditCategory-container')):
            self.alert_log.append(6)

    def _create_available_campaigns(self,):
        self.driver.find_element_by_id('select2-ctl00_ContentPlaceHolder1_ddlCreditCategory-container').click()
        items = self.driver.find_elements_by_xpath('//ul[@id="select2-ctl00_ContentPlaceHolder1_ddlCreditCategory-results"]/li')
        self.available_campaigns = [i.text for i in items]
        if 'Seçiniz' in self.available_campaigns:
            self.available_campaigns.remove('Seçiniz')
        self.driver.find_element_by_id('select2-ctl00_ContentPlaceHolder1_ddlCreditCategory-container').click()

    def _control_campaign_process(self):
        CampContObj = CampaignControl(self.defined_campaigns, self.available_campaigns)
        CampContObj.campaign_control()
        self.final_campaigns = CampContObj.final_campaigns
        self.alert_log = self.alert_log + CampContObj.campaign_alert_log

    def _control_submit_locator(self, submit_locator):
        scrape_tools._element_found(self.driver, submit_locator)

    def _set_campaign(self, campaign):
        self.page_product_step()
        self.driver.find_element_by_id('select2-ctl00_ContentPlaceHolder1_ddlCreditCategory-container').click()
        campaign_element = self.driver.find_element_by_xpath("//*[contains(@class, 'select2-search__field')]")
        campaign_element.send_keys(campaign)
        campaign_element.send_keys(Keys.ENTER)
        time.sleep(1)

    def _set_principal(self, principal):
        principal_element = self.driver.find_element_by_id('slider-amount-input')
        principal_element.clear()
        principal_element.send_keys(principal)

    def _set_tenure(self, tenure):
        tenure_element = self.driver.find_element_by_id('slider-month-input')
        tenure_element.clear()
        tenure_element.send_keys(tenure)

    def _read_interest(self):
        self.driver.find_element_by_id('btnCalculateCreditType').click()
        time.sleep(1)
        interest = self.driver.find_element_by_id('creditCalculateResult_Rate').text
        interest = interest.replace('%', '').replace(',', '.').strip()
        return float(interest)

def run_scrape(driver, principal_list, tenure_list, campaign_list=None):
    print('Running YapiKredi')
    yk = YapiKredi(
        driver,
        'https://www.yapikredi.com.tr/bireysel-bankacilik/hesaplama-araclari/kredi-hesaplama',
        'Kredi Hesaplama | Hesaplama Araçları | Yapı Kredi',
        ''' 'Sayfa Bulunamadı | Yapı Kredi' == self.driver.title''',
        ('id','select2-ctl00_ContentPlaceHolder1_ddlClientType-container'),
        campaign_list
    )
    yk.page_product_step()
    yk.campaign_control_step()
    yk.interest_control_step(
        ('id', 'slider-amount-input'),
        ('id', 'slider-month-input'),
        ('id','creditCalculateResult_Rate'),
        ('id','btnCalculateCreditType')
    )
    yk.control_scrape_initiation()
    yk.scrape(principal_list, tenure_list)
    return yk.alert_log, yk.scrape_status, yk.result