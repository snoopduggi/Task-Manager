
from django.urls import path
from .views import home  # Import a web-based view

urlpatterns = [
    path('', home, name='home'),  # Serves /tasks/ with an HTML page
]
