from django.shortcuts import render
from .models import GuestBookEntry

def index(request):
    entries = GuestBookEntry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'guestbook/index.html', {'entries': entries})
