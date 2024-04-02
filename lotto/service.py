from .models import User

def create_user(name, email, credits):
    user = User.objects.create(name=name, email=email, credits=credits)
    return user

def get_user_by_email(email):
    try:
        user = User.objects.get(email=email)
        return user
    except User.DoesNotExist:
        return None