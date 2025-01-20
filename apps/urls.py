from django.urls import path, include

urlpatterns = [
    path('', include("about.urls")),
    path('contact/', include("contact.urls")),
    path('work/', include("work.urls")),
    path('service/', include("service.urls")),
]
