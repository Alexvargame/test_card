from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import HttpResponse
from django import forms
from .models import Card, CardSearch, CardOperation,ContrAgent, CardGenerator
from .forms import CardForm, CardSearchForm,AddSumOperationForm, TransferOperationForm, PaymentOperationForm, ContrAgentForm, CardGeneratorForm, CardSearchDateCreateForm, CardSearchDateActiveForm, AmmountForm
from django.urls import reverse

from datetime import date, time, datetime, timedelta
from random import randint, choice
from django.contrib.auth.mixins import LoginRequiredMixin

from smart_selects.db_fields import GroupedForeignKey
def cards_list(request):

    cards=Card.objects.all()
##    for card in cards:
##            #date_b=[int(i) for i in card.card_end_active.split('-')]
##            d=datetime(card.card_end_active.year,card.card_end_active.month, card.card_end_active.day) 
##            d1=datetime.now()
##            if d1>d:
##                card.card_status='overdue'
##                card.save()
    return render(request,'cards/cards_list.html',context={'cards':cards,'s':cards})


def cards_update(request):
    cards=Card.objects.all()
    for card in cards:
        if card.card_end_active>datetime.now():
            card.card_status='overdue'
            card.save()
    return redirect(reverse,'cards/cards_list.html',context={'cards':cards,'s':cards})    
    
def cards_gen_list(request):

    cards_gen=CardGenerator.objects.all()
    
    return render(request,'cards/cards_gen_list.html',context={'cards_gen':cards_gen})
def main_data_menu(request):
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
    
    return render(request,'cards/main_data_page.html')



def operations_list(request):
    operations=CardOperation.objects.all()
    return render(request,'cards/operations_list.html',context={'operations':operations, 's':operations})

def search_card_for_number(request):
    search_query=request.GET.get('search','')
    if search_query:
        cards=Card.objects.filter(card_number=search_query.strip())
        return render(request, 'cards/cards_list.html', context={'cards':cards})
    else:
        return render(request,'cards/mane_page.html')

def search_card_for_serial(request):
    search_query=request.GET.get('search_serial','')
    cards=Card.objects.filter(card_serial=search_query)
    return render(request, 'cards/search_card_serial.html', context={'cards':cards})



class CardBaseUpdate(LoginRequiredMixin,View):
    
    def get(self, request):
        cards=Card.objects.all()
        return render(request, 'cards/card_base_update.html', context={'cards':cards,'s':datetime.now(),'s1':cards})

    def post(self, request):
        cards=Card.objects.all()
        for card in cards:
            #date_b=[int(i) for i in card.card_end_active.split('-')]
            d=datetime(card.card_end_active.year,card.card_end_active.month, card.card_end_active.day) 
            d1=datetime.now()
            if d1>d:
                card.card_status='overdue'
                card.save()
        return redirect(reverse('cards_list_url'))


    
##class CardGenerate(LoginRequiredMixin,View):
##    def get(self,request):
##        form=CardGeneratorForm(initial={'card_gen_number':'0000000000000000'})
##        return render(request, 'cards/card_generator.html', context={'form':form})
##    def post(self, request):
##        num=randint(100000000000,999999999999)
##        seri=request.POST['card_gen_serial']      
##        bound_form=CardGeneratorForm(request.POST)
##        if bound_form.is_valid():
##            new_card_gen=bound_form.save()
##            new_card_gen.card_gen_number=''.join([str(ord(s)-64) for s in seri])+str(num)
##            new_card_gen.save()
##            return redirect(reverse('card_gen_list_url'))
##        return render(request, 'cards/card_generator.html', context={'form':bound_form,'s':(seri,bound_form.cleaned_data,request.POST['card_gen_number'])})
        
