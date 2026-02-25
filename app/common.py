from flask import Flask
from .common import init_db_and_redis, ensure_indexes_db


def create_app():
    app = Flask(__name__)

    # Initialize DB and Redis
    mc, mdb, r, hold_sha = init_db_and_redis(app)
    ensure_indexes_db(mdb)

    # Attach to app for later use if you like
    app.mongo_client = mc
    app.mongo_db = mdb
    app.redis = r
    app.hold_sha = hold_sha

    @app.route("/")
    def health():
        return {"status": "ok"}

    return app


# This is what Gunicorn will look for: "app:app"
app = create_app()