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

### Login Credentials
<b>Username</b>: argho <br>
<b>Password</b>: 12345678! <br> <br>
Note: <em> If the login fails, please register a user with the credentials above as this user is necessary for the site to function properly. You can register and use any other user on the site but it is vital that this user exists in the database. </em>

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
