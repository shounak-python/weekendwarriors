from django.shortcuts import render
from members.models import Member, FieldPosition, Attendance, Balance
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.status import HTTP_200_OK, HTTP_406_NOT_ACCEPTABLE
import pandas as pd
import json
import datetime

# Create your views here.

member_fields = [
    "Date",
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


def memberlist(request):
    global member_fields
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

    # balance data
    balance = Balance.objects.order_by("-Date").values(*member_fields).first()
    balance_date = str(balance["Date"])
    del balance["Date"]
    balance_names = sorted(list(balance.keys()))
    balance_values = [int(balance[name]) for name in balance_names]

    # attendance data
    attendance_query = Attendance.objects.order_by("-Date").values(*member_fields)
    df = pd.DataFrame(list(attendance_query), columns=member_fields)
    headers = df.columns.tolist()
    headers = [str(headers[0]).title()] + sorted(headers[1:])
    attendance_rows = []
    for index, row in df.iterrows():
        row_dict = dict(row)
        attendance_rows.append([row_dict[header] for header in headers])

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


@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminUser])
def deduct_group(requests):
    """
    payload format should be {"Date":yyyy-mm-dd, 'Player1':'Deduction Amount', 'Player2':'Deduction Amount'} <br>
    Use below payload to create your payload. <br>
    For those who were present, replace 0 with the per head contribution to be deducted from their balance. <br>
    {<br>
    "Date":"2023-08-20", <br>
    "Adwait_Sarnobat":0, <br>
    "Amod_Narhari":0, <br>
    "Ankit":0, <br>
    "Arun":0, <br>
    "Chirag":0, <br>
    "Dilip_Mahajan":0, <br>
    "Durgesh_Patil":0, <br>
    "Jayant_Wani":0, <br>
    "Kunal_Aswale":0, <br>
    "Neelang_Chaturvedi":0, <br>
    "Nikhil_Kadukar":0, <br>
    "Niraj_Gadhe":0, <br>
    "Omkar_Panda":0, <br>
    "Prasad":0, <br>
    "Prem_Jadhav":0, <br>
    "Rahul_Dhokale":0, <br>
    "Rajesh_Sharma":0, <br>
    "Ritesh_Chambhare":0, <br>
    "Sahil":0, <br>
    "Sameer_Shewale":0, <br>
    "Satheesh":0, <br>
    "Shanmukha_Vardhan":0, <br>
    "Shounak_Deshpande":0, <br>
    "Shreekant":0, <br>
    "Souvik":0, <br>
    "Sujit":0, <br>
    "Tuahar":0, <br>
    "Umesh":0, <br>
    "Vaibhav_Sonar":0, <br>
    "Varun":0, <br>
    "Vijay_Pal":0, <br>
    "Vinit":0, <br>
    "Vinod_Hiwale":0 <br>
        }
    """
    global member_fields
    payload = dict(requests.data)
    for key in member_fields:
        if key not in payload.keys():
            resp = {"message": f"key-value pair for {key} is missing"}
            return Response(json.dumps(resp), status=HTTP_406_NOT_ACCEPTABLE)

    match_date = payload["Date"]

    try:
        datetime.date.fromisoformat(match_date)
    except ValueError:
        resp = {
            "message": f"Entered date format {match_date} is incorrect, should be YYYY-MM-DD"
        }
        return Response(json.dumps(resp), status=HTTP_406_NOT_ACCEPTABLE)

    Adwait_Sarnobat = int(payload["Adwait_Sarnobat"])
    Amod_Narhari = int(payload["Amod_Narhari"])
    Ankit = int(payload["Ankit"])
    Arun = int(payload["Arun"])
    Chirag = int(payload["Chirag"])
    Dilip_Mahajan = int(payload["Dilip_Mahajan"])
    Durgesh_Patil = int(payload["Durgesh_Patil"])
    Jayant_Wani = int(payload["Jayant_Wani"])
    Kunal_Aswale = int(payload["Kunal_Aswale"])
    Neelang_Chaturvedi = int(payload["Neelang_Chaturvedi"])
    Nikhil_Kadukar = int(payload["Nikhil_Kadukar"])
    Niraj_Gadhe = int(payload["Niraj_Gadhe"])
    Omkar_Panda = int(payload["Omkar_Panda"])
    Prasad = int(payload["Prasad"])
    Prem_Jadhav = int(payload["Prem_Jadhav"])
    Rahul_Dhokale = int(payload["Rahul_Dhokale"])
    Rajesh_Sharma = int(payload["Rajesh_Sharma"])
    Ritesh_Chambhare = int(payload["Ritesh_Chambhare"])
    Sahil = int(payload["Sahil"])
    Sameer_Shewale = int(payload["Sameer_Shewale"])
    Satheesh = int(payload["Satheesh"])
    Shanmukha_Vardhan = int(payload["Shanmukha_Vardhan"])
    Shounak_Deshpande = int(payload["Shounak_Deshpande"])
    Shreekant = int(payload["Shreekant"])
    Souvik = int(payload["Souvik"])
    Sujit = int(payload["Sujit"])
    Tuahar = int(payload["Tuahar"])
    Umesh = int(payload["Umesh"])
    Vaibhav_Sonar = int(payload["Vaibhav_Sonar"])
    Varun = int(payload["Varun"])
    Vijay_Pal = int(payload["Vijay_Pal"])
    Vinit = int(payload["Vinit"])
    Vinod_Hiwale = int(payload["Vinod_Hiwale"])

    # Update Attendance
    attendance_model_obj = Attendance(
        Date=match_date,
        Adwait_Sarnobat=Adwait_Sarnobat,
        Amod_Narhari=Amod_Narhari,
        Ankit=Ankit,
        Arun=Arun,
        Chirag=Chirag,
        Dilip_Mahajan=Dilip_Mahajan,
        Durgesh_Patil=Durgesh_Patil,
        Jayant_Wani=Jayant_Wani,
        Kunal_Aswale=Kunal_Aswale,
        Neelang_Chaturvedi=Neelang_Chaturvedi,
        Nikhil_Kadukar=Nikhil_Kadukar,
        Niraj_Gadhe=Niraj_Gadhe,
        Omkar_Panda=Omkar_Panda,
        Prasad=Prasad,
        Prem_Jadhav=Prem_Jadhav,
        Rahul_Dhokale=Rahul_Dhokale,
        Rajesh_Sharma=Rajesh_Sharma,
        Ritesh_Chambhare=Ritesh_Chambhare,
        Sahil=Sahil,
        Sameer_Shewale=Sameer_Shewale,
        Satheesh=Satheesh,
        Shanmukha_Vardhan=Shanmukha_Vardhan,
        Shounak_Deshpande=Shounak_Deshpande,
        Shreekant=Shreekant,
        Souvik=Souvik,
        Sujit=Sujit,
        Tuahar=Tuahar,
        Umesh=Umesh,
        Vaibhav_Sonar=Vaibhav_Sonar,
        Varun=Varun,
        Vijay_Pal=Vijay_Pal,
        Vinit=Vinit,
        Vinod_Hiwale=Vinod_Hiwale,
    )
    attendance_model_obj.save()

    attendance_dict = {
        "Date": match_date,
        "Adwait_Sarnobat": Adwait_Sarnobat,
        "Amod_Narhari": Amod_Narhari,
        "Ankit": Ankit,
        "Arun": Arun,
        "Chirag": Chirag,
        "Dilip_Mahajan": Dilip_Mahajan,
        "Durgesh_Patil": Durgesh_Patil,
        "Jayant_Wani": Jayant_Wani,
        "Kunal_Aswale": Kunal_Aswale,
        "Neelang_Chaturvedi": Neelang_Chaturvedi,
        "Nikhil_Kadukar": Nikhil_Kadukar,
        "Niraj_Gadhe": Niraj_Gadhe,
        "Omkar_Panda": Omkar_Panda,
        "Prasad": Prasad,
        "Prem_Jadhav": Prem_Jadhav,
        "Rahul_Dhokale": Rahul_Dhokale,
        "Rajesh_Sharma": Rajesh_Sharma,
        "Ritesh_Chambhare": Ritesh_Chambhare,
        "Sahil": Sahil,
        "Sameer_Shewale": Sameer_Shewale,
        "Satheesh": Satheesh,
        "Shanmukha_Vardhan": Shanmukha_Vardhan,
        "Shounak_Deshpande": Shounak_Deshpande,
        "Shreekant": Shreekant,
        "Souvik": Souvik,
        "Sujit": Sujit,
        "Tuahar": Tuahar,
        "Umesh": Umesh,
        "Vaibhav_Sonar": Vaibhav_Sonar,
        "Varun": Varun,
        "Vijay_Pal": Vijay_Pal,
        "Vinit": Vinit,
        "Vinod_Hiwale": Vinod_Hiwale,
    }

    # Update Current Balance
    balance = Balance.objects.order_by("-Date").values(*member_fields).first()

    Updated_Adwait_Sarnobat = int(balance["Adwait_Sarnobat"]) - Adwait_Sarnobat
    Updated_Amod_Narhari = int(balance["Amod_Narhari"]) - Amod_Narhari
    Updated_Ankit = int(balance["Ankit"]) - Ankit
    Updated_Arun = int(balance["Arun"]) - Arun
    Updated_Chirag = int(balance["Chirag"]) - Chirag
    Updated_Dilip_Mahajan = int(balance["Dilip_Mahajan"]) - Dilip_Mahajan
    Updated_Durgesh_Patil = int(balance["Durgesh_Patil"]) - Durgesh_Patil
    Updated_Jayant_Wani = int(balance["Jayant_Wani"]) - Jayant_Wani
    Updated_Kunal_Aswale = int(balance["Kunal_Aswale"]) - Kunal_Aswale
    Updated_Neelang_Chaturvedi = int(balance["Neelang_Chaturvedi"]) - Neelang_Chaturvedi
    Updated_Nikhil_Kadukar = int(balance["Nikhil_Kadukar"]) - Nikhil_Kadukar
    Updated_Niraj_Gadhe = int(balance["Niraj_Gadhe"]) - Niraj_Gadhe
    Updated_Omkar_Panda = int(balance["Omkar_Panda"]) - Omkar_Panda
    Updated_Prasad = int(balance["Prasad"]) - Prasad
    Updated_Prem_Jadhav = int(balance["Prem_Jadhav"]) - Prem_Jadhav
    Updated_Rahul_Dhokale = int(balance["Rahul_Dhokale"]) - Rahul_Dhokale
    Updated_Rajesh_Sharma = int(balance["Rajesh_Sharma"]) - Rajesh_Sharma
    Updated_Ritesh_Chambhare = int(balance["Ritesh_Chambhare"]) - Ritesh_Chambhare
    Updated_Sahil = int(balance["Sahil"]) - Sahil
    Updated_Sameer_Shewale = int(balance["Sameer_Shewale"]) - Sameer_Shewale
    Updated_Satheesh = int(balance["Satheesh"]) - Satheesh
    Updated_Shanmukha_Vardhan = int(balance["Shanmukha_Vardhan"]) - Shanmukha_Vardhan
    Updated_Shounak_Deshpande = int(balance["Shounak_Deshpande"]) - Shounak_Deshpande
    Updated_Shreekant = int(balance["Shreekant"]) - Shreekant
    Updated_Souvik = int(balance["Souvik"]) - Souvik
    Updated_Sujit = int(balance["Sujit"]) - Sujit
    Updated_Tuahar = int(balance["Tuahar"]) - Tuahar
    Updated_Umesh = int(balance["Umesh"]) - Umesh
    Updated_Vaibhav_Sonar = int(balance["Vaibhav_Sonar"]) - Vaibhav_Sonar
    Updated_Varun = int(balance["Varun"]) - Varun
    Updated_Vijay_Pal = int(balance["Vijay_Pal"]) - Vijay_Pal
    Updated_Vinit = int(balance["Vinit"]) - Vinit
    Updated_Vinod_Hiwale = int(balance["Vinod_Hiwale"]) - Vinod_Hiwale

    balance_model_obj = Balance(
        Date=match_date,
        Adwait_Sarnobat=Updated_Adwait_Sarnobat,
        Amod_Narhari=Updated_Amod_Narhari,
        Ankit=Updated_Ankit,
        Arun=Updated_Arun,
        Chirag=Updated_Chirag,
        Dilip_Mahajan=Updated_Dilip_Mahajan,
        Durgesh_Patil=Updated_Durgesh_Patil,
        Jayant_Wani=Updated_Jayant_Wani,
        Kunal_Aswale=Updated_Kunal_Aswale,
        Neelang_Chaturvedi=Updated_Neelang_Chaturvedi,
        Nikhil_Kadukar=Updated_Nikhil_Kadukar,
        Niraj_Gadhe=Updated_Niraj_Gadhe,
        Omkar_Panda=Updated_Omkar_Panda,
        Prasad=Updated_Prasad,
        Prem_Jadhav=Updated_Prem_Jadhav,
        Rahul_Dhokale=Updated_Rahul_Dhokale,
        Rajesh_Sharma=Updated_Rajesh_Sharma,
        Ritesh_Chambhare=Updated_Ritesh_Chambhare,
        Sahil=Updated_Sahil,
        Sameer_Shewale=Updated_Sameer_Shewale,
        Satheesh=Updated_Satheesh,
        Shanmukha_Vardhan=Updated_Shanmukha_Vardhan,
        Shounak_Deshpande=Updated_Shounak_Deshpande,
        Shreekant=Updated_Shreekant,
        Souvik=Updated_Souvik,
        Sujit=Updated_Sujit,
        Tuahar=Updated_Tuahar,
        Umesh=Updated_Umesh,
        Vaibhav_Sonar=Updated_Vaibhav_Sonar,
        Varun=Updated_Varun,
        Vijay_Pal=Updated_Vijay_Pal,
        Vinit=Updated_Vinit,
        Vinod_Hiwale=Updated_Vinod_Hiwale,
    )
    balance_model_obj.save()

    balance_dict = {
        "Date": match_date,
        "Updated_Adwait_Sarnobat": Updated_Adwait_Sarnobat,
        "Updated_Amod_Narhari": Updated_Amod_Narhari,
        "Updated_Ankit": Updated_Ankit,
        "Updated_Arun": Updated_Arun,
        "Updated_Chirag": Updated_Chirag,
        "Updated_Dilip_Mahajan": Updated_Dilip_Mahajan,
        "Updated_Durgesh_Patil": Updated_Durgesh_Patil,
        "Updated_Jayant_Wani": Updated_Jayant_Wani,
        "Updated_Kunal_Aswale": Updated_Kunal_Aswale,
        "Updated_Neelang_Chaturvedi": Updated_Neelang_Chaturvedi,
        "Updated_Nikhil_Kadukar": Updated_Nikhil_Kadukar,
        "Updated_Niraj_Gadhe": Updated_Niraj_Gadhe,
        "Updated_Omkar_Panda": Updated_Omkar_Panda,
        "Updated_Prasad": Updated_Prasad,
        "Updated_Prem_Jadhav": Updated_Prem_Jadhav,
        "Updated_Rahul_Dhokale": Updated_Rahul_Dhokale,
        "Updated_Rajesh_Sharma": Updated_Rajesh_Sharma,
        "Updated_Ritesh_Chambhare": Updated_Ritesh_Chambhare,
        "Updated_Sahil": Updated_Sahil,
        "Updated_Sameer_Shewale": Updated_Sameer_Shewale,
        "Updated_Satheesh": Updated_Satheesh,
        "Updated_Shanmukha_Vardhan": Updated_Shanmukha_Vardhan,
        "Updated_Shounak_Deshpande": Updated_Shounak_Deshpande,
        "Updated_Shreekant": Updated_Shreekant,
        "Updated_Souvik": Updated_Souvik,
        "Updated_Sujit": Updated_Sujit,
        "Updated_Tuahar": Updated_Tuahar,
        "Updated_Umesh": Updated_Umesh,
        "Updated_Vaibhav_Sonar": Updated_Vaibhav_Sonar,
        "Updated_Varun": Updated_Varun,
        "Updated_Vijay_Pal": Updated_Vijay_Pal,
        "Updated_Vinit": Updated_Vinit,
        "Updated_Vinod_Hiwale": Updated_Vinod_Hiwale,
    }
    resp = {"Message": {"attendance": attendance_dict, "current_balance": balance_dict}}

    return Response(json.dumps(resp), status=HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminUser])
