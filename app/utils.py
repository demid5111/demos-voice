def write_record(record, session):
    session.add(record)
    session.commit()