class CardGenerate(LoginRequiredMixin,View):
    def get(self,request):
        form=CardGeneratorForm(initial={'card_gen_number':'0000000000000000'})
        form1=AmmountForm(initial={'ammount':1})
        return render(request, 'cards/card_generator.html', context={'form':form, 'form1':form1})
    def post(self, request):
       
        seri=request.POST['card_gen_serial']
        term=request.POST['card_gen_term_active']
        bound_form=CardGeneratorForm(request.POST)
        bound_form1=AmmountForm(request.POST)
        i=int(request.POST['ammount'])
        if bound_form.is_valid():
            while i>0:
                num=randint(100000000000,999999999999)
                name='new_card_gen'+str(i)
                #name=bound_form.save()
                name=CardGenerator()
                name.card_gen_serial=seri
                name.card_gen_number=''.join([str(ord(s)-64) for s in seri])+str(num)
                name.card_gen_term_active=term
                name.save()
                i=i-1
            return redirect(reverse('card_gen_list_url'))
        return render(request, 'cards/card_generator.html', context={'form':bound_form,'s':(seri,bound_form.cleaned_data,request.POST['card_gen_number'])})

    
    
def search_card_for_status(request):
    search_query=request.GET.get('search_status','')
    cards=Card.objects.filter(card_status=search_query)
    return render(request, 'cards/search_card_status.html', context={'cards':cards})  

class CardCreate(LoginRequiredMixin,View):
##    def __init__(self, serial):
##        self.serial=serial
##
##     def get(self,request):
##        dictnum={}
##        self.initials={'card_status':'not_active', 'card_begin_active':'01/01/22', 'card_end_active':'01/01/30'}
##        
##        seria='ACC'
##        for ser in [num.card_gen_serial for num in CardGenerator.objects.all()]:
##                key, value=ser, 
##                dictnum[key]=value
##        form=CardForm(initial={'card_serial':seria})
##        form.fields['card_number'].choices=dictnum[seria]
##        if form['card_serial'].value():
##            
##            form=CardForm()
##            form.fields['card_number'].choices=dictnum['ACC']#form['card_serial'].value()]
##            numbers=[(num.card_gen_number,num.card_gen_number) for num in CardGenerator.objects.all() if num.card_gen_serial==form['card_serial'].value()]
##            
##            return render(request, 'cards/card_create.html', context={'form':form,'s':(request.POST, self.initials, form.fields['card_number'].choices)})       
##                    
##            
##        #s1=form['card_serial'].as_widget(forms.Select(choices=numbers))
##        
##            
##        return render(request, 'cards/card_create.html', context={'form':form,'s':(request.POST, self.initials, form.fields['card_number'].choices,dictnum)})
##     def post(self, request):
##                          
##                
##        bound_form=CardForm(request.POST)
##        if bound_form.is_valid():
##            new_card=bound_form.save()
##            return redirect(new_card)
##        return render(request, 'cards/card_create.html', context={'form':bound_form,'s':(request.POST,bound_form.cleaned_data)})
##        




    def get(self,request):
        self.initials={'card_status':'not_active'}
        form=CardForm()
        return render(request, 'cards/card_create.html', context={'form':form})       
  
    def post(self, request):
        term=request.POST['card_termin']                   
        seri=request.POST['card_serial']    
        bound_form=CardForm(request.POST)
        if bound_form.is_valid():
            new_card=bound_form.save()
            new_card.card_number=choice([num.card_gen_number for num in CardGenerator.objects.all() if num.card_gen_serial==seri and num.card_gen_term_active==term])
            new_card.save()
            card_gen=CardGenerator.objects.filter(card_gen_serial=seri,card_gen_number=new_card.card_number,card_gen_term_active=term)
            card_gen[0].delete()
            return redirect(new_card)
        return render(request, 'cards/card_create.html', context={'form':bound_form,'s':(request.POST,bound_form.cleaned_data)})
        
                      
class CardDetailView(LoginRequiredMixin,View):
    def get(self, request, card_id):
        card=get_object_or_404(Card, id=card_id)
        return render(request, 'cards/card_detail.html', context={'card':card})

class OperationDetailView(LoginRequiredMixin,View):
    def get(self, request, card_operation_id):
        oper=get_object_or_404(CardOperation, id=card_operation_id)
        #card=Card.objects.filter(card_owner_name=oper.agent)
        return render(request, 'cards/card_operation_detail.html', context={'oper':oper})

    
class CardDelete(LoginRequiredMixin,View):
    
    def get(self, request, card_id):
        card=Card.objects.get(id=card_id)
        return render(request, 'cards/card_delete.html', context={'card':card})

    def post(self, request, card_id):
        card=Card.objects.get(id=card_id)
        card.delete()
        return redirect(reverse('cards_list_url'))

