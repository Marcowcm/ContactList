from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('',views.ContactListView.as_view(),name='contact_list'),
    path('<pk>',views.Contact_detail,name='contact_detail'),
    path('new/',views.ContactCreateView.as_view(),name='contact_new'),
    path('<pk>/update/',views.ContactUpdateView.as_view(),name='contact_update')
]
