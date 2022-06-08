echo "Creating seeds..."

python -Xutf8 manage.py dumpdata locations.region -o .\seeds\region.json;
python -Xutf8 manage.py dumpdata locations.commune -o .\seeds\commune.json;
echo "Locations done!"

python -Xutf8 manage.py dumpdata occupations.education -o .\seeds\education.json;
python -Xutf8 manage.py dumpdata occupations.institution -o .\seeds\institution.json;
python -Xutf8 manage.py dumpdata occupations.institutionType -o .\seeds\institutionType.json;
echo "Occupations done!"

python -Xutf8 manage.py dumpdata posts.subject -o .\seeds\subject.json;
python -Xutf8 manage.py dumpdata posts.axis -o .\seeds\axis.json;
python -Xutf8 manage.py dumpdata posts.academicLevel -o .\seeds\academicLevel.json;
echo "Posts done!"
echo "Seeds created :)"