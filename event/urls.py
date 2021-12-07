from django.urls import path, re_path
from event import views

urlpatterns = [
    path('create', views.event_all, name='create'),
    path('list', views.event_all, name='list'),
    # re_path(r'^detail/(?P<pk>[0-9]+)$', views.event_detail),
    path('detail/read/<int:id>', views.event_by_id),
    path('detail/update/<int:id>', views.event_by_id),
    path('detail/delete/<int:id>', views.event_by_id),

    path('time/count/<int:id>', views.get_event_detail),
    # re_path(r'test/list/(?P<id>\d)$', views.event_detail),
    path('test/put', views.get_event_detail2),
    # re_path


]