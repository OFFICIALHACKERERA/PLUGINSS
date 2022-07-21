from sqlalchemy import Column, String

from . import BASE, SESSION


class Husbando(BASE):
    __tablename__ = "husbando"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Husbando.__table__.create(checkfirst=True)


def add_grp(chat_id: str):
    auto = Husbando(str(chat_id))
    SESSION.add(auto)
    SESSION.commit()


def rm_grp(chat_id: str):
    auto = SESSION.query(Husbando).get(str(chat_id))
    if auto:
        SESSION.delete(auto)
        SESSION.commit()


def get_all_grp():
    auto = SESSION.query(Husbando).all()
    SESSION.close()
    return auto


def is_husbando(chat_id: str):
    try:
        auto = SESSION.query(Husbando).get(str(chat_id))
        if auto:
            return str(auto.chat_id)
    finally:
        SESSION.close()
