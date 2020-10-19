from scrape_package import scrape_tools
from scrape_package.scrape_tools import BaseScrape
from scrape_package.scrape_tools import CampaignControl

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import pandas as pd
import time


class Garanti(BaseScrape):

	def _contol_campaign_locator(self):
		if scrape_tools._element_found(self.driver, ('id', 'campaignsForCredit')):
			self.alert_log.append(6)

	def _create_available_campaigns(self):
		campaign_element = self.driver.find_element_by_id('campaignsForCredit')
		menu = Select(campaign_element)
		self.available_campaigns = [i.text for i in menu.options]

	def _control_campaign_process(self):
		CampContObj = CampaignControl(self.defined_campaigns, self.available_campaigns)
		CampContObj.campaign_control()
		self.final_campaigns = CampContObj.final_campaigns
		self.alert_log = self.alert_log + CampContObj.campaign_alert_log

	def _set_campaign(self, campaign):
		campaign_element = self.driver.find_element_by_id('campaignsForCredit')
		menu = Select(campaign_element)
		time.sleep(1)
		menu.select_by_visible_text(campaign)

	def _set_principal(self, principal):
		principal_element = self.driver.find_element_by_id('amountInteger')
		principal_element.clear()
		time.sleep(1)
		principal_element.send_keys(principal)
		time.sleep(1)

	def _set_tenure(self, tenure):
		tenure_element = self.driver.find_element_by_id('maturity')
		tenure_element.clear()
		time.sleep(1)
		tenure_element.send_keys(tenure)
		time.sleep(1)

	def _read_interest(self):
		interest = self.driver.find_elements_by_xpath(
			'//div[@id="calcResultCreditAmount"]//li[@class="info-block nth-child-3"]/span')[1].text
		interest = interest.replace('%', '').replace(',', '.').strip()
		return float(interest)



def run_scrape(driver, principal_list, tenure_list, campaign_list=None):
	print('Running Garanti')
	gr = Garanti(
		driver,
		'https://www.garantibbva.com.tr/tr/bireysel/krediler/tasit-arac-kredisi-hesaplama.page',
		'Taşıt Kredisi Hesaplama ve Başvuru | Garanti BBVA',
		''' 'Üzgünüz, Aradığınız Sayfayı Bulamadık.' in [i.text for i in self.driver.find_elements_by_tag_name('h1')]''',
		('id', 'creditAmountSlider-slider'),
		campaign_list
	)
	gr.page_product_step()
	gr.campaign_control_step()
	gr.interest_control_step(
		('id', 'amountInteger'),
		('id', 'maturity'),
		('xpath', '//div[@id="calcResultCreditAmount"]//li[@class="info-block nth-child-3"]/span')
	)
	gr.control_scrape_initiation()
	gr.scrape(principal_list, tenure_list)
	return gr.alert_log, gr.scrape_status, gr.result