class CardActivate(LoginRequiredMixin,View):
    
    def get(self, request, card_id):
        card=Card.objects.get(id=card_id)
        
        return render(request, 'cards/card_activate_deactivate.html', context={'card':card})

    def post(self, request, card_id):
        card=Card.objects.get(id=card_id)
        card.card_status='active'
        card.card_begin_active=datetime.now()
        card.card_end_active=card.card_begin_active+timedelta(days=int(card.card_termin)*30)
        card.save()
        return redirect(reverse('cards_list_url'))

class CardDeactivate(LoginRequiredMixin,View):
    
    def get(self, request, card_id):
        card=Card.objects.get(id=card_id)
        
        return render(request, 'cards/card_activate_deactivate.html', context={'card':card})

    def post(self, request, card_id):
        card=Card.objects.get(id=card_id)
        card.card_status='not_active'
        card.card_end_active=datetime.now()
        card.save()
        return redirect(reverse('cards_list_url'))

    
class CardAddSum(LoginRequiredMixin,View):
    def get(self, request, card_id):
        card=Card.objects.get(id=card_id)
        initials={'type_op':'Add_sum','agent':card.card_owner_name}
        form=AddSumOperationForm()
        return render(request, 'cards/add_sum_operation.html', context={'form':form,'card':card})
    def post(self, request, card_id):
        card=Card.objects.get(id=card_id)
        bound_form=AddSumOperationForm(request.POST)
        if bound_form.is_valid():
            new_oper=bound_form.save()
            new_oper.agent=card.card_owner_name
            new_oper.type_op='Add_sum'
            new_oper.save()
            return redirect(new_oper)
        return render(request, 'cards/add_sum_operation.html', context={'form':bound_form,'card':card})
        
class CardTransfer(LoginRequiredMixin,View):
    def get(self, request, card_id):
        card=Card.objects.get(id=card_id)
        initials={'type_op':'Add_sum','agent':card.card_owner_name}
        form=TransferOperationForm()
        return render(request, 'cards/transfer_operation.html', context={'form':form,'card':card})
    def post(self, request, card_id):
        card=Card.objects.get(id=card_id)
        bound_form=TransferOperationForm(request.POST)
        if bound_form.is_valid():
            new_oper=bound_form.save()
            new_oper.agent=card.card_owner_name
            new_oper.type_op='Transfer'
            new_oper.save()
            return redirect(new_oper)
        return render(request, 'cards/transfer_operation.html', context={'form':bound_form,'card':card})  

class CardPayment(LoginRequiredMixin,View):
    def get(self, request, card_id):
        card=Card.objects.get(id=card_id)
        initials={'type_op':'Add_sum','agent':card.card_owner_name}
        form=PaymentOperationForm()
        return render(request, 'cards/payment_operation.html', context={'form':form,'card':card})
    def post(self, request, card_id):
        card=Card.objects.get(id=card_id)
        bound_form=PaymentOperationForm(request.POST)
        if bound_form.is_valid():
            new_oper=bound_form.save()
            new_oper.agent=card.card_owner_name
            new_oper.type_op='Payment'
            new_oper.save()
            return redirect(new_oper)
        return render(request, 'cards/payment_operation.html', context={'form':bound_form,'card':card})  

  
