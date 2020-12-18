#UEL Library Management System software developed by 5A-UEL Programmers
----------------------------------------------------------------
Built in python django 3.1.3 framework.
This software is built for final project submission

** Note: This software is built with use of theme of different liscence. Please read it before use  ** 

#LMS setup requirements
-----------------------------------------------------------
**For image field**

-- `pip install pillow`

**For uploaded Image thumbnail**

-- `pip install django-imagekit`

**For connection of mysql to python**

-- `pip install mysqlclient`

------------------------------------------------------------------------------------------------------------------------

Note: If Namecheap or any other hosting does not allow user to install mysqlclient for connecting mysql to python
Install PyMySQL using following method (https://www.dev2qa.com/how-to-connect-mysql-database-in-django-project/)
OR follow below code

-------------------------------------------------------------------------------------------------------------------------
**For connecting mysql use of pymysql**
1. pip install pymysql

2. **edit lms/setting.py**

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'NAME': 'XXXXXX',
                'USER': 'XXXXXX',
                'PASSWORD': 'XXXXXX',
                # connect options
                'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",},
            }
        }
    
**3. edit lms/__init__.py**

       import pymysql
        
        """for bypassing pymysql required version"""
        pymysql.version_info = (1, 4, 0, "final", 0)
        
        """install pymysql as mysql database driver."""
        pymysql.install_as_MySQLdb()
        
----------------------------------------------------------------------------------------------------------------------
End: of installing PyMySQL

----------------------------------------------------------------------------------------------------------------------

**For Theme**

-- `pip install git+https://github.com/app-generator/django-admin-black.git`

**For filter design from list to select**

-- `pip install django-admin-list-filter-dropdown`

** For book search via datatables

-- `pip install django-datatables-view`

-----------------------------------------------------------------------------------------------------------------------

**For uploading files some part of django code are changed as per below link**

-------------
    This method is used because namecheap cpanel shared hosting is not allowing me to upload files in the system as per
    django admin form method.
-------------
https://medium.com/@mnydigital/how-to-resolve-django-admin-404-post-error-966ce0dcd39d

-----------------------------------------------------------------------
**For test cases** 

    python manage.py test apps.userDetail.tests For user detail and issue book app
    python manage.py test apps.Book.tests //For book app
    OR
    python manage.py test // For both apps at a time
    
        