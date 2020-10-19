from django.db import models
from loans.models import Bank, LoanType, Program
import uuid
from django.contrib import auth

# Create your models here.
class ClassName(models.Model):
	id             = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	bank           = models.ForeignKey(Bank, on_delete=models.PROTECT, db_column = 'bank_id', to_field = 'id')
	class_name     = models.CharField(max_length = 100, unique=True)

	def __str__(self):
		return self.class_name

class ProductCampaign(models.Model):
	id             = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	bank           = models.ForeignKey(Bank, on_delete=models.PROTECT, db_column = 'bank_id', to_field = 'id')
	loan_type      = models.ForeignKey(LoanType, on_delete=models.PROTECT, db_column = 'loan_type', to_field = 'loan_type')
	campaign_name  = models.CharField(max_length = 100)
	upd_program    = models.ForeignKey(Program, on_delete=models.PROTECT, db_column = '_program', to_field= 'program')
	upd_time       = models.DateTimeField(auto_now=True, db_column = '_upd_time')
	upd_user       = models.ForeignKey(auth.get_user_model(), on_delete=models.PROTECT, db_column = '_user', to_field= 'username')

	def __str__(self):
		return str(self.id)+"-"+self.campaign_name

class AlertType(models.Model):
	id                 = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	alert_type         = models.CharField(max_length = 100, unique=True)

	def __str__(self):
		return self.alert_type

class Result(models.Model):
	id             = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	result         = models.CharField(max_length = 10, unique=True)

	def __str__(self):
		return self.result

class AlertLog(models.Model):
	id                 = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	alert_type         = models.ForeignKey(AlertType, on_delete=models.PROTECT, db_column = 'alert_type', to_field = 'alert_type')
	bank               = models.ForeignKey(Bank, on_delete=models.PROTECT, db_column = 'bank_id', to_field = 'id')
	loan_type          = models.ForeignKey(LoanType, on_delete=models.PROTECT, db_column = 'loan_type', to_field = 'loan_type')
	upd_program        = models.ForeignKey(Program, on_delete=models.PROTECT, db_column = '_program', to_field= 'program')
	upd_time           = models.DateTimeField(auto_now=True, db_column = '_upd_time')
	upd_user           = models.ForeignKey(auth.get_user_model(), on_delete=models.PROTECT, db_column = '_user', to_field= 'username')

class ScrapeLog(models.Model):
	id                 = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	bank               = models.ForeignKey(Bank, on_delete=models.PROTECT, db_column = 'bank_id', to_field = 'id')
	loan_type          = models.ForeignKey(LoanType, on_delete=models.PROTECT, db_column = 'loan_type', to_field = 'loan_type')
	result			   = models.ForeignKey(Result, on_delete=models.PROTECT, db_column = 'result', to_field = 'result')
	upd_program        = models.ForeignKey(Program, on_delete=models.PROTECT, db_column = '_program', to_field= 'program')
	upd_time           = models.DateTimeField(auto_now=True, db_column = '_upd_time')
	upd_user           = models.ForeignKey(auth.get_user_model(), on_delete=models.PROTECT, db_column = '_user', to_field= 'username')