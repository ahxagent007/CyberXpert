from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import UserAccount

def is_user_logged_in(user):
    if user.is_authenticated:
        return True
    else:
        return False

def is_admin_logged_in(user):
    if user.is_authenticated:
        user_account = UserAccount.objects.get(id=user.id)
        if user_account.role == 'ADMIN':
            return True
        else:
            return False
    else:
        print()
        return False

def login_access_only(view_to_return="User:Login"):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not is_user_logged_in(request.user):
                messages.error(request, "You cannot access \
                                LOG IN PLEASE !")
                return redirect(view_to_return)
            return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def admin_access_only(view_to_return="User:Login"):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not is_admin_logged_in(request.user):
                messages.error(request, "You cannot access \
                                ADMIN ACCESS NEEDED !")
                request.session['error_message'] = 'You cannot access ADMIN ACCESS NEEDED !'
                return redirect(view_to_return)
            return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator