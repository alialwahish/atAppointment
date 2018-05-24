from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^main$',views.main),
    url(r'^customer_register$',views.customer_register),
    url(r'^staff_register$',views.staff_register),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^add_appointment$',views.add_appointment),
    url(r'^user_page&',views.user_page),
]

    # url(r'^travel$',views.dashboard),
    # url(r'^create_plan$',views.create_plan),
    # url(r'^destination/(?P<trip_id>\d+)/$',views.trip_view),
    # url(r'^join_trip/(?P<trip_id>\d+)/$',views.join_trip),