#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
from members.models import Club, Player, Foot, FieldPosition, Proficiency, Member

def write():
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

