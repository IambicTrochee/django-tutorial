from django.shortcuts import render

# Create your views here.
def message_list(request):
    return render(request, 'form/message_list.html', {})