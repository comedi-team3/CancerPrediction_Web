# CancerPrediction_Web
Web page &amp; Server


## Install
### Using Dockerfile
#### 1. Start Server
```
$ docker build -t <image name> .
$ docker run -d -p <port number>:80 <image name>
```

#### 2. Access Web Page
```
localhost:<port number>
```

### Or using docker-compose
#### 1. Start Server
```
$ docker-compose up
```

#### 2. Access Web Page
```
localhost:4000
```


## PROJECT STRUCTURE
```
< PROJECT ROOT >
   |  
   |-- input/                     # 업로드한 파일 저장 
   |-- model/                     # 모델
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
   |    |-- home/
   |    |    |-- index.html         # main page                  
   |    |    |-- performance.html   # model performance page                                                   
   |    |
   |    |-- cancer_result/       # 
   |
   |-- Dockerfile          
   |-- requirements.txt          
   |-- .env                      # Inject Configuration via Environment
   |-- config.py                 # Set up the app
   |-- run.py                    
```