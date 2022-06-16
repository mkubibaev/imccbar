# International Medical Cooperation Center for the Belt and Road

# Building

**Requires:**
* [Python 3+](https://www.python.org)
* [Django 4.0](https://www.djangoproject.com/)
* [MySQL 5.7](https://www.mysql.com/)

**Installation**
* Install dependencies (in local virtual env) 
    ```shell script
        pip install -r requirements.txt
    ```
  
* Migrate DB
    ```shell script
        python manage.py migrate
    ```
  
* Load initial data (fixtures)
    ```shell script
        python manage.py loaddata fixtures.json
    ```  

* Run server
    ```shell script
        python manage.py runserver
    ```
 
**i18n**
* Collect messages
    ```shell script
        python manage.py makemessages -l zh_CN
        python manage.py makemessages -l ru
        python manage.py makemessages -l en
    ```
* Compile messages
    ```shell script
        python manage.py compilemessages
    ```

**SASS**
* Compile scss to css
    ```shell script
        python manage.py sass --watch webapp/static/scss/ webapp/static/css/
    ```