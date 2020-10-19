from django.db import models

class FAQItem(models.Model):
	parent_subject   = models.CharField(max_length=240, default = 'NA')
	subject          = models.CharField(max_length=240, default = 'NA')
	bullet_no        = models.PositiveIntegerField()
	bullet_title     = models.CharField(max_length=240)
	bullet_content   = models.TextField()
	relevant_to      = models.CharField(max_length=240) # bu bir sayfa ismi, bank_name veya loan_type olabilir

	def __str__(self):
		return self.subject+"-"+str(self.bullet_no)