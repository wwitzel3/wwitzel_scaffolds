from ming import Session
from ming.datastore import DataStore
from ming.orm import ThreadLocalORMSession
from ming.orm import Mapper

mainsession = Session()
DBSession = ThreadLocalORMSession(mainsession)

def init_mongo(engine):
    datastore = DataStore(*engine)
    mainsession.bind = datastore
    Mapper.compile_all()

    for mapper in Mapper.all_mappers():
        mainsession.ensure_indexes(mapper.collection)

# Database includes here allow for a simple programming API convention. By importing all the models here
# we can use the import models as M convention throughout the rest of the code.
from .sample import Sample

# Explicit is better.
__all__ = ['DBSession', 'init_mongo', 'Sample']
