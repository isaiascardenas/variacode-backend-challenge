from flask import Flask, g
from sqlalchemy.orm.session import sessionmaker


class DatabaseMiddleware:
    def __init__(self, session_maker: sessionmaker):
        self.session_maker = session_maker

    def open(self):
        session = self.session_maker()
        g.session = session

    def close(self, *_args, **_kwargs):
        db_session = g.pop("session", None)

        if db_session is not None:
            db_session.close()

    def register(self, app: Flask):
        app.before_request(self.open)
        app.teardown_appcontext(self.close)
