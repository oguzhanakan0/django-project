from django.db import models

from django.contrib import auth
from django.db.models import signals
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.postgres.fields.array import ArrayField
import uuid

"""
 ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗     ████████╗ █████╗ ██████╗ ██╗     ███████╗███████╗
 ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
 ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝       ██║   ███████║██████╔╝██║     █████╗  ███████╗
 ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝        ██║   ██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║
 ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║            ██║   ██║  ██║██████╔╝███████╗███████╗███████║
 ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝            ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝
"""

class LoanType(models.Model):
	id                 = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	loan_type          = models.CharField(max_length = 3, unique = True)
	loan_type_long     = models.CharField(max_length = 100, unique = True)
	description        = models.TextField()
	active             = models.BooleanField(default=True)

	def __str__(self):
		return self.loan_type_long
		
class Principal(models.Model):
	id                   = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	principal            = models.PositiveIntegerField(unique=True)
	active               = models.BooleanField(default=True)
	loan_types           = models.ManyToManyField(LoanType, related_name="principals", )

	def __str__(self):
	 return str(self.principal)

class InstallmentType(models.Model):
	id               = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	installment_type = models.CharField(max_length=40,unique=True)
	active           = models.BooleanField(default=True)

	def __str__(self):
		return str(self.installment_type)

class Program(models.Model):
	id               = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	program          = models.CharField(max_length=40,unique=True, default = "not_specified")
	active           = models.BooleanField(default=True)

	def __str__(self):
	 return str(self.program)

class Action(models.Model):
	id               = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	action           = models.CharField(max_length=40,unique=True, default = "INSERT")
	active           = models.BooleanField(default=True)

	def __str__(self):
	 return str(self.action)

from wagtail.images.models import Image

class Bank(models.Model):
	id                 = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name               = models.CharField(max_length = 40, unique = True)
	logo               = models.ForeignKey('wagtailimages.Image',null=True,on_delete=models.SET_NULL,related_name='+')
	icon               = models.ForeignKey('wagtailimages.Image',null=True,on_delete=models.SET_NULL,related_name='+')
	slug               = models.SlugField()
	active             = models.BooleanField(default=True)

	def __str__(self):
	 return self.name

class Insurance(models.Model):
	id                = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	insurance_type    = models.CharField(max_length = 40)
	description       = models.TextField()
	active            = models.BooleanField(default=True)

	def __str__(self):
	 return self.insurance_type

class Tenure(models.Model):
	id     = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	tenure = models.PositiveIntegerField(unique = True)
	active = models.BooleanField(default=True)
	loan_types = models.ManyToManyField(LoanType, related_name="tenures", )

	def convert_str(self):
		if (self.tenure >= 12 and self.tenure%12==0):
			return str(self.tenure) + " ay (" +str(int(self.tenure/12))+" yıl)"
		else:
			return str(self.tenure) + " ay"
	readable_tenure = property(convert_str)

	def __str__(self):
		return str(self.tenure)
"""
 
 ██████╗ ███████╗ ██████╗ ██╗   ██╗██╗      █████╗ ██████╗     ████████╗ █████╗ ██████╗ ██╗     ███████╗███████╗
 ██╔══██╗██╔════╝██╔════╝ ██║   ██║██║     ██╔══██╗██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
 ██████╔╝█████╗  ██║  ███╗██║   ██║██║     ███████║██████╔╝       ██║   ███████║██████╔╝██║     █████╗  ███████╗
 ██╔══██╗██╔══╝  ██║   ██║██║   ██║██║     ██╔══██║██╔══██╗       ██║   ██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║
 ██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗██║  ██║██║  ██║       ██║   ██║  ██║██████╔╝███████╗███████╗███████║
 ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝
                                                                                                                
 
"""

