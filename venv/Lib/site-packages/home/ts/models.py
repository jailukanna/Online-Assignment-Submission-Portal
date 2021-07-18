from datetime import datetime

from sqlalchemy import Column, Numeric, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


class ModelBase(object):
    created_at = Column(DateTime, nullable=False)

    def __init__(self):
        self.created_at = datetime.utcnow()


Base = declarative_base(cls=ModelBase)


class Series(Base):
    __tablename__ = 'series'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

    def __init__(self, name):
        self.created_at = datetime.utcnow()
        super().__init__()
        self.name = name

    def __repr__(self):
        return "Series(name=%r)" % (self.name)


class Device(Base):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True, unique=True)
    device_type = Column(Integer)
    device_sub_type = Column(Integer)
    device_id = Column(String(20), nullable=False, unique=True)

    def __init__(self, device_type, device_sub_type, device_id):
        self.created_at = datetime.utcnow()
        super().__init__()
        self.device_type = device_type
        self.device_sub_type = device_sub_type
        self.device_id = device_id

    def __repr__(self):
        return "Device(name=%s, ID=%r)" % (
            self.name, self.device_id)


class DataPoint(Base):
    __tablename__ = 'data_point'

    id = Column(Integer, primary_key=True)
    value = Column(Numeric, nullable=False)
    series_id = Column(Integer, ForeignKey('series.id'))
    device_id = Column(Integer, ForeignKey('device.id'))

    series = relationship("Series",
                          backref=backref('data_points', order_by=id))
    device = relationship("Device",
                          backref=backref('data_points', order_by=id))

    def __init__(self, series, device, value):
        self.created_at = datetime.utcnow()
        super().__init__()
        self.series = series
        self.device = device
        self.value = value

    def __repr__(self):
        return "<Data Point(%s, %s, value=%s, created_at=%s)>" % (
            self.series, self.device, self.value, self.created_at)
