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
    shains = User.objects.raw('select auth_user.id, username, (select update_date from app1_workhistory where app1_workhistory.id = auth_user.id order by update_date desc limit 1) as update_date from auth_user')
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


