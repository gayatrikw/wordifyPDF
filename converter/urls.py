# converter/urls.py
from django.urls import path
from .views import home, about, contact
from .views import convert_file, view_converted_file


urlpatterns = [
    path('convert/', convert_file, name='convert_file'),
    path('view/<int:file_id>/', view_converted_file, name='view_converted_file'),
    path('', home, name='home'),
    path('about/', about, name='about'),  # Add this line
    path('contact/', contact, name='contact'),
]
