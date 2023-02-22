echo "BUILD STARTED"
pip install -r requirements.txt
python3.9 manage.py collectstatic
echo "BUILD ENDED"