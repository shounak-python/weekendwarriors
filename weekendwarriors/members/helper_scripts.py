#!/usr/bin/env python
# coding: utf-8

# In[104]:


import pandas as pd
import json
from datetime import date
from members.models import Attendance, Balance, Club, Player, Foot, FieldPosition, Proficiency, Member


def current_balance():
    df = pd.read_csv("members/balance.csv")
    cols = [df.columns[0]] + df.columns[-7:].tolist()
    df = df[cols]
    df.drop([0, 1], axis=0, inplace=True)
    cols = df.columns.tolist()
    cols[0] = None
    df.columns = cols
    df = df.T
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.reset_index()
    df.columns = [str(name).strip().replace(" ", "_") for name in df.columns.tolist()]
    df = df.rename({"index": "Date"}, axis=1)
    balance_df = df[df["Date"] == "Balance"].copy()
    balance_df = balance_df[balance_df.columns[1:]]
    current_balance = balance_df.iloc[0].to_dict()
    with open("members/current_balance.json", "w") as json_file:
        json.dump({str(Date.today()): current_balance}, json_file)
    return current_balance


def populate_attendance():
    df = pd.read_csv("members/balance.csv")
    cols = [df.columns[0]] + df.columns[-7:].tolist()
    df = df[cols]
    df.drop([0, 1], axis=0, inplace=True)
    cols = df.columns.tolist()
    cols[0] = None
    df.columns = cols
    df = df.T
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.reset_index()
    df = df.rename({"index": "Date"}, axis=1)
    df = df[:-1]
    df.columns = [str(name).strip().replace(" ", "_") for name in df.columns.tolist()]
    df["Date"] = pd.to_datetime(df["Date"])
    for index, row in df.iterrows():
        att = Attendance(
            Date=str(row["Date"]).split(" ")[0],
            Nikhil_Kadukar=row["Nikhil_Kadukar"],
            Rajesh_Sharma=row["Rajesh_Sharma"],
            Omkar_Panda=row["Omkar_Panda"],
            Vinod_Hiwale=row["Vinod_Hiwale"],
            Niraj_Gadhe=row["Niraj_Gadhe"],
            Ritesh_Chambhare=row["Ritesh_Chambhare"],
            Jayant_Wani=row["Jayant_Wani"],
            Neelang_Chaturvedi=row["Neelang_Chaturvedi"],
            Durgesh_Patil=row["Durgesh_Patil"],
            Shanmukha_Vardhan=row["Shanmukha_Vardhan"],
            Rahul_Dhokale=row["Rahul_Dhokale"],
            Amod_Narhari=row["Amod_Narhari"],
            Kunal_Aswale=row["Kunal_Aswale"],
            Sameer_Shewale=row["Sameer_Shewale"],
            Vaibhav_Sonar=row["Vaibhav_Sonar"],
            Prem_Jadhav=row["Prem_Jadhav"],
            Chirag=row["Chirag"],
            Dilip_Mahajan=row["Dilip_Mahajan"],
            Vijay_Pal=row["Vijay_Pal"],
            Shounak_Deshpande=row["Shounak_Deshpande"],
            Adwait_Sarnobat=row["Adwait_Sarnobat"],
            Umesh=row["Umesh"],
            Ankit=row["Ankit"],
            Satheesh=row["Satheesh"],
            Varun=row["Varun"],
            Prasad=row["Prasad"],
            Vinit=row["Vinit"],
            Sahil=row["Sahil"],
            Arun=row["Arun"],
            Souvik=row["Souvik"],
            Tuahar=row["Tuahar"],
            Sujit=row["Sujit"],
            Shreekant=row["Shreekant"],
        )
        att.save()


def populate_balance():
    with open("members/current_balance.json", "r") as json_file:
        current_balance = json.load(json_file)

    for key, val in current_balance.items():
        bal = Balance(
            Date=key,
            Nikhil_Kadukar=val["Nikhil_Kadukar"],
            Rajesh_Sharma=val["Rajesh_Sharma"],
            Omkar_Panda=val["Omkar_Panda"],
            Vinod_Hiwale=val["Vinod_Hiwale"],
            Niraj_Gadhe=val["Niraj_Gadhe"],
            Ritesh_Chambhare=val["Ritesh_Chambhare"],
            Jayant_Wani=val["Jayant_Wani"],
            Neelang_Chaturvedi=val["Neelang_Chaturvedi"],
            Durgesh_Patil=val["Durgesh_Patil"],
            Shanmukha_Vardhan=val["Shanmukha_Vardhan"],
            Rahul_Dhokale=val["Rahul_Dhokale"],
            Amod_Narhari=val["Amod_Narhari"],
            Kunal_Aswale=val["Kunal_Aswale"],
            Sameer_Shewale=val["Sameer_Shewale"],
            Vaibhav_Sonar=val["Vaibhav_Sonar"],
            Prem_Jadhav=val["Prem_Jadhav"],
            Chirag=val["Chirag"],
            Dilip_Mahajan=val["Dilip_Mahajan"],
            Vijay_Pal=val["Vijay_Pal"],
            Shounak_Deshpande=val["Shounak_Deshpande"],
            Adwait_Sarnobat=val["Adwait_Sarnobat"],
            Umesh=val["Umesh"],
            Ankit=val["Ankit"],
            Satheesh=val["Satheesh"],
            Varun=val["Varun"],
            Prasad=val["Prasad"],
            Vinit=val["Vinit"],
            Sahil=val["Sahil"],
            Arun=val["Arun"],
            Souvik=val["Souvik"],
            Tuahar=val["Tuahar"],
            Sujit=val["Sujit"],
            Shreekant=val["Shreekant"],
        )
        bal.save()
        

def populate_members():
    df = pd.read_csv("members/input.csv")

    for index, row in df.iterrows():
        (
            first_name,
            last_name,
            image,
            number,
            favorite_club,
            favorite_player,
            preferred_foot,
            preferred_field_position,
            secondary_field_position,
            football_proficiency
        ) = row.values
        football_proficiency = football_proficiency.replace("?","⭐")
        objClub, statusClub = Club.objects.get_or_create(club=favorite_club)
        objPlayer, statusPlayer = Player.objects.get_or_create(player=favorite_player)
        objFoot, statusFoot = Foot.objects.get_or_create(foot=preferred_foot)
        objPreferredFieldPosition, statusFieldPosition = FieldPosition.objects.get_or_create(position=preferred_field_position)
        objSecondaryFieldPosition,statusFieldPosition = FieldPosition.objects.get_or_create(position=secondary_field_position)
        objProficiency, statusProficiency = Proficiency.objects.get_or_create(pro_level=football_proficiency)

        objMember, statusMember = Member.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            image=image,
            number=number,
            favorite_club=objClub,
            favorite_player=objPlayer,
            preferred_foot=objFoot,
            preferred_field_position=objPreferredFieldPosition,
            secondary_field_position=objSecondaryFieldPosition,
            football_proficiency=objProficiency,
        )

