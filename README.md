# StudentRegistrationApp (Django + Angular + SQL)

## Functionality
This app can help to add students information, and Registration fee. Also edit, and Delete them.

## Setup

### Backend Setup
-  virtualenv venv --python=python3 
-  source venv/bin/activate 
-  pip3 install -r requirements.txt
-  python3 manage.py makemigrations  
-  python3 manage.py migrate 
-  python3 manage.py runserver  
-  go to http://127.0.0.1:8000/

### Frontend Setup
- npm install -g @angular/cli  
  - (if this doesnt work then follow the next step)
- deactivate 
- sudo npm install -g @angular/cli  
- cd frond-end 
- ng serve  
- go to http://localhost:4200/
