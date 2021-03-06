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
    msg = ''
    if request.method == 'POST' :
        form = DakokuForm(request.POST)
        login_user = request.user
        status = request.POST["text"]
        
        location = request.POST["location"]
        logger.info(location)
             
        t = datetime.now(timezone('UTC'))
        logger.info(t)
        
        wh = WorkHistory(user=login_user, status=status, update_date=t, location=location)
        wh.save()
        
        return render(request, 'form.html',  { 'form' :  form , 'username': username, 'msg':  '打刻しました'})
    else:	
        form = DakokuForm()
        return render(request, 'form.html', {'form': form, 'username': username})
