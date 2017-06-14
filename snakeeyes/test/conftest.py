import pytest

from snakeeyes.app import create_app

@pytest.yield_fixture(scope='session')
def app():
    """
    Set up our flask test app, this only gets executed once

    :return: Flask app
    """
    params = {
        'DEBUG':False,
        'TESTING':True,
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()

