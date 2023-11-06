from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('form/<form_id>', views.display_form),
    path('export', views.export_to_excel),
    path('tesekkurederim', views.tesekkur)
]
