#! /bin/sh
source /.cp/bin/activate
./manage.py makemigrations
./manage.py migrate
#/.cp/bin/python ./manage.py shell -c "from django.contrib.auth.models import User; \
 #                          User.objects.create_superuser('john','', '123')"
./manage.py shell -c "from django.contrib.auth.models import User; \
                           User.objects.filter(username='john').exists() or \
                           User.objects.create_superuser('john',
                           '', '123')" 
./manage.py runserver 172.18.0.4:80
