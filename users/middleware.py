from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def registration_page(request):
    return redirect('users:')
