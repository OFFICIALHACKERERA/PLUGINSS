"""
credits to @LEGEND_K_BOY
"""
#    Copyright (C) 2020  sandeep.n(π.$)
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
from sqlalchemy import Column, String, UnicodeText

from . import BASE, SESSION


class Gban_Sql(BASE):
    __tablename__ = "gban_sql"
    user_id = Column(String(14), primary_key=True)
    first_name = Column(UnicodeText)
    date = Column(UnicodeText)
    username = Column(UnicodeText)
    reason = Column(UnicodeText)

    def __init__(self, user_id, first_name, date, username, reason):
        self.user_id = str(user_id)
        self.first_name = first_name
        self.date = date
        self.username = username
        self.reason = reason


Gban_Sql.__table__.create(checkfirst=True)


def gban(user_id, first_name, date, username, reason):
    to_check = is_gbanned(user_id)
    if not to_check:
        user = Gban_Sql(str(user_id), first_name, date, username, reason)
        SESSION.add(user)
        SESSION.commit()
        return True
    rem = SESSION.query(Gban_Sql).get(str(user_id))
    SESSION.delete(rem)
    SESSION.commit()
    user = Gban_Sql(str(user_id), first_name, date, username, reason)
    SESSION.add(user)
    SESSION.commit()
    return True


def gbanned(user_id):
    to_check = is_gbanned(user_id)
    if not to_check:
        return False
    rem = SESSION.query(Gban_Sql).get(str(user_id))
    SESSION.delete(rem)
    SESSION.commit()
    return True


def is_gbanned(user_id):
    try:
        _result = SESSION.query(Gban_Sql).get(str(user_id))
        if _result:
            return _result
        return None
    finally:
        SESSION.close()


def get_all_gbanned():
    try:
        return SESSION.query(Gban_Sql).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def ungban_all():
    try:
        SESSION.query(PmPermit_Sql).delete()
        SESSION.commit()
        return True
    except BaseException:
        return False
    finally:
        SESSION.close()
