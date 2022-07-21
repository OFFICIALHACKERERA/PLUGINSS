from sqlalchemy import Column, String, UnicodeText

from . import BASE, SESSION


class SEchos(BASE):
    __tablename__ = "sechos"
    chat_id = Column(String(14), primary_key=True)
    user_id = Column(String(14), primary_key=True, nullable=False)
    chat_name = Column(UnicodeText)
    user_name = Column(UnicodeText)
    user_username = Column(UnicodeText)
    chat_type = Column(UnicodeText)

    def __init__(
        self, chat_id, user_id, chat_name, user_name, user_username, chat_type
    ):
        self.chat_id = str(chat_id)
        self.user_id = str(user_id)
        self.chat_name = chat_name
        self.user_name = user_name
        self.user_username = user_username
        self.chat_type = chat_type

    def __eq__(self, other):
        return bool(
            isinstance(other, SEchos)
            and self.chat_id == other.chat_id
            and self.user_id == other.user_id
        )


SEchos.__table__.create(checkfirst=True)


def sis_echo(chat_id, user_id):
    try:
        return SESSION.query(SEchos).get((str(chat_id), str(user_id)))
    except BaseException:
        return None
    finally:
        SESSION.close()


def sget_echos(chat_id):
    try:
        return SESSION.query(SEchos).filter(SEchos.chat_id == str(chat_id)).all()
    finally:
        SESSION.close()


def sget_all_echos():
    try:
        return SESSION.query(SEchos).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def saddecho(chat_id, user_id, chat_name, user_name, user_username, chat_type):
    to_check = sis_echo(chat_id, user_id)
    if not to_check:
        sadder = SEchos(
            str(chat_id), str(user_id), chat_name, user_name, user_username, chat_type
        )
        SESSION.add(sadder)
        SESSION.commit()
        return True
    rem = SESSION.query(SEchos).get((str(chat_id), str(user_id)))
    SESSION.delete(rem)
    SESSION.commit()
    sadder = SEchos(
        str(chat_id), str(user_id), chat_name, user_name, user_username, chat_type
    )
    SESSION.add(sadder)
    SESSION.commit()
    return False


def sremove_echo(chat_id, user_id):
    to_check = sis_echo(chat_id, user_id)
    if not to_check:
        return False
    srem = SESSION.query(SEchos).get((str(chat_id), str(user_id)))
    SESSION.delete(srem)
    SESSION.commit()
    return True


def sremove_echos(chat_id):
    if saved_filter := SESSION.query(SEchos).filter(SEchos.chat_id == str(chat_id)):
        saved_filter.delete()
        SESSION.commit()


def sremove_all_echos():
    if saved_filter := SESSION.query(SEchos):
        saved_filter.delete()
        SESSION.commit()
