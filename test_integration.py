from backend_epithet_generator.app import app


def test_app_one_random():
    with app.test_client() as cli:
        result = cli.get('/')
        assert result.status_code == 200
        data = result.data.decode()
        assert isinstance(data, str)


def test_app_vocab():
    result = app.test_client().get('/vocabulary')
    assert result.status_code == 200
    assert result.data.decode()


def test_app_multi_random():
    result = app.test_client().get('/epithets/<int:quantity>')
    assert result.data.decode()


def test_app_random_num():
    result = app.test_client().get('/random')
    assert result.status_code == 200
    assert result.data.decode()
