# booksharing

## How to run
`$ python app/manage.py runserver 0:8000`

### Hosting providers

Cloud
AWS, GCP (google), Azure (microsoft)

Hosting
DigitalOcean


[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/projects/booksharing/app
ExecStart=/home/ubuntu/projects/booksharing/env/bin/gunicorn booksharing.wsgi --workers=4 --bind 0.0.0.0:8000 --timeout=30 --max-requests=10000
ExecStart=/home/ubuntu/projects/booksharing/env/bin/celery -A booksharing beat -l info

[Install]
WantedBy=multi-user.target
