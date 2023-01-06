from django.db import models

from django.shortcuts import reverse
from smart_selects.db_fields import GroupedForeignKey


class CardGenerator(models.Model):
    serials=[('AABB','AABB'),('ABCC','ABCC'),('ACAB','ACAB'),('ADBC','ADBC')]
    terms=[('1','1'),('6','6'),('12','12')]
    card_gen_serial=models.CharField(max_length=10, choices=serials)
    #card_gen_serial=models.ForeignKey(max_length=10, choices=serials)
    card_gen_number=models.CharField(max_length=22)
    card_gen_term_active=models.CharField(max_length=5, choices=terms)
    def get_absolute_url(self):
            return reverse('card_gen_detail_url', kwargs={'card_gen_id':self.id})
    def get_update_url(self):
            return reverse('card_gen_update_url', kwargs={'card_gen_id':self.id})
    def get_delete_url(self):
            return reverse('card_gen_delete_url', kwargs={'card_gen_id':self.id})
    def __str__(self):
            return " Серия- %s  Номер- %s Срок активности %s" % (self.card_gen_serial,self.card_gen_number,self.card_gen_term_active)

class Card(models.Model):
    serials=[('AABB','AABB'),('ABCC','ABCC'),('ACAB','ACAB'),('ADBC','ADBC')]
    terms=[('1','1'),('6','6'),('12','12')]
    card_owner_name=models.CharField(max_length=50)
    card_serial=models.CharField(max_length=10, choices=serials)
    card_number=models.CharField(max_length=22,choices=[(num.card_gen_number,num.card_gen_number) for num in CardGenerator.objects.all()],blank=True)
##    card_serial=models.ForeignKey(CardGenerator,on_delete=models.CASCADE,)
##    card_number=GroupedForeignKey(Card, "card_serial")
    card_balance=models.FloatField(default=0.0)
    card_date_create=models.DateTimeField(auto_now_add=True)
    card_begin_active=models.DateTimeField(default='2022-01-01 00:00:00',blank=True)
    card_end_active=models.DateTimeField(default='2030-01-01 00:00:00',blank=True)
    card_status=models.CharField(default='not_active',max_length=15)
    card_termin=models.CharField(max_length=5,choices=terms,blank=True,null=True)

    def get_absolute_url(self):
            return reverse('card_detail_url', kwargs={'card_id':self.id})
    def get_update_url(self):
            return reverse('card_update_url', kwargs={'card_id':self.id})
    def get_delete_url(self):
            return reverse('card_delete_url', kwargs={'card_id':self.id})
    def get_activate_url(self):
            return reverse('card_activate_url', kwargs={'card_id':self.id})
    def get_deactivate_url(self):
            return reverse('card_deactivate_url', kwargs={'card_id':self.id})
    def __str__(self):
            return " Владелец- %s Серия- %s Номер- %s Дата выпуска- %s Дата активации- %s Дата окончания активации- %s Статус- %s Срок- активности %" % (self.card_owner_name,
        self.card_serial,self.card_number, self.card_date_create, self.card_begin_active, self.card_end_active, self.card_status, self.card_termin)


class CardSearch(models.Model):
    status_var=[('not_active','not_active'),('active', 'active'),('overdue', 'overdue')]
    serials=[('AABB','AABB'),('ABCC','ABCC'),('ACAB','ACAB'),('ADBC','ADBC')]
    card_owner_name=models.CharField(max_length=50,null=True, blank=True)
    card_serial=models.CharField(max_length=10,choices=serials,null=True, blank=True)
    card_number=models.CharField(max_length=20,null=True, blank=True)

    card_date_create_from=models.DateTimeField()
    card_end_active=models.DateTimeField()
    card_status=models.CharField(max_length=10, choices=status_var, null=True, blank=True)

class CardDateCreateSearch(models.Model):
    card_date_create=models.DateTimeField()
class CardDateActiveSearch(models.Model):
    card_date_end_active=models.DateTimeField()
class Ammount(models.Model):
    ammount=models.IntegerField()





class ContrAgent(models.Model):
        serials=[('AABB','AABB'),('ABCC','ABCC'),('ACAB','ACAB'),('ADBC','ADBC')]
        contr_agent_name = models.CharField(max_length=40, db_index=True)
        contr_agent_serial=models.CharField(max_length=10, choices=serials)
        contr_agent_number=models.CharField(max_length=20)
        
        def get_absolute_url(self):
            return reverse('contr_agent_detail_url', kwargs={'contr_agent_id':self.id})
        def get_update_url(self):
            return reverse('contr_agent_update_url', kwargs={'contr_agent_id':self.id})
        def get_delete_url(self):
            return reverse('contr_agent_delete_url', kwargs={'contr_agent_id':self.id})
        def __str__(self):
            return " Имя- %s Серия карты - %s Номер карты- %s" % (self.contr_agent_name, self.contr_agent_serial, self.contr_agent_number)
       

class CardOperation(models.Model):
    types=[('Add_sum','Add_sum'),('Payment','Payment'),('Transfer money', 'Transfer money')]
    contr_agents=[(ag.contr_agent_name,ag.contr_agent_name) for ag in ContrAgent.objects.all()]
    #contr_agents=[('A','A'),('B','B')]
    type_op=models.CharField(max_length=20, choices=types)
    agent=models.CharField(max_length=20, default='')
    contr_agent=models.CharField(max_length=20,choices=contr_agents)
    date_operation=models.DateTimeField(auto_now_add=True)
    summa=models.FloatField()
    oper_info=models.TextField(blank=True)
    checks=models.FileField(blank=True)

    def get_absolute_url(self):
            return reverse('card_operation_detail_url', kwargs={'card_operation_id':self.id})
    def get_delete_url(self):
            return reverse('card_deactivate_url', kwargs={'card_id':self.id})
    def __str__(self):
            return " Тип операции- %s Агент- %s Контрагент- %s Дата операции- %s Сумма- %s Информация- %s " % (self.type_op,
        self.agent,self.contr_agent, self.date_operation, self.summa, self.oper_info)

    
##class AddSumOperation(models.Model):
##    types=[('Add_sum','Add_sum'),('Payment','Payment'),('Transfer money', 'Transfer money')]
##    #contr_agents=[(ag,name,ag.name) for ag in ContrAgent.objects.all()]
##    contr_agents=[('A','A'),('B','B')]
##    type_op=models.CharField(max_length=20, choices=types)
##    agent=models.CharField(max_length=20, default='')
##    contr_agent=models.CharField(max_length=20)
##    date_operation=models.DateTimeField(auto_now_add=True)
##    summa=models.FloatField()
##    oper_info=models.TextField(blank=True)
##    checks=models.FileField(blank=True)
##    
##
