from django.urls import path

from .views import *

urlpatterns =[
    path('', main_menu, name='main_menu_url'),
    path('cards/',cards_list, name='cards_list_url'),
    path('cards/update/', CardBaseUpdate.as_view(),name='card_base_update_url' ),
    path('data/', main_data_menu, name='main_data_menu_url'), 
    path('data/card_generate/', CardGenerate.as_view(),name='card_gen_url'),
    path('data/card_generate/list', cards_gen_list,name='card_gen_list_url'),
    path('data/contragents/create/', ContragentCreate.as_view(),name='contr_agent_create_url'),
    path('data/contragents/<int:contr_agent_id>/update/',ContragentUpdate.as_view(), name='contr_agent_update_url'),
    path('data/contragents/<int:contr_agent_id>/delete/',ContragentDelete.as_view(), name='contr_agent_delete_url'),
    path('data/contragents/<int:contr_agent_id>/detail/',ContragentDetailView.as_view(), name='contr_agent_detail_url'),
    path('data/contragents/', contragents_list, name='contragents_list_url'),
    path('operations/',operations_list, name='operations_list_url'),
    path('cards/create/', CardCreate.as_view(), name='card_create_url'),
    path('cards/search/', CardSearchView.as_view(), name='search_card_url'),
    path('search/', search_card_for_number, name='search_card_for_number_url'),
    path('cards/search_serial/', search_card_for_serial, name='search_card_for_serial_url'),
    path('cards/search_status/', search_card_for_status, name='search_card_for_status_url'),
    path('cards/search_date_create/', CardDateCreateSearchView.as_view(), name='search_date_create_card_url'),
    path('cards/search_date_active/', CardDateActiveSearchView.as_view(), name='search_date_active_card_url'),
    path('cards/<int:card_id>', CardDetailView.as_view(),name='card_detail_url' ),
    path('operations/<int:card_operation_id>', OperationDetailView.as_view(),name='card_operation_detail_url' ),
    path('cards/<int:card_id>/add_sum/', CardAddSum.as_view(),name='card_add_sum_url' ),
    path('cards/<int:card_id>/transfer/', CardTransfer.as_view(),name='card_transfer_url' ),
    path('cards/<int:card_id>/payment/', CardPayment.as_view(),name='card_payment_url' ),
    path('cards/<int:card_id>/delete/', CardDelete.as_view(),name='card_delete_url' ),
    path('cards/<int:card_id>/activate/', CardActivate.as_view(),name='card_activate_url' ),
    path('cards/<int:card_id>/deactivate/', CardDeactivate.as_view(),name='card_deactivate_url' ),
    ]
