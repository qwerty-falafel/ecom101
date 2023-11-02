from django.apps import AppConfig
from django.contrib.auth import get_user_model

class SocialConfig(AppConfig):
    name = 'social'

    def ready(self):
        from actstream import registry
        from .models import UserProfilePost  # Your custom model
        User = get_user_model()
        registry.register(User)  # Registering the User model
        registry.register(UserProfilePost)  # Registering your custom model
