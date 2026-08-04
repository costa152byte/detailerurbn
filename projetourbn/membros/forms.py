from django import forms

from .models import Membros


class Membrosform(forms.Modelform):
    class meta:
        model = Membros

        fields = ['fiirsname', 'lastname', 'telefone', 'data_ingresso']  # noqa: RUF012 

        widgets = {  # noqa: RUF012
                ' data_ingresso ': forms.DateInput(attrs={'type':'date' }),

                'telefone': forms.NumberInput(attrs={'placeholder': 'digite apenas números'}
        ),
    }
        labels =  {  # noqa: RUF012
            'firsname': 'primeiro nome',
            'lastname': 'ultimo nome',
            'telefone': 'Telefone',
            'data_ingresso': 'Data de Ingresso',
    }
