from sqlalchemy import Column, String

from . import BASE, SESSION


class Collect(BASE):
    __tablename__ = "collect"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Collect.__table__.create(checkfirst=True)


def add_grp(chat_id: str):
    auto = Collect(str(chat_id))
    SESSION.add(auto)
    SESSION.commit()


def rm_grp(chat_id: str):
    auto = SESSION.query(Collect).get(str(chat_id))
    if auto:
        SESSION.delete(auto)
        SESSION.commit()


def get_all_grp():
    auto = SESSION.query(Collect).all()
    SESSION.close()
    return auto


def is_collect(chat_id: str):
    try:
        auto = SESSION.query(Collect).get(str(chat_id))
        if auto:
            return str(auto.chat_id)
    finally:
        SESSION.close()
