from django.urls import path
from zmhs.offices import views

app_name = 'offices'
urlpatterns = [
    path('',views.HqListView.as_view(),name='hq_list'),
    path('add_hq',views.CreateHqView.as_view(),name='add_hq'),
    path('<int:pk>',views.HqUpdateView.as_view(),name='update_hq'),
    path('hq/<int:pk>',views.HqUpdateView.as_view(),name='update_hq'),
    path('hq/delete/<int:pk>',views.HqDeleteView.as_view(),name='delete_hq'),
]
