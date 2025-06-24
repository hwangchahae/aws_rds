from django.shortcuts import render

# Create your views here.
def board_lists(request):
    return render(request, 'board/lists.html')