from django.shortcuts import render
from bulletinboard.models import Bulletin

# Create your views here.

def bulletinlist(request):
    bulletin_query = Bulletin.objects.order_by('-updated_on').all()
    ctx = dict()
    if bulletin_query.count() > 0:
        ctx = {"bulletin_query": bulletin_query}
    return render(request, "bulletinboard/bulletinlist.html", ctx)


def bulletindetail(request, pk:int):
    bulletin = Bulletin.objects.get(pk=pk)
    ctx = {"bulletin": bulletin}
    return render(request, "bulletinboard/bulletindetail.html", ctx)
