from sqlalchemy import func
from home.ts.models import Series, DataPoint
from home.ts import Session


def report():

    print()

    session = Session()

    series = session.query(Series)

    count, start, latest = session.query(
        func.count(DataPoint.value),
        func.min(DataPoint.created_at),
        func.max(DataPoint.created_at)
    ).one()

    print("Overall stats:")
    print("    Data Points :", count)
    print("    Data From   :", start)
    print("    Last Read   :", latest)
    print()

    for s in series:

        max_v, min_v, count, start, latest = session.query(
            func.max(DataPoint.value),
            func.min(DataPoint.value),
            func.count(DataPoint.value),
            func.min(DataPoint.created_at),
            func.max(DataPoint.created_at)
        ).filter_by(series=s).one()

        print("Metric:", s.name)
        print("    Data Points :", count)
        print("    Data From   :", start)
        print("    Last Read   :", latest)
        print("    Minimum     :", min_v)
        print("    Maximum     :", max_v)
        print()


def run():

    report()
