from main import app


def test_main():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Doe normaal!'

    response = app.test_client().get('/cow')
    assert response.status_code == 200
    assert response.data == b'Boodschaaap!'
