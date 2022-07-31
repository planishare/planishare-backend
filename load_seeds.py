# script to load seeds

import os

os.system("echo Loading seeds...")

# https://shorturl.ae/eSrjv
os.system("python manage.py loaddata ./seeds/region.json")
os.system("python manage.py loaddata ./seeds/commune.json")
print("Locations done!")

# https://shorturl.ae/2OlMJ
os.system("python manage.py loaddata ./seeds/education.json")
os.system("python manage.py loaddata ./seeds/institutionType.json")
os.system("python manage.py loaddata ./seeds/institution.json")
print("Occupations done!")

# https://shorturl.ae/6YqkP
os.system("python manage.py loaddata ./seeds/academicLevel.json")
os.system("python manage.py loaddata ./seeds/subject.json")
os.system("python manage.py loaddata ./seeds/axis.json")
print("Posts done!")

os.system("python manage.py loaddata ./seeds/reportType.json")
print("Reports done!")

print("Seeds loaded!")
print("Nota: revisar ./seeds/load_seeds.py para ver como crear una seed :)")
# Se pueden crea una seed con el siguiente comando
# python -Xutf8 manage.py dumpdata <app name>.<model name> -o <file name>
# python -Xutf8 manage.py dumpdata <app name>.<model name> <app name>.<model name> -o <file name>
# python -Xutf8 manage.py dumpdata <app name> -o <file name>
# Ejemplo: python -Xutf8 manage.py dumpdata reports.reportType -o .\seeds\reportType.json