from django.contrib.auth import get_user_model

User = get_user_model()


class MyPasswordValidator:
    def validate(self, password: str, user: User | None = None):
        return
