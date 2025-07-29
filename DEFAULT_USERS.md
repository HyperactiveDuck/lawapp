# Default Users

This application automatically creates two default users every time it launches:

## Default Client User
- **Username:** `default_client`
- **Email:** `client@example.com`
- **Password:** `defaultpass123`
- **User Type:** Client (Müvekkil)
- **Name:** Default Client

## Default Lawyer User
- **Username:** `default_lawyer`
- **Email:** `lawyer@example.com`
- **Password:** `defaultpass123`
- **User Type:** Provider/Lawyer (Avukat)
- **Name:** Default Lawyer

## How it works

The default users are created automatically when:
1. You run `python manage.py migrate` (first time setup)
2. The Django application starts up (through signals)

The system is smart enough to not create duplicate users if they already exist.

## Manual creation

You can also manually create the default users by running:
```bash
python manage.py create_default_users
```

## Customization

To modify the default users, edit the file:
`accounts/management/commands/create_default_users.py`

## Security Note

**Important:** Change these default passwords in production! These are meant for development and testing purposes only.
