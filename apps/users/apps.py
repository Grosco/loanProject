from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name属性指向此应用程序的完整的 Python 格式的路径，如 'django.contrib.admin'
    name = 'apps.users'