class CardSearchView(LoginRequiredMixin,View):
    initials={'card_number':'','card_date_create_from':date.today()+timedelta(days=1),'card_end_active':date(2030,1,1)}
    
    def get(self, request):
        query_name=[]
        query_status=[]
        query_serial=[]
        query_number=[]
        if request.GET:
            bound_form=CardSearchForm(request.GET, initial=self.initials)
            date_b=[int(i) for i in request.GET['card_date_create_from'].split('-')]
            date_e=[int(i) for i in request.GET['card_end_active'].split('-')] 
            if bound_form['card_owner_name'].value():
                query_name.append(bound_form['card_owner_name'].value())
            else:
                for n in Card.objects.all():
                    query_name.append(n.card_owner_name)
            if bound_form['card_number'].value():
                query_number.append(bound_form['card_number'].value())
            else:
                for n in Card.objects.all():
                    query_number.append(n.card_number)
            if bound_form['card_serial'].value():
                query_serial.append(bound_form['card_serial'].value())
            else:
                query_serial=['AABB','ABCC','ACAB','ADBC']
            if bound_form['card_status'].value():
                query_status.append(bound_form['card_status'].value())
            else:
                query_status=['not_active','active','overdue']
            cards=Card.objects.filter(card_owner_name__in=query_name, card_serial__in=query_serial,card_number__in=query_number,
                                      card_date_create__range=(date(2014,1,1),date(date_b[0],date_b[1],date_b[2])),
                                      card_end_active__range=(date.today(), date(2030,1,1)),
                                      card_status__in=query_status,)
            return render(request, 'cards/cards_search_list.html', context={'cards':cards})
                
        else:
            form=CardSearchForm(initial=self.initials)
        return render(request, 'cards/search_card.html', context={'form':form})

class CardDateCreateSearchView(LoginRequiredMixin,View):    
    def get(self, request):
        if request.GET:
            bound_form=CardSearchDateCreateForm(request.GET)
            date_b=[int(i) for i in request.GET['card_date_create'].split('-')]
            cards=Card.objects.filter( card_date_create__range=(date(2014,1,1),date(date_b[0],date_b[1],date_b[2])))
            return render(request, 'cards/cards_list.html', context={'cards':cards})
                
        else:
            form=CardSearchDateCreateForm()
        return render(request, 'cards/search_date_create_card.html', context={'form':form})

class CardDateActiveSearchView(LoginRequiredMixin,View):    
    def get(self, request):
        if request.GET:
            bound_form=CardSearchDateActiveForm(request.GET)
            cards=Card.objects.filter( card_end_active__range=(date.today(), date(2030,1,1)))
            return render(request, 'cards/cards_list.html', context={'cards':cards})
                
        else:
            form=CardSearchDateActiveForm()
        return render(request, 'cards/search_date_active_card.html', context={'form':form})   
class ContragentCreate(LoginRequiredMixin, View):
    def get(self, request):
        form=ContrAgentForm()
        return render(request, 'cards/contragents/contragent_create.html', context={'form':form})

    def post(self, request):
        bound_form=ContrAgentForm(request.POST)
        if bound_form.is_valid():
            new_contragent=bound_form.save()
            
            return redirect(new_contragent)
        return render(request, 'cards/contragents/contragent_create.html', context={'form':bound_form})
def contragents_list(request):
    contragents=ContrAgent.objects.all()
    return render(request,'cards/contragents/contragent_list.html', context={'contragents':contragents})


class ContragentDetailView(View):  
    def get (self, request, contr_agent_id):
        contragent=get_object_or_404(ContrAgent, id=contr_agent_id)
        return render(request,'cards/contragents/contragent_detail.html', context={'contragent':contragent})

class ContragentUpdate(LoginRequiredMixin,View):
    
    def get(self, request, contr_agent_id):
        contragent=ContrAgent.objects.get(id=contr_agent_id)
        bound_form=ContrAgentForm(instance=contragent)
        return render(request, 'cards/contragents/contragent_update.html', context={'form':bound_form, 'contragent':contragent})
    def post(self, request,contr_agent_id):
        contragent=ContrAgent.objects.get(id=contr_agent_id)
        bound_form=ContrAgentForm(request.POST, instance=contragent)
        if bound_form.is_valid():
            new_contragent=bound_form.save()
            return redirect(new_contragent)
        return render(request, 'cards/contragents/contragent_update.html', context={'form':bound_form, 'contragent':contragent}) 
       
class ContragentDelete(LoginRequiredMixin, View):
    
    def get(self, request, contr_agent_id):
        contragent=ContrAgent.objects.get(id=contr_agent_id)
        return render(request, 'cards/contragents/contragent_delete.html', context={'contragent':contragent})

    def post(self, request, contr_agent_id):
        contragent=ContrAgent.objects.get(id=contr_agent_id)
        contragent.delete()
        return redirect(reverse('contragents_list_url'))

   



def main_menu(request):
  
    return render(request,'cards/main_page.html',)
