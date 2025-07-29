from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

class Command(BaseCommand):
    help = 'Create default users for the application'

    def handle(self, *args, **options):
        # Default users data
        default_users = [
            {
                'username': 'default_client',
                'email': 'client@example.com',
                'password': 'defaultpass123',
                'user_type': 'client',
                'first_name': 'Default',
                'last_name': 'Client'
            },
            {
                'username': 'default_lawyer',
                'email': 'lawyer@example.com',
                'password': 'defaultpass123',
                'user_type': 'provider',
                'first_name': 'Default',
                'last_name': 'Lawyer'
            }
        ]

        created_count = 0
        
        for user_data in default_users:
            try:
                # Check if user already exists
                if not User.objects.filter(username=user_data['username']).exists():
                    user = User.objects.create_user(
                        username=user_data['username'],
                        email=user_data['email'],
                        password=user_data['password'],
                        user_type=user_data['user_type'],
                        first_name=user_data['first_name'],
                        last_name=user_data['last_name']
                    )
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Successfully created {user_data["user_type"]} user: {user_data["username"]}'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f'User {user_data["username"]} already exists, skipping...'
                        )
                    )
            except IntegrityError as e:
                self.stdout.write(
                    self.style.ERROR(
                        f'Error creating user {user_data["username"]}: {str(e)}'
                    )
                )

        if created_count > 0:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created {created_count} default users.')
            )
        else:
            self.stdout.write(
                self.style.WARNING('No new users were created.')
            )
