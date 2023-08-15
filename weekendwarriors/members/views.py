from django.shortcuts import render
from members.models import Member, FieldPosition, Attendance, Balance
import pandas as pd
import json

# Create your views here.
def memberlist(request):

    attacker_obj = Member.objects.filter(
        preferred_field_position=FieldPosition.objects.get(position="Attacker")
    )
    midfielder_obj = Member.objects.filter(
        preferred_field_position=FieldPosition.objects.get(position="Midfielder")
    )
    defender_obj = Member.objects.filter(
        preferred_field_position=FieldPosition.objects.get(position="Defender")
    )
    goalkeeper_obj = Member.objects.filter(
        preferred_field_position=FieldPosition.objects.get(position="Goalkeeper")
    )

    member_fields = [
        "date",
        "Nikhil_Kadukar",
        "Rajesh_Sharma",
        "Omkar_Panda",
        "Vinod_Hiwale",
        "Niraj_Gadhe",
        "Ritesh_Chambhare",
        "Jayant_Wani",
        "Neelang_Chaturvedi",
        "Durgesh_Patil",
        "Shanmukha_Vardhan",
        "Rahul_Dhokale",
        "Amod_Narhari",
        "Kunal_Aswale",
        "Sameer_Shewale",
        "Vaibhav_Sonar",
        "Prem_Jadhav",
        "Chirag",
        "Dilip_Mahajan",
        "Vijay_Pal",
        "Shounak_Deshpande",
        "Adwait_Sarnobat",
        "Umesh",
        "Ankit",
        "Satheesh",
        "Varun",
        "Prasad",
        "Vinit",
        "Sahil",
        "Arun",
        "Souvik",
        "Tuahar",
        "Sujit",
        "Shreekant",
    ]

    # balance data
    with open("members/current_balance.json", "r") as json_file:
        balance = json.load(json_file)
        balance_date = list(balance.keys())[0]
        balance_obj = balance[balance_date]
        balance_names = sorted(list(balance_obj.keys()))
        balance_values = [int(balance_obj[name]) for name in balance_names]

    # attendance data
    attendance_query = Attendance.objects.order_by("-date").values(*member_fields)
    df = pd.DataFrame(list(attendance_query), columns=member_fields)
    headers = df.columns.tolist()
    headers = [str(headers[0]).upper()] + sorted(headers[1:])
    attendance_rows = []
    for index, row in df.iterrows():
        attendance_rows.append(row.values.tolist())

    ctx = {
        "attacker_obj": attacker_obj,
        "midfielder_obj": midfielder_obj,
        "defender_obj": defender_obj,
        "goalkeeper_obj": goalkeeper_obj,
        "headers": headers,
        "attendance_rows": attendance_rows,
        "balance_date": balance_date,
        "balance_names": balance_names,
        "balance_values": balance_values,
    }

    return render(request, "members/memberlist.html", ctx)