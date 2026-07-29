# Makefile for PostgreSQL setup
.PHONY: init-db reset-db psql

# Initialize database (safe to run multiple times)
init-db:
	@echo "Initializing database..."
	psql postgres -f init-db.sql

# Reset database (drop and recreate)
reset-db:
	@echo "Resetting database..."
	psql postgres -c "DROP DATABASE IF EXISTS eggdb;"
	psql postgres -c "DROP USER IF EXISTS egguser;"
	$(MAKE) init-db

# Connect to database
psql:
	psql -d eggdb -U egguser -h localhost

# Run Python script
run:
	python app.py