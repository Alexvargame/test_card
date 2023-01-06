from django import forms
from .models import Card, CardSearch, CardOperation, ContrAgent, CardGenerator,CardDateCreateSearch, CardDateActiveSearch,Ammount
from django.forms import widgets

class CardForm(forms.ModelForm):

    class Meta:
        
        model=Card
        fields=['card_owner_name','card_serial','card_termin']
       
        widgets={
            'card_owner_name':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'card_serial':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            #'card_number':forms.Select( attrs={'class':'form-control', 'empty_value':True}),
            'card_termin':forms.Select( attrs={'class':'form-control', 'empty_value':True}),
            #'card_number':forms.Select( attrs={'class':'form-control', 'empty_value':True}),
            #'card_balance':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            #'card_begin_active':forms.DateTimeInput(attrs={'class':'form-control', 'empty_value':True}),
            #'card_end_active':forms.DateTimeInput(attrs={'class':'form-control', 'empty_value':True}),
            #'card_status':forms.TextInput(attrs={'class':'form-control', 'empty_value':True,'disabled':True}),
        }


class AmmountForm(forms.ModelForm):
    class Meta:
        model=Ammount
        fields=['ammount']
        
        widgets={
            'ammount':forms.NumberInput(attrs={'class':'form-control'}),
            }

class CardGeneratorForm(forms.ModelForm):
    class Meta:
        model=CardGenerator
        fields=['card_gen_serial','card_gen_number','card_gen_term_active']
        
        widgets={
            'card_gen_serial':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'card_gen_number':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'card_gen_term_active':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            }
    
class CardSearchForm(forms.ModelForm):

    class Meta:
        model=CardSearch
        fields=['card_owner_name','card_serial','card_number','card_date_create_from','card_end_active','card_status']

        widgets={
            'card_owner_name':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'card_serial':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'card_number':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'card_date_create_from':forms.DateInput(attrs={'class':'form-control', 'empty_value':True, 'type':'date'}),
            'card_end_active':forms.DateInput(attrs={'class':'form-control', 'empty_value':True, 'type':'date'}),
            'card_status':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            }

class CardSearchDateCreateForm(forms.ModelForm):

    class Meta:
        model=CardDateCreateSearch
        fields=['card_date_create']

        widgets={ 
            'card_date_create':forms.DateInput(attrs={'class':'form-control', 'empty_value':True, 'type':'date'}),
            }
class CardSearchDateActiveForm(forms.ModelForm):

    class Meta:
        model=CardDateActiveSearch
        fields=['card_date_end_active']

        widgets={ 
            'card_date_end_active':forms.DateInput(attrs={'class':'form-control', 'empty_value':True, 'type':'date'}),
            }
        
class AddSumOperationForm(forms.ModelForm):
    class Meta:
        model=CardOperation
        #initial - agent. type
        fields=['contr_agent','summa']
        widgets={
            'contr_agent':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'summa':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
         
            }
class TransferOperationForm(forms.ModelForm):
    class Meta:
        model=CardOperation
        fields=['contr_agent','summa']
        widgets={
            'contr_agent':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'summa':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            }

class PaymentOperationForm(forms.ModelForm):
    class Meta:
        model=CardOperation
        fields=['contr_agent','summa','oper_info']
        widgets={
            'contr_agent':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'summa':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'oper_info':forms.Textarea(attrs={'class':'form-control', 'empty_value':True}),
            }
class ContrAgentForm(forms.ModelForm):
    class Meta:
        model=ContrAgent
        fields=['contr_agent_name','contr_agent_serial','contr_agent_number']
        widgets={
             'contr_agent_name':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
             'contr_agent_serial':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
             'contr_agent_number':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),

            }
