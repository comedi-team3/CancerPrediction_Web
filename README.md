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

## Install
### Start Server
```
$ docker build -t <image name> .
$ docker run -d -p <port number>:80 <image name>
```

### Access Web Page
```
localhost:<port number>
```

## PROJECT STRUCTURE
```
< PROJECT ROOT >
   |  
   |-- static/ 
   |    |-- <css, JS, images>  
   |         
   |-- templates/                                # base page for main page
   |    |-- layouts/
   |    |    |-- base.html
   |    |
   |    |-- side/                     
   |    |    |-- navigation.html                  
   |    |    |-- sidebar.html          
   |    |    |-- footer.html           
   |    |    |-- scripts.html 
   |    |    
   |    |-- index.html                                                
   |
   |-- requirements.txt          
   |-- .env                      # Inject Configuration via Environment
   |-- config.py                 # Set up the app
   |-- run.py                    
```