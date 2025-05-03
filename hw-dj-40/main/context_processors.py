from django.contrib.auth.models import User

def all_users_and_user_groups(request):
    users = User.objects.all()
    user_groups = []

    if request.user.is_authenticated:
        user_groups = request.user.groups.all()

    return {
        'all_users': users,
        'user_groups': user_groups,
    }
