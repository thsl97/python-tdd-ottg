from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ViewAndAddToList.as_view(), name='view_list'),
    url(r'^new$', views.NewListView.as_view(), name='new_list'),
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
]
