# SQL with Docker, PostgreSQL and SQLAlchemy

Eduardo, here is the clean modern path.

Recommendation

For portfolio and “Data X” jobs, use PostgreSQL + SQLAlchemy 2 + psycopg.
PostgreSQL is the mainstream open-source SQL database, Docker’s official Postgres image is a standard way to run it locally, SQLAlchemy 2 is the standard Python toolkit, and PostgreSQL access from Python is typically through a DBAPI driver such as psycopg.  ￼

What “talks to GitHub”

The database does not talk to GitHub.
Your project repo stores code, migrations, schemas, seed scripts, and maybe a docker-compose.yml. The actual database runs locally or on a server. You usually do not commit database files/data dumps except tiny demo seeds.  ￼

Best setup for learning and portfolio

Use Docker for the DB, and Python for queries.

1) Install Docker Desktop

On your Mac, install Docker Desktop, then confirm:

docker --version
docker compose version

2) Create a project

mkdir sql_playground
cd sql_playground
python3.12 -m venv .venv
source .venv/bin/activate
pip install sqlalchemy psycopg[binary]

SQLAlchemy provides the Python-side engine/toolkit, and PostgreSQL connectivity is via a DBAPI driver.  ￼

3) Start PostgreSQL with Docker

Create compose.yaml:

```yaml
services:
  db:
    image: postgres:latest
    container_name: sql_playground_db
    restart: unless-stopped
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: apppass
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Then run:

``docker compose up -d``

The official Postgres image supports POSTGRES_DB, POSTGRES_USER, and POSTGRES_PASSWORD; POSTGRES_PASSWORD is required.  ￼

4) Add Python code

Create app.py:

```python
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg://appuser:apppass@localhost:5432/appdb"
)

with engine.begin() as conn:
    conn.execute(text("""
        create table if not exists users (
            id serial primary key,
            name text not null,
            spend numeric not null
        )
    """))

    conn.execute(
        text("insert into users (name, spend) values (:name, :spend)"),
        [
            {"name": "Ana", "spend": 120.5},
            {"name": "Bruno", "spend": 88.0},
        ],
    )

with engine.connect() as conn:
    rows = conn.execute(
        text("select id, name, spend from users order by spend desc")
    )
    for row in rows:
        print(row)
```

Then:

``python app.py``

SQLAlchemy engines connect using URLs like postgresql+driver://..., and the first actual DBAPI connection is created when you call connect() or begin().  ￼

Should you write raw SQL or “SQL in Python”?

For GitHub, the minimal modern version is:
	•	SQLAlchemy Core
	•	mostly raw SQL via text()
	•	parameterized queries
	•	simple compose.yaml

That shows:
	•	you can run a real DB
	•	you know SQL
	•	you know Python DB access
	•	you know reproducible setup

You do not need a heavy ORM at first.

Good GitHub structure

```
sql_playground/
├── compose.yaml
├── app.py
├── requirements.txt
├── .env.example
├── sql/
│   ├── 001_schema.sql
│   └── 002_seed.sql
└── README.md
```

Very important

Do not hardcode real passwords in public repos.
Use environment variables or a .env file that is gitignored.

Example:

``export DATABASE_URL="postgresql+psycopg://appuser:apppass@localhost:5432/appdb"``

Then in Python:

```python
import os
from sqlalchemy import create_engine

engine = create_engine(os.environ["DATABASE_URL"])
```

If you want the absolute smallest possible demo

Use SQLite.
But for jobs, PostgreSQL looks better because it is a real server database and closer to what teams use in practice. SQLAlchemy supports multiple backends through dialects, including PostgreSQL and SQLite.  ￼

My blunt recommendation

Start with exactly this stack:
	•	DB: PostgreSQL in Docker
	•	Python package: sqlalchemy + psycopg[binary]
	•	Style: raw SQL with text()
	•	Repo content: code + schema + seed + compose + README
	•	Not in repo: actual database data directory

That is modern, minimal, clean, and GitHub-friendly.

I can also give you a ready-to-paste starter repo with compose.yaml, app.py, .env.example, and a tiny README.

--------------------

Eduardo — clean, minimal, correct order for macOS.
Goal: brew → micromamba → Python env → SQL tools.

⸻

4️⃣ Install core Python packages

Inside the environment:

pip install sqlalchemy psycopg[binary] pandas

Optional but useful:

pip install ipython python-dotenv


⸻

5️⃣ Install Docker (for PostgreSQL)

brew install --cask docker

Start Docker Desktop once.

Check:

docker --version
docker compose version


⸻

6️⃣ (Optional but recommended) SQL CLI tools

Install PostgreSQL client tools:

brew install libpq
brew link --force libpq

Check:

psql --version


⸻

7️⃣ Verify Python ↔ SQL

Test driver:

python - <<EOF
import sqlalchemy
import psycopg
print("SQL stack OK")
EOF


⸻

Minimal stack you now have

brew
micromamba
python 3.12 env
sqlalchemy
psycopg
docker
psql client

This is exactly what most data engineers / data scientists run locally.

⸻

If you want, I can also give you the 5-minute SQL refresher cheat sheet that covers 80% of interview SQL questions (joins, windows, group-by traps, ranking).

-----









I completely understand your frustration with Docker—you're right, `docker version` and `docker --version` are different commands, and Docker adds complexity you don't need right now. Let's set up a clean, local PostgreSQL environment directly on your Mac without containers.

## Complete Setup Guide for PostgreSQL + SQLAlchemy on Apple Silicon

### Step 1: Install PostgreSQL using Homebrew (No Docker!)

First, let's get PostgreSQL installed natively on your Mac:

```bash
# Install Homebrew if you don't have it yet
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install PostgreSQL (includes server, client, and command-line tools)
brew install postgresql@15