class LoanAbs(models.Model):
	# Foreign Keys
	loan_type          = models.ForeignKey(LoanType, on_delete=models.PROTECT, db_column = 'loan_type', to_field = 'loan_type')
	bank               = models.ForeignKey(Bank, on_delete=models.PROTECT, db_column = 'bank_name', to_field= 'name')
	tenure             = models.ForeignKey(Tenure, on_delete=models.PROTECT, db_column = 'tenure', to_field = 'tenure')
	principal	       = models.ForeignKey(Principal, on_delete=models.PROTECT, db_column = 'principal', to_field= 'principal')
	# Other Fields
	name               = models.CharField(max_length = 100)
	slug               = models.SlugField()
	description        = models.TextField()
	interest           = models.FloatField()
	is_base 		   = models.BooleanField(default=False)
	is_featured        = models.BooleanField(default=False)
	feature_order      = models.PositiveIntegerField(null=True,blank=True)
	# Log Fields
	upd_user           = models.ForeignKey(auth.get_user_model(), on_delete=models.PROTECT, db_column = '_user', to_field= 'username')
	upd_program        = models.ForeignKey(Program, on_delete=models.PROTECT, db_column = '_program', to_field= 'program')
	active             = models.BooleanField(default=True)

	class Meta:
		abstract = True

class Loan(LoanAbs):
	id            	   = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	upd_time           = models.DateTimeField(auto_now=True, db_column = '_upd_time')

	def save(self, *args, **kwargs):
		if self.loan_type not in self.tenure.loan_types.all():
			raise ValueError('Invalid Loan Type - Tenure combination.')
		else:
			super(Loan, self).save(*args, **kwargs)

	def __str__(self):
		return self.bank.name + "-" +str(self.loan_type) +"-"+self.name

	

class LinkAbs(models.Model):
	bank               = models.ForeignKey(Bank, on_delete=models.PROTECT, db_column = 'bank_name', to_field= 'name')
	url                = models.TextField()
	loan_type          = models.ForeignKey(LoanType, on_delete=models.CASCADE, db_column = 'loan_type', to_field = 'loan_type')
	upd_user           = models.ForeignKey(auth.get_user_model(), on_delete=models.PROTECT, db_column = '_user', to_field= 'username')
	upd_program        = models.ForeignKey(Program, on_delete=models.PROTECT, db_column = '_program', to_field= 'program')
	active             = models.BooleanField(default=True)

	class Meta:
		abstract = True

class Link(LinkAbs):
	id                 = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	upd_time           = models.DateTimeField(auto_now=True, db_column = '_upd_time')

	class Meta:
		unique_together = ['loan_type', 'bank']

	def __str__(self):
		return self.bank.name+"-"+str(self.loan_type)

class LoanDetailAbs(models.Model):
	# Foreign Keys
	insurance	       = models.ForeignKey(Insurance, on_delete=models.PROTECT)
	installment_type   = models.ForeignKey(InstallmentType, on_delete=models.PROTECT)
	# Log Fields
	upd_user           = models.ForeignKey(auth.get_user_model(), on_delete=models.PROTECT, db_column = '_user', to_field= 'username')
	upd_program        = models.ForeignKey(Program, on_delete=models.PROTECT, db_column = '_program', to_field= 'program')
	active             = models.BooleanField(default=True)

	class Meta:
		abstract = True

class LoanDetail(LoanDetailAbs):
	id                 = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	upd_time           = models.DateTimeField(auto_now=True, db_column = '_upd_time')
	loan               = models.OneToOneField(Loan, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.loan.bank)+"-"+str(self.loan.loan_type)+"-"+self.loan.name

"""
 
 ██╗      ██████╗  ██████╗     ████████╗ █████╗ ██████╗ ██╗     ███████╗███████╗
 ██║     ██╔═══██╗██╔════╝     ╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
 ██║     ██║   ██║██║  ███╗       ██║   ███████║██████╔╝██║     █████╗  ███████╗
 ██║     ██║   ██║██║   ██║       ██║   ██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║
 ███████╗╚██████╔╝╚██████╔╝       ██║   ██║  ██║██████╔╝███████╗███████╗███████║
 ╚══════╝ ╚═════╝  ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝
                                                                                
 
"""
class LoanRequest(models.Model):
	request_id   = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	loan_type    = models.ForeignKey(LoanType, on_delete=models.PROTECT, db_column = 'loan_type', to_field = 'loan_type')
	tenure       = models.ForeignKey(Tenure, on_delete=models.PROTECT, db_column = 'tenure', to_field = 'tenure')
	principal    = models.PositiveIntegerField()
	request_time = models.DateTimeField(auto_now_add=True)

	@property
	def available_tenures(self):
		return self.loan_type.tenures.all()

