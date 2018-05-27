from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^main$',views.main),
    url(r'^registration$',views.registration),
    url(r'^customer_Dashboard$',views.customer_Dashboard),
    url(r'^admin_view$',views.admin_view),
    url(r'^add_staff_view$',views.add_staff_view),
    url(r'^staff_adding$',views.staff_adding),
    url(r'^delete_appointment/(?P<id>\d+)$',views.delete_appointment),
    url(r'^delete_appointment_admin/(?P<id>\d+)$',views.delete_appointment_admin),
    url(r'^staff_view$',views.staff_view),
    url(r'^delete_appointment_staff/(?P<id>\d+)$',views.delete_appointment_staff),
    url(r'^staff_delete_first$',views.staff_delete_first),
    url(r'^customer_register$',views.customer_register),
    url(r'^staff_register$',views.staff_register),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^add_appointment$',views.add_appointment),
    url(r'^user_page$',views.user_page),
]

    # url(r'^travel$',views.dashboard),
    # url(r'^create_plan$',views.create_plan),
    # url(r'^destination/(?P<trip_id>\d+)/$',views.trip_view),
    # url(r'^join_trip/(?P<trip_id>\d+)/$',views.join_trip),