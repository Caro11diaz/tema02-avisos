from django.views.generic import ListView
from django.utils import timezone
from .models import Aviso

class AvisosVigentesListView(ListView):
    model = Aviso
    template_name = "avisos/lista.html" 
    context_object_name = "avisos"

    def get_queryset(self):
        hoy = timezone.localdate()
        return Aviso.objects.filter(
            fecha_inicio__lte=hoy, 
            fecha_fin__gte=hoy
        ).order_by('-fecha_inicio')
