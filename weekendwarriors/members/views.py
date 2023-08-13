from django.shortcuts import render
from members.models import Member, FieldPosition

# Create your views here.
def memberlist(request):

    attacker_obj = Member.objects.filter(preferred_field_position=FieldPosition.objects.get(position='Attacker'))
    midfielder_obj = Member.objects.filter(preferred_field_position=FieldPosition.objects.get(position='Midfielder'))
    defender_obj = Member.objects.filter(preferred_field_position=FieldPosition.objects.get(position='Defender'))
    goalkeeper_obj = Member.objects.filter(preferred_field_position=FieldPosition.objects.get(position='Goalkeeper'))

    ctx = {
        "attacker_obj":attacker_obj,
        "midfielder_obj":midfielder_obj,
        "defender_obj":defender_obj,
        "goalkeeper_obj":goalkeeper_obj,
    }
    return render(request, "members/memberlist.html", ctx)