# Steps to run this project

__Step 1:__
First create and activate the virtual environment of python 3.7 and install the packages using the command:
```bash
pip install -r requirements.txt
```
# Super Admin Credentials :- email : om@gmail.com, password : 2311

# API Documentation

__Q2. User Sign Up__
__User SignUp(Assuming that the server is running on localhost:8000)__


link : http://localhost:8000/users/sign-up/

request-method : POST 

Sample Form-data :

{

    __*REQUIRED_VALUES*__
    'email'         : 'xxx@gmail.com',
    
    'password'      : 'xxxx',
    
    'first_name'    : 'xxxx',
    
    'last_name'     : 'xxxx',
    
    'mobileNo'      : '1234567890'(Only 10 digits),
    
    'address'       : 'xxxxx',
    
    __*OPTIONAL_VALUES*__
    
    'is_staff'     : 'True/False',
    
    'is_superuser' : 'True/False',
    
    'is_admin'     : 'True/False',
    
}


__User Signin with REST_FRAMEWORK__

This project uses the DJANGO_REST_KNOX authentication.
*I have used django_rest_knox which is a secure method. This method doesn't store the tokens directly in the database, it stores the encoded tokens which prevents the access of the database with the tokens when database is stolen...*

link: http://localhost:8000/users/login/

request-method : POST

Sample Form-data :
{

    'email'    : 'xxxx@gmail.com',
    
    'password' : 'xxxx'
    
}


__User Signout__

link: http://localhost:8000/users/logout/

request-method : POST

Headers should contain :

{

    Authorization : Token *GENERRATED_TOKEN*
}
