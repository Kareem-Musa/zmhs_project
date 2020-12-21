from django.shortcuts import render
from django.views.generic import CreateView , ListView , DetailView ,UpdateView , DeleteView
from zmhs.offices.models import HQuarter , Sector , Office
from zmhs.offices.forms import HqForm , SectorForm

class CreateHqView(CreateView):
    model = HQuarter
    form_class = HqForm
    #fields = ['state','name']
    context_object_name = 'hquarter'
    template_name = 'offices/add_hq.html'

class HqListView(ListView):
    model = HQuarter
    context_object_name = 'hqs'
    template_name = 'offices/hq_list.html'

class HqDetailView(DetailView):
    model = HQuarter
    context_object_name = 'hq'
    template_name = 'offices/hq_detail.html'

class HqUpdateView(UpdateView):
    model = HQuarter
    form_class = HqForm
    context_object_name = 'hq'
    template_name = 'offices/add_hq.html'

class HqDeleteView(DeleteView):
    model = HQuarter
    context_object_name = 'hq'
    template_name = 'offices/hq_delete.html'

# Sector views
class SectorCreateView(CreateView):
    model = Sector
    form_class = SectorForm
    context_object_name = "sector"
    template_name = 'offices/add_sector.html'

class SectorListView(ListView):
    model = Sector
    context_object_name = 'sectors'
    template_name = 'offices/sector_list.html'

class SectorDetailView(DetailView):
    model = Sector
    context_object_name = 'sector'
    template_name = 'offices/sector_detail.html'

class SectorUpdateView(UpdateView):
    model = Sector
    form_class = SectorForm
    context_object_name = 'sector'
    template_name = 'offices/sector_update.html'

class SectorDeleteView(DetailView):
    model = Sector
    context_object_name = 'sector'
    template_name = 'offices/sector_delete.html'
