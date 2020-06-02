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
    fake_name = fakegen.name().split()
    print("name")
    print(fake_name)
    fake_first_name = fake_name[0]
    fake_last_name = fake_name[1]
    fake_email = fakegen.email()

    user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
  print("Populating script")
  populate(20)
  print("COMPLETE")
