from django.views import generic as views

from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.main.models import PetsPhoto


# def show_home(request):
#     context = {
#         'hide_additional_nav_items': True,
#     }
#     return render(request, 'main/home_page.html', context)


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


# def show_dashboard(request):
#     profile = get_profile()
#     if not profile:
#         redirect('main/401')
#     pet_photos = PetsPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile).distinct()
#     context = {
#         'pet_photos': pet_photos,
#     }
#     return render(request, 'main/dashboard.html', context)


class DashboardView(views.ListView):
    model = PetsPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'
