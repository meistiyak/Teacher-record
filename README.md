# Teacher-record
A Django application to store teacher record

## Building

It is best to use the python `virtualenv` tool to build locally:

```bash
> virtualenv env
> source env/bin/activate
> git clone https://github.com/meistiyak/Teacher-record.git .
```
Then you navigate to the base directory of the project and install the requirements in your virtual environment

```bash
> cd Teacher-record
> pip install -r requirements.txt
```
And finally you make migrations to the database, and run the server
```bash
> python manage.py makemigrations
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

The server should be responding at 127.0.0.1:8000
