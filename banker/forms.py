from django import forms

from banker.models import Account, Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        error_css_class = 'error'
        required_css_class = 'required'

        widgets = {
            'payer_account': forms.RadioSelect,
            'payee_account': forms.RadioSelect,
        }

    def __init__(self, game_id=None, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)

        if game_id:
            for field in ['payer_account', 'payee_account']:
                self.fields[field].queryset = Account.objects.filter(game_id=game_id)
                self.fields[field].empty_label = None
