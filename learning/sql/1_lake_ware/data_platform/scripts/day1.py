"""
SQLAlchemy + PostgreSQL Hello World
Run with: python hello_db.py
"""

from pathlib import Path

import duckdb

con = duckdb.connect()

root: Path = Path("/Users/egg/projects/eduardogade/challenges/sql/1_lake_ware/data_platform/lake/raw/renomica_dac")
table = root / "renomica.parquet"

table = "../"

con.execute("""
SELECT *
FROM {table}
LIMIT 5;
""")

# con.execute("""
# SELECT country, count(*)
# FROM 'lake/raw/events/**/*.parquet'
# GROUP BY country
# """)