echo "Loading seeds..."

# https://shorturl.ae/eSrjv
python manage.py loaddata .\seeds\region.json
python manage.py loaddata .\seeds\commune.json
echo "Locations done!"

# https://shorturl.ae/2OlMJ
python manage.py loaddata .\seeds\education.json
python manage.py loaddata .\seeds\institutionType.json
python manage.py loaddata .\seeds\institution.json
echo "Occupations done!"

# https://shorturl.ae/6YqkP
python manage.py loaddata .\seeds\academicLevel.json
python manage.py loaddata .\seeds\subject.json
python manage.py loaddata .\seeds\axis.json
echo "Posts done!"

python manage.py loaddata .\seeds\reportType.json
echo "Reports done!"

echo "Seeds loaded :)"