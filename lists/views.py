from django.shortcuts import render, redirect
from lists.models import List
from lists.forms import ItemForm, ExistingListItemForm
from django.views.generic import FormView, CreateView


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})


class NewListView(CreateView, HomePageView):

    def form_valid(self, form):
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
