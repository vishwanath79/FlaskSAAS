import pytest
import nose



from snakeeyes.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    Set up our flask tests app, this only gets executed once at begining of tests suite

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

@pytest.yield_fixture(scope='function')
def client(app):
    """ setup an app client, this gets executed for each tests function
    :param app: Pytest fisture
    :return: Flask app client
    """
    yield app.test_client()

