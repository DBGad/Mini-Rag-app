## Run Alembic Migrations

#### Install dependencies for Alembic 

```bash
sudo apt update 
sudo apt install libpq-dev gcc python3-dev
```

### start Data migrations with alembic

- goes to the dir of ur database folder and behind schemes dir do this 
```bash 
$ alembic init alembic
```


### Configuration

```bash
cp alembic.ini.example alembic.ini
```

- Update the `alembic.ini` with your database credentials (`sqlalchemy.url`)
  
### (Optional) Create a new migration

```bash
alembic revision --autogenerate -m "Add ..."
```

### Upgrade the database

```bash
alembic upgrade head
```