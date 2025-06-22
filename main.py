from lia.interface.gui import run
from lia.database import db, models

def init_db():
    models.Base.metadata.create_all(db.engine)

if __name__ == "__main__":
    init_db()
    run()
