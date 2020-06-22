from django.conf.urls import url, include
from lists import views
from lists import urls as list_urls

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^lists/', include(list_urls)),
]
