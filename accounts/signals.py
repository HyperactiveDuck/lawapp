from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.management import call_command

@receiver(post_migrate)
def create_default_users(sender, **kwargs):
    """Create default users after migrations are complete"""
    if sender.name == 'accounts':
        try:
            call_command('create_default_users')
        except Exception as e:
            print(f"Could not create default users: {e}")
