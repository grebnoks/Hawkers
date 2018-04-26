https://linode.com/docs/web-servers/nginx/deploy-django-applications-using-uwsgi-and-nginx-on-ubuntu-14-04/

https://manager.linode.com/linodes/remote_access/linode7298022



Server: api.rockhawkapp.com
IP: 104.237.132.189
or
http://li808-189.members.linode.com 


Some of what we had to install:

pip install djangorestframework
pip install django-admin-view-permission
pip install psycopg2
pip3 install psycopg2 
apt-get install postresql
apt-get install python-psycopg2
apt-get install libq-dev
python -m pip install pyserial
pip install Pillow


to access database command line from server:

prod/Hawkers# sudo su - postgres
psql mydatabase

API points:
http://localhost:8000/feedback_list/
http://localhost:8000/locationData_list/
http://localhost:8000/trailData_list/
http://localhost:8000/feedback_detail/2/    The 2 is the ID of the specific location
http://localhost:8000/locationData_detail/2/  	  The 2 is the ID of the specific location
http://localhost:8000/trailData_detail/2/  	  The 2 is the ID of the specific location