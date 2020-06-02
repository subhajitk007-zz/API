import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_api_app.settings')


import django
django.setup()

from api_basic.models import User,ActivityPeriod
from faker import Faker

fakegen = Faker()
print(fakegen)

def populate(N=5):

  for entry in range(N):
    fake_id = fakegen.id()
    fake_name = fakegen.name()
    fake_tz = fakegen.timezone()
    fake_email = fakegen.email()

    user = User.objects.get_or_create(id=fake_id,real_name=fake_name,email=fake_email,tz=fake_tz)[0]

if __name__ == '__main__':
  print("Populating script")
  populate(20)
  print("COMPLETE")
