#! /bin/sh
/.env/bin/python ./manage.py makemigrations
/.env/bin/python ./manage.py migrate
#/.cp/bin/python ./manage.py shell -c "from django.contrib.auth.models import User; \
 #                          User.objects.create_superuser('john','', '123')"
/.env/bin/python ./manage.py shell -c "from django.contrib.auth.models import User; \
                           User.objects.filter(username='john').exists() or \
                           User.objects.create_superuser('john',
                           '', '123')" 
/.env/bin/python./manage.py runserver 0.0.0.0:80
