# CancerPrediction_Web
Web page &amp; Server

## Settings
```
sudo apt-get install python3.6
sudo apt install python3-venv
cd [project name]
python3 -m venv [venv]
source [venv]/bin/activate
pip3 install Flask
```

## PROJECT STRUCTURE
```
< PROJECT ROOT >
   |
   |-- app/                      
   |    |-- base/                
   |    |-- main/                     # main page Blueprint
   |         |-- static/
   |         |    |-- <css, JS, images>          # CSS files, Javascripts files
   |         |
   |         |    |-- <css, JS, images>        
   |         |
   |         |-- templates/           
   |              |
   |              |-- index.html        
   |              |-- *.html          # All other HTML pages
   |              |-- routes.py
   |              |-- __init__.py    
   |   __init__.py              
   |
   |-- requirements.txt          
   |-- .env                      # Inject Configuration via Environment
   |-- config.py                 # Set up the app
   |-- run.py                    
   |
   |-- ************************************************************************
```