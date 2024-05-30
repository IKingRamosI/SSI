from functools import wraps
from django.shortcuts import redirect

def session_check(function=None, login_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if 'hash_pwd' is in the session
            if 'pwd' not in request.session:
                return redirect(login_url if login_url else 'login_view')
            
            if request.session['pwd'] != 'c@o123!':
                return redirect(login_url if login_url else 'login_view')

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