# Add PostgreSQL to your PATH (brew will show this command after installation)
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Start PostgreSQL as a background service
brew services start postgresql@15

# Verify it's working
psql --version
# Should output: psql (PostgreSQL) 15.x
```

The key here is `brew services start`—this runs PostgreSQL in the background, and it'll automatically restart when you reboot your Mac .

### Step 2: Create Your Database and User

Now let's set up a database for your "egg" project:

```bash
# Connect to PostgreSQL as your system user (no password needed initially)
psql postgres

# You're now in the PostgreSQL prompt (psql). Run these commands:
CREATE DATABASE eggdb;
CREATE USER egguser WITH PASSWORD 'eggpassword';
GRANT ALL PRIVILEGES ON DATABASE eggdb TO egguser;

# Exit psql
\q
```

Homebrew's PostgreSQL uses "peer authentication" by default, which means your Mac username automatically matches a PostgreSQL user. That's why you can connect without a password right now .

### Step 3: Activate Your Micromamba Environment and Install Python Packages

```bash
# Activate your egg environment
micromamba activate egg

# Install SQLAlchemy and PostgreSQL driver
pip install sqlalchemy
pip install psycopg2-binary  # Pure Python PostgreSQL adapter, no compilation needed

# Verify installations
python -c "import sqlalchemy; print(f'SQLAlchemy version: {sqlalchemy.__version__}')"
python -c "import psycopg2; print('psycopg2 installed successfully')"
```

The `psycopg2-binary` package is recommended for development—it's a pre-compiled version that avoids compilation issues on Apple Silicon .

### Step 4: Your "Hello World" with PostgreSQL and SQLAlchemy

Create a file called `hello_db.py`:

```python
"""
SQLAlchemy + PostgreSQL Hello World
Run with: python hello_db.py
"""

from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import Session, DeclarativeBase

# 1. Create the engine - this connects to PostgreSQL
# Format: postgresql://username:password@host:port/database
DATABASE_URL = "postgresql://egguser:eggpassword@localhost:5432/eggdb"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL queries

# Test the connection
with engine.connect() as conn:
    result = conn.execute(text("SELECT 'Hello from PostgreSQL!' as message"))
    print(result.fetchone()[0])

# 2. Define a table structure using SQLAlchemy ORM
class Base(DeclarativeBase):
    pass

class Greeting(Base):
    __tablename__ = 'greetings'
    
    id = Column(Integer, primary_key=True)
    message = Column(String(100))

# 3. Create the table in PostgreSQL
Base.metadata.create_all(engine)

# 4. Insert and query data using sessions
with Session(engine) as session:
    # Insert a greeting
    hello = Greeting(message="Hello, SQLAlchemy + PostgreSQL!")
    session.add(hello)
    session.commit()
    print(f"Inserted greeting with id: {hello.id}")
    
    # Query it back
    all_greetings = session.query(Greeting).all()
    for greet in all_greetings:
        print(f"Retrieved: {greet.message}")

print("✅ Hello World complete!")
```

Run it:

```bash
python hello_db.py
```

You'll see the SQL queries being printed (thanks to `echo=True`), followed by your hello messages .

### Step 5: Understanding What Just Happened

Here's the flow of what you just built:

1. **PostgreSQL** (installed via brew) is running as a background service on your Mac
2. **Database "eggdb"** and **user "egguser"** are ready for your project
3. **SQLAlchemy** connects to PostgreSQL using the connection string
4. The **ORM** lets you work with Python classes (`Greeting`) instead of writing SQL
5. **Session** manages the transaction—`add()` queues the change, `commit()` saves it

### Useful Commands for Daily Use

```bash
# Check if PostgreSQL is running
brew services list | grep postgresql

# Stop PostgreSQL
brew services stop postgresql@15

# Start it again
brew services start postgresql@15

# Connect directly to your database (for debugging)
psql -d eggdb -U egguser -h localhost

# List all databases in psql
\l

# Switch to your database in psql
\c eggdb

# Show tables in current database
\dt
```

### Why This Approach is Better Than Docker for Learning

- **No container complexity**—PostgreSQL runs as a native macOS process
- **Commands are exactly what the documentation shows**—no `docker exec` confusion
- **Files are on your Mac**—you can find the data at `/opt/homebrew/var/postgresql@15/`
- **Service management** is handled by `brew services`, which is reliable on macOS
- **Performance** is better without the container overhead

### Troubleshooting Tips

| Problem | Solution |
|---------|----------|
| `psql: error: could not connect to server` | Run `brew services restart postgresql@15`  |
| `FATAL: role "egguser" does not exist` | In psql: `CREATE USER egguser WITH PASSWORD 'eggpassword';`  |
| `psycopg2` installation fails | Use `pip install psycopg2-binary` instead  |
| Port 5432 already in use | Check with `lsof -i :5432`, stop conflicting service |

Once you're comfortable with this setup, you can explore SQLAlchemy's more advanced features like relationships between tables, but this gives you a solid foundation that actually works on your machine .

Want me to explain any part of this in more detail?








