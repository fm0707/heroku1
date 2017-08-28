from django.shortcuts import render
from .forms import DakokuForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app1.models import WorkHistory
import datetime

# Create your views here.
@login_required
def dakoku(request):
    if request.method == 'POST' :
        form = DakokuForm(request.POST)
        login_user_id = request.user.id
        login_user = request.user
        status = request.POST["text"]
        t = datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")
        wh = WorkHistory(user=login_user, status=status, update_date=t)
        wh.save()
        
        return render(request, 'form.html',  { 'form' :  form })
    else:	
        form = DakokuForm()
        return render(request, 'form.html', {
        'form': form
        })
