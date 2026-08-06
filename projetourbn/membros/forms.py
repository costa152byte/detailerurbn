from django import forms

from .models import Membros


class MembrosForm(forms.ModelForm):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'M'
        verbose_name_plural = 'Meta'
        model = Membros

        fields = ['firstname', 'lastname', 'telefone', 'data_ingresso']  # noqa: RUF012 

        widgets = {  # noqa: RUF012
                ' data_ingresso': forms.DateInput(attrs={'type':'date' }),

                'telefone': forms.NumberInput(attrs={'placeholder': 'digite apenas números'}),
    }
        labels =  {  # noqa: RUF012
            'firstname': 'Primeiro Nome',
            'lastname': 'Ultimo Nome',
            'telefone': 'Telefone',
            'data_ingresso': 'Data de Ingresso',
    }