def add(requests):
    """
    Add balance for specific members. Make sure the name matches the names in the database.
    Format:
    {
    "Member1": 100,
    "Member2": 200
    }
    """
    global member_fields
    payload = dict(requests.data)

    for name in payload.keys():
        if name not in member_fields:
            resp = {"message": f"Name {name} not found in database. Existing names in database are {[name for name in member_fields if name != 'Date']}"}
            return Response(json.dumps(resp), status=HTTP_406_NOT_ACCEPTABLE)
        
    add_dict = dict()    
    for name in member_fields:
        if name != "Date":
            if name in payload.keys():
                add_dict[name] = int(payload[name])
            else:
                add_dict[name] = 0
        else:
            add_dict[name] = str(datetime.date.today())

    balance = Balance.objects.order_by("-Date").values(*member_fields).first()

    updated_balance = Balance(
        Date=str(add_dict["Date"]),
        Adwait_Sarnobat=int(balance["Adwait_Sarnobat"]) + int(add_dict["Adwait_Sarnobat"]),
        Amod_Narhari=int(balance["Amod_Narhari"]) + int(add_dict["Amod_Narhari"]),
        Ankit=int(balance["Ankit"]) + int(add_dict["Ankit"]),
        Arun=int(balance["Arun"]) + int(add_dict["Arun"]),
        Chirag=int(balance["Chirag"]) + int(add_dict["Chirag"]),
        Dilip_Mahajan=int(balance["Dilip_Mahajan"]) + int(add_dict["Dilip_Mahajan"]),
        Durgesh_Patil=int(balance["Durgesh_Patil"]) + int(add_dict["Durgesh_Patil"]),
        Jayant_Wani=int(balance["Jayant_Wani"]) + int(add_dict["Jayant_Wani"]),
        Kunal_Aswale=int(balance["Kunal_Aswale"]) + int(add_dict["Kunal_Aswale"]),
        Neelang_Chaturvedi=int(balance["Neelang_Chaturvedi"])
        + int(add_dict["Neelang_Chaturvedi"]),
        Nikhil_Kadukar=int(balance["Nikhil_Kadukar"]) + int(add_dict["Nikhil_Kadukar"]),
        Niraj_Gadhe=int(balance["Niraj_Gadhe"]) + int(add_dict["Niraj_Gadhe"]),
        Omkar_Panda=int(balance["Omkar_Panda"]) + int(add_dict["Omkar_Panda"]),
        Prasad=int(balance["Prasad"]) + int(add_dict["Prasad"]),
        Prem_Jadhav=int(balance["Prem_Jadhav"]) + int(add_dict["Prem_Jadhav"]),
        Rahul_Dhokale=int(balance["Rahul_Dhokale"]) + int(add_dict["Rahul_Dhokale"]),
        Rajesh_Sharma=int(balance["Rajesh_Sharma"]) + int(add_dict["Rajesh_Sharma"]),
        Ritesh_Chambhare=int(balance["Ritesh_Chambhare"])
        + int(add_dict["Ritesh_Chambhare"]),
        Sahil=int(balance["Sahil"]) + int(add_dict["Sahil"]),
        Sameer_Shewale=int(balance["Sameer_Shewale"]) + int(add_dict["Sameer_Shewale"]),
        Satheesh=int(balance["Satheesh"]) + int(add_dict["Satheesh"]),
        Shanmukha_Vardhan=int(balance["Shanmukha_Vardhan"])
        + int(add_dict["Shanmukha_Vardhan"]),
        Shounak_Deshpande=int(balance["Shounak_Deshpande"])
        + int(add_dict["Shounak_Deshpande"]),
        Shreekant=int(balance["Shreekant"]) + int(add_dict["Shreekant"]),
        Souvik=int(balance["Souvik"]) + int(add_dict["Souvik"]),
        Sujit=int(balance["Sujit"]) + int(add_dict["Sujit"]),
        Tuahar=int(balance["Tuahar"]) + int(add_dict["Tuahar"]),
        Umesh=int(balance["Umesh"]) + int(add_dict["Umesh"]),
        Vaibhav_Sonar=int(balance["Vaibhav_Sonar"]) + int(add_dict["Vaibhav_Sonar"]),
        Varun=int(balance["Varun"]) + int(add_dict["Varun"]),
        Vijay_Pal=int(balance["Vijay_Pal"]) + int(add_dict["Vijay_Pal"]),
        Vinit=int(balance["Vinit"]) + int(add_dict["Vinit"]),
        Vinod_Hiwale=int(balance["Vinod_Hiwale"]) + int(add_dict["Vinod_Hiwale"]),
    )
    updated_balance.save()
    resp = f"Balance added for {add_dict}. Check current balance on Member tab for confirmation."
    return Response(json.dumps(resp), status=HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminUser])
