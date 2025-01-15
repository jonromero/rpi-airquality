Create an venv

Use pip install -r requirement.txt

Create a Service File:

bash
Copy code
sudo nano /etc/systemd/system/flask-app.service
Add the Following Configuration:

plaintext
Copy code
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
Reload Systemd:

bash
Copy code
sudo systemctl daemon-reload
Enable the Service:

bash
Copy code
sudo systemctl enable flask-app
Start the Service:

bash
Copy code
sudo systemctl start flask-app
Check the Service Status:

bash
Copy code
sudo systemctl status flask-app
