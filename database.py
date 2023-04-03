import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative 
import sqlalchemy.orm as orm # object-relational mapping - convert data between a relational database and the heap of an object-oriented programming language   

DATABASE_URL = "postgresql://myuser:password@localhost/fast_api_database"

enigne = sql.create_engine(DATABASE_URL)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=enigne)

Base = declarative.declarative_base() # base class from which to inherit