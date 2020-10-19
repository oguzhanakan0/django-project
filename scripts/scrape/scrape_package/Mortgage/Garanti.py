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


class Garanti(BaseScrape):

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
		interest =  self.driver.find_elements_by_xpath(
			'//ul[@id="calcResultCreditAmount"]//li[@class="info-block nth-child-8"]/span[@class="green-bold-medium"]')[
			0].text
		interest = interest.replace('%', '').replace(',', '.').strip()
		return float(interest)

def run_scrape(driver, principal_list, tenure_list, campaign_list=None):
	print('Running Garanti')
	gr = Garanti(
		driver,
		'https://www.garantibbva.com.tr/tr/bireysel/mortgage/konut_kredisi_hesaplama.page',
		'Konut Kredisi Hesaplama (Mortgage - Ev) | Garanti BBVA',
		''' 'Üzgünüz, Aradığınız Sayfayı Bulamadık.' in [i.text for i in self.driver.find_elements_by_tag_name('h1')]''',
		('id', 'creditAmountSlider-slider')
	)
	gr.page_product_step()
	gr.campaign_control_step()
	gr.interest_control_step(
		('id', 'amountInteger'),
		('id', 'maturity'),
		('xpath',
		 '//ul[@id="calcResultCreditAmount"]//li[@class="info-block nth-child-8"]/span[@class="green-bold-medium')
	)
	gr.control_scrape_initiation()
	gr.scrape(principal_list, tenure_list)
	return gr.alert_log, gr.scrape_status, gr.result