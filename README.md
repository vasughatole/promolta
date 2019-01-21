# promolta
mail assignment for promolta

The code is in the assignment folder
To run the project cd to assignment and then run the following command

python manage.py runserver

Note: the default homepage is at localhost:8000
      
      Accepted username are test1, test2 ..... test10
      password for all username is normaluser
      Accepted emails are test1@test.com, test2@test.com, .... , test10@test.com
      Only these emails are mapped with a user and will be able to view,
      other email although stored but we cant view as there is no user with the corresponding email
      
      the admin page is at localhost:8000/admin
      admin username is vasu
      admin password is superuser
...............................................................................................

If there are dependency issues while running the project do the following
    Create a virtual environment and install dependencies
      cd assignment/
      virtualenv venv -p python3.6 
      source venv/bin/activate
      pip install -r requirements.txt
