from database import Base, engine
from models import Contact

print("Creating database...")

Base.metadata.create_all(engine)