from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, Series, Device, DataPoint


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        return instance

engine = create_engine('postgresql://home:home@localhost:5432/home')
Session = sessionmaker(bind=engine)


def syncdb():

    Base.metadata.create_all(engine)


def get_series(session, name):
    series = get_or_create(session, Series, name=name)
    session.commit()
    return series


def get_device(session, device_type, device_sub_type, device_id):
    device = get_or_create(session, Device, device_type=device_type,
                           device_sub_type=device_sub_type,
                           device_id=device_id)
    session.commit()
    return device


def record(session, series, device, value):
    data_point = DataPoint(series=series, device=device, value=value)
    session.add(data_point)
    session.commit()
    return data_point
