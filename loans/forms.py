from django import forms
from .models import LoanRequest, Tenure
from loans.models import LoanType

class CurrencyInputWidget(forms.widgets.TextInput):
    template_name = 'loans/widgets/principal_input_widget.html'
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.4.1.slim.min.js',
            'loans/js/number-seperator.js',
        )


class LoanRequestForm(forms.ModelForm):
    # tenure = forms.ChoiceField(choices=[(x, x) for x in Tenure.objects.all().order_by('tenure')])
    class Meta:
        model = LoanRequest
        fields = ('loan_type','principal','tenure')
        widgets = {
            'principal': CurrencyInputWidget(
                attrs={}),
        }
    
    def __init__(self, *args, **kwargs):
        super(LoanRequestForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''
        
    def save(self, loan_type=None):
        print('saving loan request')
        self.loan_type = LoanType.objects.get(loan_type=loan_type)
        print(self.loan_type)
        super(LoanRequestForm, self).save()