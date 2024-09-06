import datetime
from sqlalchemy.orm import Session
from database.models import *

engine = create_engine("sqlite:///taskdata.db", echo=True)
BaseClass.metadata.create_all(engine)
with Session(engine) as session:
    print("\n\n\n\n\n\nSTART SESSION\n\n\n\n\n\n")