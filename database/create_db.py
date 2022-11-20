from database.database import Base, engine
from models.models import Contact

print("Creating database...")

Base.metadata.create_all(engine)