# StudentRegistrationApp (Django + Angular + SQL)

## Functionality
Behold this magnificent creation - a Student Registration app fashioned with the power of Django backend, Angular frontend, and the robustness of SQL database.

This marvel of modern technology allows you to effortlessly add and store vital student information, including registration fees. Not only that, but it also provides the convenience of editing and deleting entries with ease.

With its sleek and user-friendly interface, this app is an ideal solution for academic institutions seeking a streamlined way to manage their student registration process. So why wait? Take advantage of this remarkable tool today and elevate your student registration experience to new heights!

## Contributors
- Saiful Islam Shovo
- Iris Du

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
  - (if this doesnt work then follow the next 2 steps otherwise skip those 2 steps)
- deactivate 
- sudo npm install -g @angular/cli  
- cd frond-end 
- ng serve  
- go to http://localhost:4200/
