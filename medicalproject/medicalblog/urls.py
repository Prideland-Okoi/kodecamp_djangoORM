from django.urls import path
from .views import home_view, about_view, contact_view, service_view, post_details

urlpatterns =[
        path("", home_view),
        path("about/",about_view),
        path("contact/", contact_view),
        path("services/", service_view),
        path("post/", post_details),
]
