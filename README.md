# Teacher-record
A Django application to store teacher record

## Building

It is best to use the python `virtualenv` tool to build locally:

```bash
> git clone https://github.com/meistiyak/Teacher-record.git
> cd Teacher-record
> virtualenv env -p python3
> source env/bin/activate
```
Then install the requirements in your virtual environment

```bash
> pip install -r requirements.txt
```
And finally apply the migrations and run the server
```bash
> python manage.py migrate
> python manage.py runserver
```

Then visit `http://localhost:8000` to view the app


## Building with Docker
First run `docker-compose` to build the container:

```bash
docker-compose build
```

Then, the Docker container can be launched with the following command:

```bash
docker-compose up
```
The server should be responding at `http://localhost:8000`

## Admin Login
During migration a superuser is created. You may use this user for login.
```bash
username: admin
password: admin123
```

