from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.models import *

engine = create_engine("sqlite:///taskdata.db", echo=True)
BaseClass.metadata.create_all(engine)
with Session(engine) as session:
    print("Started session")