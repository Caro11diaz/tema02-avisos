from django.urls import path
from .views import AvisosVigentesListView
app_name = "avisos"
urlpatterns = [
 path("", AvisosVigentesListView.as_view(), name="vigentes"),
]