def deduct(requests):
    """
    Deduct balance for specific members. Make sure the name matches the names in the database.
    Format:
    {
    "Member1": 100,
    "Member2": 200
    }
    """
    global member_fields
    payload = dict(requests.data)

    for name in payload.keys():
        if name not in member_fields:
            resp = {
                "message": f"Name {name} not found in database. Existing names in database are {[name for name in member_fields if name != 'Date']}"
            }
            return Response

    deduct_dict = dict()
    for name in member_fields:
        if name != "Date":
            if name in payload.keys():
                deduct_dict[name] = int(payload[name])
            else:
                deduct_dict[name] = 0
        else:
            deduct_dict[name] = str(datetime.date.today())

    balance = Balance.objects.order_by("-Date").values(*member_fields).first()

    updated_balance = Balance(
        Date=str(deduct_dict["Date"]),
        Adwait_Sarnobat=int(balance["Adwait_Sarnobat"])
        - int(deduct_dict["Adwait_Sarnobat"]),
        Amod_Narhari=int(balance["Amod_Narhari"]) - int(deduct_dict["Amod_Narhari"]),
        Ankit=int(balance["Ankit"]) - int(deduct_dict["Ankit"]),
        Arun=int(balance["Arun"]) - int(deduct_dict["Arun"]),
        Chirag=int(balance["Chirag"]) - int(deduct_dict["Chirag"]),
        Dilip_Mahajan=int(balance["Dilip_Mahajan"]) - int(deduct_dict["Dilip_Mahajan"]),
        Durgesh_Patil=int(balance["Durgesh_Patil"]) - int(deduct_dict["Durgesh_Patil"]),
        Jayant_Wani=int(balance["Jayant_Wani"]) - int(deduct_dict["Jayant_Wani"]),
        Kunal_Aswale=int(balance["Kunal_Aswale"]) - int(deduct_dict["Kunal_Aswale"]),
        Neelang_Chaturvedi=int(balance["Neelang_Chaturvedi"])
        - int(deduct_dict["Neelang_Chaturvedi"]),
        Nikhil_Kadukar=int(balance["Nikhil_Kadukar"])
        - int(deduct_dict["Nikhil_Kadukar"]),
        Niraj_Gadhe=int(balance["Niraj_Gadhe"]) - int(deduct_dict["Niraj_Gadhe"]),
        Omkar_Panda=int(balance["Omkar_Panda"]) - int(deduct_dict["Omkar_Panda"]),
        Prasad=int(balance["Prasad"]) - int(deduct_dict["Prasad"]),
        Prem_Jadhav=int(balance["Prem_Jadhav"]) - int(deduct_dict["Prem_Jadhav"]),
        Rahul_Dhokale=int(balance["Rahul_Dhokale"]) - int(deduct_dict["Rahul_Dhokale"]),
        Rajesh_Sharma=int(balance["Rajesh_Sharma"]) - int(deduct_dict["Rajesh_Sharma"]),
        Ritesh_Chambhare=int(balance["Ritesh_Chambhare"])
        - int(deduct_dict["Ritesh_Chambhare"]),
        Sahil=int(balance["Sahil"]) - int(deduct_dict["Sahil"]),
        Sameer_Shewale=int(balance["Sameer_Shewale"])
        - int(deduct_dict["Sameer_Shewale"]),
        Satheesh=int(balance["Satheesh"]) - int(deduct_dict["Satheesh"]),
        Shanmukha_Vardhan=int(balance["Shanmukha_Vardhan"])
        - int(deduct_dict["Shanmukha_Vardhan"]),
        Shounak_Deshpande=int(balance["Shounak_Deshpande"])
        - int(deduct_dict["Shounak_Deshpande"]),
        Shreekant=int(balance["Shreekant"]) - int(deduct_dict["Shreekant"]),
        Souvik=int(balance["Souvik"]) - int(deduct_dict["Souvik"]),
        Sujit=int(balance["Sujit"]) - int(deduct_dict["Sujit"]),
        Tuahar=int(balance["Tuahar"]) - int(deduct_dict["Tuahar"]),
        Umesh=int(balance["Umesh"]) - int(deduct_dict["Umesh"]),
        Vaibhav_Sonar=int(balance["Vaibhav_Sonar"]) - int(deduct_dict["Vaibhav_Sonar"]),
        Varun=int(balance["Varun"]) - int(deduct_dict["Varun"]),
        Vijay_Pal=int(balance["Vijay_Pal"]) - int(deduct_dict["Vijay_Pal"]),
        Vinit=int(balance["Vinit"]) - int(deduct_dict["Vinit"]),
        Vinod_Hiwale=int(balance["Vinod_Hiwale"]) - int(deduct_dict["Vinod_Hiwale"]),
    )
    updated_balance.save()

    resp = f"Balance deducted for {deduct_dict}. Check current balance on Member tab for confirmation."
    return Response(json.dumps(resp), status=HTTP_200_OK)
