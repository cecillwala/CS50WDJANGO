from django.shortcuts import render
import datetime
# Create your views here.
def index (request):
    now = datetime.datetime.now()
    return render(request, "valentines/index.html",
                  {
                      "valentines" : now.month == 5 and now.day == 6
                
                  })