class LoanLog(LoanAbs):
	# Log Fields
	id                 = models.UUIDField(primary_key=True,default=uuid.uuid1, editable=False)
	loan_id            = models.CharField(max_length=36)
	upd_time           = models.DateTimeField(db_column = '_upd_time')
	upd_action		   = models.ForeignKey(Action, on_delete=models.PROTECT, db_column = '_action', to_field= 'action')

	def __init__(self, loan=None, action=None):
		super(LoanLog, self).__init__()
		self.loan_id        = str(loan.pk)
		self.loan_type      = loan.loan_type
		self.bank           = loan.bank
		self.tenure         = loan.tenure
		self.principal      = loan.principal
		self.name           = loan.name
		self.slug           = loan.slug
		self.description    = loan.description
		self.interest       = loan.interest
		self.active         = loan.active

		self.upd_user       = loan.upd_user
		self.upd_program    = loan.upd_program
		self.upd_time       = loan.upd_time
		self.upd_action     = action

	def __str__(self):
		return "log-"+self.bank.name + "-" +self.name

class LoanDetailLog(LoanDetailAbs):
	# Log Fields
	id                 = models.UUIDField(primary_key=True,default=uuid.uuid1, editable=False)
	upd_action		   = models.ForeignKey(Action, on_delete=models.PROTECT, db_column = '_action', to_field= 'action')
	loan_detail_id     = models.CharField(max_length=36)
	loan_id            = models.CharField(max_length=36)
	upd_time           = models.DateTimeField(db_column = '_upd_time')

	def __init__(self, loan_detail=None, action=None):
		super(LoanDetailLog, self).__init__()
		self.loan_detail_id   = str(loan_detail.pk)
		self.loan_id          = str(loan_detail.loan.id)
		self.insurance        = loan_detail.insurance
		self.installment_type = loan_detail.installment_type
		self.upd_program      = loan_detail.upd_program
		self.upd_user         = loan_detail.upd_user
		self.upd_time         = loan_detail.upd_time
		self.active           = loan_detail.active

		self.upd_action       = action

	def __str__(self):
		return "log-"+str(self.loan_detail_id)

class LinkLog(LinkAbs):
	# Log Fields
	id                 = models.UUIDField(primary_key=True,default=uuid.uuid1, editable=False)
	link_id            = models.CharField(max_length=36)
	upd_time           = models.DateTimeField(db_column = '_upd_time')
	upd_action		   = models.ForeignKey(Action, on_delete=models.PROTECT, db_column = '_action', to_field= 'action')

	def __init__(self, link=None, action=None):
		super(LinkLog, self).__init__()
		self.link_id          = str(link.pk)
		
		self.bank             = link.bank
		self.loan_type        = link.loan_type
		self.url              = link.url
		self.active           = link.active

		self.upd_program      = link.upd_program
		self.upd_user         = link.upd_user
		self.upd_time         = link.upd_time
		self.upd_action       = action

	def __str__(self):
		return "log-"+self.bank.name+"-"+str(self.loan_type)


class LoanSummary(models.Model):
	"""
	View table that is produced everyday and can be used directly in frontend.
	'bank','loan_name','min_principal','max_principal','min_tenure','max_tenure','interest','url'
	"""
	bank           = models.ForeignKey(Bank, on_delete=models.PROTECT)
	loan_type      = models.ForeignKey(LoanType, on_delete=models.PROTECT, db_column = 'loan_type', to_field= 'loan_type')
	min_principal  = models.ForeignKey(Principal, on_delete=models.PROTECT, db_column = 'min_principal', to_field= 'principal',related_name='+')
	max_principal  = models.ForeignKey(Principal, on_delete=models.PROTECT, db_column = 'max_principal', to_field= 'principal',related_name='+')
	min_tenure     = models.ForeignKey(Tenure, on_delete=models.PROTECT, db_column = 'min_tenure', to_field= 'tenure',related_name='+')
	max_tenure     = models.ForeignKey(Tenure, on_delete=models.PROTECT, db_column = 'max_tenure', to_field= 'tenure',related_name='+')
	min_interest   = models.FloatField()
	max_interest   = models.FloatField()
	tenures        = models.ManyToManyField(Tenure, related_name="loan_summaries", )
	date           = models.DateField(auto_now=True)

