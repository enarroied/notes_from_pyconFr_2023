import requests


def test_create_user(db):
    user = {
        "name": "David",
        "email": "david.jkandersson.com",
        "password": "secure",
    }

    requests.post("localhost/user", data=user)

    users = db.user.select()
    assert len(users) == 1
    assert users[0].name == user["name"]
    assert users[0].password == hash(user["password"])
