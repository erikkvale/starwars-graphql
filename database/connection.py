from dotenv import dotenv_values
from sqlalchemy import create_engine, text

config = dotenv_values("database.env")
conn_str = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(**config)
engine = create_engine(conn_str, echo=True, future=True)


#  https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html
def create_table(table_name: str) -> bool:
    query = text("CREATE TABLE")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 'Hello, Erik'"))
        print(result.all())


if __name__ == "__main__":
    pass
