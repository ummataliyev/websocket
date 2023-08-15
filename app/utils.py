from django.shortcuts import reverse
from django.shortcuts import redirect


def registered_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('register'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view
