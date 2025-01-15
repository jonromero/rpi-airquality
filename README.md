Create an venv

Use pip install -r requirement.txt

## Setting Up a Systemd Service for a Flask Application

Follow these steps to create and configure a `systemd` service to run your Flask application at boot:

### **1. Create a Service File**
Create a new `systemd` service file:
```bash
sudo nano /etc/systemd/system/flask-app.service

[Unit]
Description=Flask Application
After=network.target

[Service]
User=god
WorkingDirectory=/home/god/Sources/rpi-airquality/
Environment="PATH=/home/god/Sources/rpi-airquality/venv/bin"
ExecStart=/home/god/Sources/rpi-airquality/venv/bin/flask run --host=0.0.0.0

[Install]
WantedBy=multi-user.target


sudo systemctl daemon-reload

sudo systemctl enable flask-app

sudo systemctl start flask-app

sudo systemctl status flask-app
