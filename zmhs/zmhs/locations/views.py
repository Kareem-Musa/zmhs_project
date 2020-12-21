from django.shortcuts import render , get_object_or_404
from zmhs.locations.models import State , Locality , Unity , City , District
from django.views.generic import CreateView , ListView , DetailView , UpdateView
from django.utils import timezone
from zmhs.locations.forms import StateForm


class StateListView(ListView):
    model = State
    template_name = 'locations/state_list.html'
    context_object_name = 'states'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     state = State.objects.get(id=kwargs['pk'])
    #     context['state'] = state
    #     return context

class StateDetailView(DetailView):
    models = State
    template_name = 'locations/state_detail.html'
    context_object_name = 'state'
    queryset = State.objects.all()
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

class AddStateView(CreateView):
    model = State
    fields = ['name']
    template_name = 'locations/create_state.html'

class UpdateStateView(UpdateView):
    model = State
    fields = ['name']
    context_object_name = 'state'
    template_name = 'locations/create_state.html'

# def update_state(request,pk):
#     state = State.objects.get(id=pk)
#     form = StateForm(instance=state)
#     if request.method == "POST":
#         form = StateForm(request.POST,instance=state)
#         if form.is_valid():
#             form.save()
#         return redirect('locations:state_list')
#     return render(reuest,'locations/state_list.html',{'form':form,'state':state})
# Locality views
class LocalityListView(ListView):
    model = Locality
    template_name = 'locations/locality_list.html'
    context_object_name = 'localities'

class AddLocalityView(CreateView):
    model = Locality
    fields = ['name','state']
    template_name = 'locations/add_locality.html'
    #context_object_name = 'locality'

class LocalityDetailView(DetailView):
    model = Locality
    template_name = 'locations/locality_detail.html'
    context_object_name = 'locality'

class LocalityUpdateView(UpdateView):
    model = Locality
    template_name = 'locations/add_locality.html'
    fields = ['name','state']

# Unity views
class UnityListView(ListView):
    model = Unity
    template_name = 'locations/unity_list.html'
    context_object_name = 'unities'

class AddUintyView(CreateView):
    model = Unity
    fields = ['name','locality']
    template_name = 'locations/add_unity.html'

class UnityDetailView(DetailView):
    model = Unity
    template_name = 'locations/unity_detail'
    context_object_name = 'unity'

class UnityUpdateView(UpdateView):
    model = Unity
    fields = ['name','locality']
    template_name = 'locations/add_unity.html'

# City Views
class CityListView(ListView):
    model = City
    template_name = 'locations/city_list.html'
    context_object_name = 'cities'

class AddCityView(CreateView):
    model = City
    fields = ['name','unity']
    template_name = 'locations/add_city.html'

class CityDetailView(DetailView):
    model = City
    template_name = 'locations/city_detail.html'
    context_object_name = 'city'

class CityUpdateView(UpdateView):
    model = City
    fields = ['name','unity']
    template_name = 'locations/add_city.html'

# District views
class DistrictListView(ListView):
    model = District

    template_name = 'locations/district_list.html'
    context_object_name = 'districts'

class AddDistrictView(CreateView):
    model = District
    fields = ['name','city']
    template_name = 'locations/add_district.html'

class DistrictDetailView(DetailView):
    model = District
    template_name = 'locations/district_detail.html'
    context_object_name = 'district'

class DistrictUpdateView(UpdateView):
    model = District
    fields = ['name','city']
    template_name = 'locations/add_district.html'
