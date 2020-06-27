from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from lists.models import List
from lists.forms import ItemForm, ExistingListItemForm, NewListForm
from django.views.generic import FormView, CreateView, DetailView


User = get_user_model()


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


class ViewAndAddToList(DetailView, CreateView):
    model = List
    template_name = 'list.html'
    form_class = ExistingListItemForm

    def __init__(self):
        super(ViewAndAddToList, self).__init__()
        self.object = None

    def get_form(self, *args, **kwargs):
        self.object = self.get_object()
        return self.form_class(for_list=self.object, data=self.request.POST)


def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})


def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})