class LoanMatrix(models.Model):
	"""
	View table that is produced everyday and can be used directly in frontend.
	"""
	loan_type      = models.ForeignKey(LoanType, on_delete=models.PROTECT, db_column = 'loan_type', to_field= 'loan_type')
	tenure         = models.ForeignKey(Tenure, on_delete=models.PROTECT, db_column = 'min_tenure', to_field= 'tenure',related_name='+')
	principal      = models.ForeignKey(Principal, on_delete=models.PROTECT, db_column = 'min_principal', to_field= 'principal',related_name='+')
	min_interest   = models.FloatField(null=True, blank=True)
	loan_1         = models.ForeignKey(Loan, on_delete=models.PROTECT,related_name='+', blank=True, null=True)
	loan_2         = models.ForeignKey(Loan, on_delete=models.PROTECT,related_name='+', blank=True, null=True)
	loan_3         = models.ForeignKey(Loan, on_delete=models.PROTECT,related_name='+', blank=True, null=True)
	date           = models.DateField(auto_now=True)

class LoanMatrixTable(models.Model):
	"""
	View table that is produced everyday and can be used directly in frontend.
	"""
	loan_type      = models.ForeignKey(LoanType, on_delete=models.PROTECT, db_column = 'loan_type', to_field= 'loan_type')
	table_html     = models.TextField()
	date           = models.DateField(auto_now=True)
	

"""
 
 ███████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██╗     ███████╗
 ██╔════╝██║██╔════╝ ████╗  ██║██╔══██╗██║     ██╔════╝
 ███████╗██║██║  ███╗██╔██╗ ██║███████║██║     ███████╗
 ╚════██║██║██║   ██║██║╚██╗██║██╔══██║██║     ╚════██║
 ███████║██║╚██████╔╝██║ ╚████║██║  ██║███████╗███████║
 ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝
                                                       
 
"""

# Loanlog
@receiver(signals.post_save, sender=Loan)
def log_loan(sender, instance, created, **kwargs):
	action_str = "INSERT" if created else "UPDATE"
	upd_action = get_object_or_404(Action, action=action_str)
	LoanLog(loan=instance,action=upd_action).save()
	print('loan change logged')

@receiver(signals.pre_delete, sender=Loan)
def log_loan_delete(sender, instance, **kwargs):
	action_str = "DELETE"
	upd_action = get_object_or_404(Action, action=action_str)
	instance.upd_time = timezone.now()
	LoanLog(loan=instance,action=upd_action).save()
	print('loan deletion logged')

# Loandetaillog
@receiver(signals.post_save, sender=LoanDetail)
def log_loan_detail(sender, instance, created, **kwargs):
	action_str = "INSERT" if created else "UPDATE"
	upd_action = get_object_or_404(Action, action=action_str)
	LoanDetailLog(loan_detail=instance,action=upd_action).save()
	print('loan detail change logged')

@receiver(signals.pre_delete, sender=LoanDetail)
def log_loan_detail_delete(sender, instance, **kwargs):
	action_str = "DELETE"
	upd_action = get_object_or_404(Action, action=action_str)
	instance.upd_time = timezone.now()
	LoanDetailLog(loan_detail=instance,action=upd_action).save()
	print('loan detail deletion logged')


# Linklog
@receiver(signals.post_save, sender=Link)
def log_link(sender, instance, created, **kwargs):
	print('updating')
	action_str = "INSERT" if created else "UPDATE"
	upd_action = get_object_or_404(Action, action=action_str)
	LinkLog(link=instance,action=upd_action).save()
	print('loan detail change logged')

@receiver(signals.pre_delete, sender=Link)
def log_link_delete(sender, instance, **kwargs):
	action_str = "DELETE"
	upd_action = get_object_or_404(Action, action=action_str)
	instance.upd_time = timezone.now()
	LinkLog(link=instance,action=upd_action).save()
	print('loan detail deletion logged')