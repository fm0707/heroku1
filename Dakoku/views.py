from django.shortcuts import render
from .forms import DakokuForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app1.models import WorkHistory
from django.contrib.auth.models import User
from datetime import datetime
from pytz import timezone
import logging

# Create your views here.
@login_required
def dakoku(request):
    logger = logging.getLogger('command')
    shain = User.objects.get(id= request.user.id)
    username = shain.first_name
    if request.method == 'POST' :
        form = DakokuForm(request.POST)
        login_user = request.user
        status = request.POST["text"]
        
        
        t = datetime.now(timezone('UTC'))
        logger.info(t)
        
        wh = WorkHistory(user=login_user, status=status, update_date=t)
        wh.save()
        
        return render(request, 'form.html',  { 'form' :  form , 'username': username })
    else:	
        form = DakokuForm()
        return render(request, 'form.html', {'form': form, 'username': username})
