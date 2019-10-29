import os
import tempfile

import pytest

from feature_server import db, create_app
from feature_server import config


def upgrade_db():
    import alembic
    from alembic.config import Config
    from alembic.script import ScriptDirectory

    alembic_config = Config(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'alembic.ini',
        )
    )
    script_dir = ScriptDirectory.from_config(alembic_config)
    heads = [s.revision for s in script_dir.get_revisions("head")]
    assert len(heads) == 1
    alembic.command.upgrade(alembic_config, heads[0])


@pytest.fixture(scope='module')
def client():
    # Create test DB
    db_fd, db_fname = tempfile.mkstemp('.db')
    config.SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_fname}"
    config.TESTING = True

    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            upgrade_db()
        yield client

    os.close(db_fd)
    os.unlink(db_fname)
