from django.views.generic.detail import DetailView
from .models import UserCustom


class ProfielDetailView(DetailView):
    model = UserCustom
    template_name = 'accounts/index.html'
