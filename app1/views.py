from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.template import RequestContext
from app1.models import WorkHistory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import logging


# Create your views here.
@login_required
def shain(request):
    # データベース上のIPアドレス情報を配列型で取得
    # shains = Shain.objects.all().order_by('shain_id')
    #shains = User.objects.filter(workhistory__user__isnull=False).order_by('id').values("id", "username", "update_date")
    #shains = User.objects.raw('select auth_user.id, username, (select update_date from #app1_workhistory where app1_workhistory.id = auth_user.id order by update_date desc limit #1) as update_date from auth_user')
    shains = User.objects.raw("select auth_user.id, username, s.update_date as start_time, e.update_date as end_time, s.location as s_location, e.location as e_location  from auth_user left outer join (select user_id, MAX(update_date) + INTERVAL 9 HOUR as update_date, location from app1_workhistory where status = '1' group by user_id, location) s on auth_user.id = s.user_id left outer join (select user_id, MAX(update_date) + INTERVAL 9 HOUR as update_date , location from app1_workhistory where status = '0' group by user_id, location) e on auth_user.id = e.user_id")
    context = {'shains' : shains }
    logger = logging.getLogger('command')
    logger.info(shains)

    return  render(
        request,
        'shain.html', # テンプレート名を指定
        context
        #{'shains' : shains }, # 取得したIPアドレス情報をテンプレート内の変数に代入
        #context_instance=RequestContext(request)
        )


