from .models import Profile
class ProfileInfo:
    def post(self, *args, **kwargs):
        self.kwargs['pk'] = Profile.objects.first().pk
        return super().post(*args, **kwargs)

    def get(self, *args, **kwargs):
        self.kwargs['pk'] = Profile.objects.first().pk
        return super().get(*args, **kwargs)
