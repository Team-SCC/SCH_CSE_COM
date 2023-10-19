import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csecom.settings")
django.setup()

from django.contrib.auth.hashers import make_password

data = pd.read_excel('C:/Users/dldls/OneDrive/바탕 화면/학과홈페이지 개발/common_user 디비초안.xlsx')
sha_list = []

for i in data['password']:
    i = str(i)
    i = make_password(i)
    sha_list.append(i)

data['password'] = sha_list

data.to_csv('C:/Users/dldls/OneDrive/바탕 화면/학과홈페이지 개발/common_user.csv', index=False)
