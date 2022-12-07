# jTro Blog

## How to Run (Linux Environment)

### Step - 01

- Clone the repo: `https://github.com/jakiiii/jtroblog.git`
- Entry the project directory: `cd jtroblog`
- Create Virtual Environment: `python3 -m venv venv`
- Activate environment: `source venv/bin/activate`
- Install requirements: `pip install - requirements.txt`

### Step - 02
*Note: Here we use Postgres database.*

```
sudo -u postgres psql

CREATE DATABASE db_blog;
CREATE USER myprojectuser WITH PASSWORD 'password';

ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE db_blog TO myprojectuser;

\q
```

### Step - 03

- Create a new file .env. Open env-example.txt file and copy all and paste .env
or
`mv env-example.txt .env`
of
`cp env-example.txt .env`
- Configure postgres database in .env file.

```env
JTRO_DEV_DATABASE_NAME="db_blog"
JTRO_DEV_DATABASE_USER="myprojectuser"
JTRO_DEV_DATABASE_PASSWORD="password"
```

### Step - 04

- Migrate database: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
