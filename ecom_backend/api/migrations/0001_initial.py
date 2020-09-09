from django.db import migrations

from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name = "akash",
         email= "akashbittu96@gmail.com",
         is_staff= True,
         is_superuser = True,
         phone = "7002251100",
         gender = "Male")

        user.set_password("bittursp")
        user.save() 

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data), 
    ]