from django.urls import path
from . import views

app_name = 'locations'
urlpatterns = [
    path('',views.StateListView.as_view(),name='state_list'),
    path('add_state',views.AddStateView.as_view(),name='add_state'),
    path('<int:pk>',views.StateDetailView.as_view(),name='state_detail'),
    path('update_state/<int:pk>',views.UpdateStateView.as_view(),name='update_state'),
    #Locality urls
    path('localities',views.LocalityListView.as_view(),name='locality_list'),
    path('add_locality',views.AddLocalityView.as_view(),name='add_locality'),
    path('locality/<int:pk>',views.LocalityDetailView.as_view(),name='locality_detail'),
    path('locality/update/<int:pk>',views.LocalityUpdateView.as_view(),name='update_locality'),
    # Unities urls
    path('unities',views.UnityListView.as_view(),name='unity_list'),
    path('add_unity',views.AddUintyView.as_view(),name='add_unity'),
    path('unity/<int:id>',views.UnityDetailView.as_view(),name='unity_detail'),
    path('unity/update/<int:pk>',views.UnityUpdateView.as_view(),name='update_unity'),
    # City urls
    path('cities',views.CityListView.as_view(),name='city_list'),
    path('add_city',views.AddCityView.as_view(),name='add_city'),
    path('city/<int:pk>',views.CityDetailView.as_view(),name='city_detail'),
    path('city/update/<int:pk>',views.CityUpdateView.as_view(),name='update_city'),
    #Distric urls
    path('districts',views.DistrictListView.as_view(),name='district_list'),
    path('add_district',views.AddDistrictView.as_view(),name='add_district'),
    path('district/<int:pk>',views.DistrictDetailView.as_view(),name='district_detail'),
    path('district/update/<int:pk>',views.DistrictUpdateView.as_view(),name='district_city'),
]
