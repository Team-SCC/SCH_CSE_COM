import hashlib
import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csecom.settings")
django.setup()

from django.contrib.auth.hashers import make_password

data = pd.read_csv('C:/Users/dldls/바탕 화면/before_table.csv', encoding='utf-8')
sha_list = []

for i in data['password']:
    i = str(i)
    i = make_password(i)
    sha_list.append(i)

data['password'] = sha_list

data.to_csv('C:/Users/dldls/바탕 화면/common_user.csv', index=False)
