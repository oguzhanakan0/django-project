from django.contrib import admin
from .models import *

# Basic Models
admin.site.register(Bank)
admin.site.register(Insurance)
admin.site.register(LoanType)
admin.site.register(Principal)
admin.site.register(Tenure)
admin.site.register(InstallmentType)

# Log Related Models
admin.site.register(Program)

# Complex Models
admin.site.register(Loan)
admin.site.register(LoanDetail)
admin.site.register(Link)
admin.site.register(LoanRequest)
admin.site.register(LoanSummary)