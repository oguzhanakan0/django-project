import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException


def initiate_driver(driver_path):
	driver = webdriver.Firefox(executable_path=driver_path)
	driver.implicitly_wait(5)
	return driver


def _element_found(driver, locator):
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
		error = 0
	except:
		error = 1


class BaseScrape:
	def __init__(self, driver, url, title, not_found_check, visible_check_locator,
				 defined_campaigns=['Standard_campaign']):
		self.defined_campaigns = defined_campaigns
		self.final_campaigns = defined_campaigns
		self.driver = driver
		self.url = url
		self.title = title
		self.not_found_check = not_found_check
		self.visible_check_locator = visible_check_locator

		self.scrape_status = -1
		self.alert_log = []

		self.result = pd.DataFrame(columns=['campaign', 'principal', 'tenure', 'interest'])

	def _go_to_page(self):
		try:
			self.driver.get(self.url)
		except WebDriverException:
			self.alert_log.append(2)
		except:
			self.alert_log.append(1)

	def _control_page(self, ):
		try:
			WebDriverWait(self.driver, 10).until(EC.title_contains(self.title))
		except TimeoutException:
			if eval(self.not_found_check):
				self.alert_log.append(3)
			else:
				self.alert_log.append(1)
		except:
			self.alert_log.append(1)

		try:
			WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.visible_check_locator))
		except:
			self.alert_log.append(4)

	def _control_product_locator(self):
		pass

	def _set_product(self):
		pass

	def page_product_step(self):
		for met in ['_go_to_page', '_control_page', '_control_product_locator', '_set_product']:
			if list(filter(lambda x: x not in [7, 8], self.alert_log)) == []:
				print('Running ', met)
				self.__getattribute__(met)()

	def _control_campaign_locator(self):
		pass

	def _create_available_campaigns(self):
		pass

	def _control_campaign_process(self):
		pass

	def campaign_control_step(self):
		for met in ['_control_campaign_locator', '_create_available_campaigns', '_control_campaign_process']:
			if list(filter(lambda x: x not in [7, 8], self.alert_log)) == []:
				print('Running ', met)
				self.__getattribute__(met)()

	def _control_principal_tenure_locator(self, principal_locator, tenure_locator):
		if _element_found(self.driver, principal_locator):
			self.alert_log.append(10)
		if _element_found(self.driver, tenure_locator):
			self.alert_log.append(10)

	def _control_interest_locator(self, interest_locator):
		if _element_found(self.driver, interest_locator):
			self.alert_log.append(11)

	def _control_submit_locator(self, submit_locator):
		pass

	def interest_control_step(self, principal_locator, tenure_locator, interest_locator, submit_locator=None):
		inputs = [[principal_locator, tenure_locator], [interest_locator], [submit_locator]]
		i = 0
		for met in ['_control_principal_tenure_locator', '_control_interest_locator', '_control_submit_locator']:
			if list(filter(lambda x: x not in [7, 8], self.alert_log)) == []:
				print('Running ', met)
				self.__getattribute__(met)(*inputs[i])
			i += 1

	def control_scrape_initiation(self):
		if list(filter(lambda x: x not in [7, 8], self.alert_log)) == []:
			self.scrape_status = 0

	def _set_campaign(self, campaign):
		pass

	def _set_principal(self, principal):
		pass

	def _set_tenure(self, tenure):
		pass

	def _read_interest(self):
		pass

	def scrape(self, principal_list, tenure_list):
		print('Running scrape')
		if self.scrape_status == 0:
			try:
				i = 0
				for campaign in self.final_campaigns:
					self._set_campaign(campaign)
					for principal in principal_list:
						self._set_principal(principal)
						for tenure in tenure_list:
							self._set_tenure(tenure)
							interest = self._read_interest()
							self.result.loc[i] = [campaign, principal, tenure, interest]
							i += 1
				self.scrape_status = 1
			except:
				self.scrape_status = 2
		else:
			self.scrape_status = 0


class CampaignControl:
	def __init__(self, defined_campaigns, available_campaigns):
		self.defined_campaigns = defined_campaigns
		self.available_campaigns = available_campaigns
		self.campaign_alert_log = []

	def campaign_control(self):
		defined_set = set(self.defined_campaigns)
		available_set = set(self.available_campaigns)

		self.final_campaigns = list(defined_set.intersection(available_set))

		if defined_set.difference(available_set): self.campaign_alert_log.append(8)
		if available_set.difference(defined_set): self.campaign_alert_log.append(7)
		if not defined_set.intersection(available_set): self.campaign_alert_log.append(9)

