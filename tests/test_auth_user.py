from fastapi.testclient import TestClient

from routers.user import get_password_hash, pwd_context

endpoint = '/auth'
msg_nao_cadastrado = 'Usuário não cadastrado.'


def test_get_password_hash():
    psw = get_password_hash('fulano123')
    assert pwd_context.verify('fulano123', psw)


# def test_auth_by_username(client: TestClient):
#     response = client.post(endpoint, json={
#         "credential": "user_A",
#         "value": "senha1"

#     })

#     assert response.json() == {
#         "message": "Autenticação efetuada com sucesso.",
#         "error": None,
#         "data": []
#     }
#     assert response.cookies['Authorization'] == "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXJfQSIsIm5hbWUiOiJOb21lIEEiLCJqb2Jfcm9sZSI6IlRyYWJhbGhvIDEiLCJhY2Nlc3MiOiJhZG1pbiJ9.cCarXgAlBG7HtaDXXv_UEwcEKuuIehM43_JwZQf_YCE"  # noqa 501
#     assert response.status_code == 200
#     assert not response.json()["error"]


# def test_auth_by_email(client: TestClient):
#     response = client.post(endpoint, json={
#         "credential": "email3@email.com",
#         "value": "senha3"
#     })
#     assert response.status_code == 200
#     assert not response.json()["error"]
#     assert response.cookies['Authorization'] == "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXJfQyIsIm5hbWUiOiJOb21lIEEiLCJqb2Jfcm9sZSI6IlRyYWJhbGhvIDMiLCJhY2Nlc3MiOiJtYW5hZ2VyIn0.jPfb0274i-V7QM_ajfn2TPlrHPjtoX75aGn0NdSnpsM"  # noqa 501


def test_invalid_email(client: TestClient):
    response = client.post(endpoint, json={
        "credential": "naoexiste@email.com",
        "value": "senha3"
    })

    assert response.json()["error"]
    assert response.json()["message"] == msg_nao_cadastrado
    assert response.status_code == 401


def test_invalid_user(client: TestClient):
    response = client.post(endpoint, json={
        "credential": "naoexiste",
        "value": "senha50"
    })

    assert response.json()["error"]
    assert response.json()["message"] == msg_nao_cadastrado
    assert response.status_code == 401


def test_inactive_user(client: TestClient):
    response = client.post(endpoint, json={
        "credential": "user_H",
        "value": "senha8"
    })

    assert response.json() == {
        "message": msg_nao_cadastrado,
        "error": True,
        "data": []
    }
    assert response.status_code == 401
