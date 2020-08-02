# CancerPrediction_Web
Web page &amp; Server

## Settings
```
$sudo apt-get install python3.6
$sudo apt install python3-venv
$cd [project name]
$python3 -m venv [venv]
$source [venv]/bin/activate
$pip3 install Flask
```

## PROJECT STRUCTURE
```
< PROJECT ROOT >
   |
   |-- app/  
   |    |-- __init__.py             
   |    |-- base/                                # base page for main page
   |    |    |-- static/
   |    |    |    |-- <css, JS, images>          # CSS files, Javascripts 
   |    |    |
   |    |    |-- templates/                      # Templates used to render pages
   |    |         |
   |    |         |-- side/                  
   |    |         |    |-- navigation.html       
   |    |         |    |-- sidebar.html          
   |    |         |    |-- footer.html           
   |    |         |    |-- scripts.html          
   |    |         |
   |    |         |-- layouts/                  
   |    |              |-- base.html             
   |    |            
   |    |-- main/                               # main page Blueprint
   |         |-- templates/           
   |              |
   |              |-- index.html        
   |              |-- *.html          
   |              |-- routes.py
   |              |-- __init__.py                
   |
   |-- requirements.txt          
   |-- .env                      # Inject Configuration via Environment
   |-- config.py                 # Set up the app
   |-- run.py                    
   |
   |-- ************************************************************************
```