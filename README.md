# CMPUT404Project
## Tests  
 > python manage.py test
## Resources Used:  
Tutorials used for user authentication
 - [Kolawole, M. (2021). FullStack React & Django Authentication : Django REST ,TypeScript, Axios, Redux & React Router. DEV.](https://dev.to/koladev/django-rest-authentication-cmh)
 - 
## Setting up environment

### Backend
    >> virtualenv venv
    >> .\venv\Scripts\activate  
    >> pip install -r requirements.txt
    >> python manage.py runserver

### Frontend
    >> yarn install
    >> yarn start

### Features added post Demo

- We have added frontend tests after the demo.

- We have improved the UI of the loginpage. New loginpage image:
![image](https://user-images.githubusercontent.com/55654485/206632939-2ceac1fa-b4c7-4015-bc39-cfbad5c88787.png)

### Notes about AJAX usage

- Our frontend to backend communication is done through axios, which is basically AJAX under the hood.

### API Documentation

- https://socialdistribution-cmput404.herokuapp.com/docs/

### Notes about Connections

- As mentioned in the Demo, one of the teams still hasn't fixed their schema so their posts (the posts in red background) will still appear to be broken.
