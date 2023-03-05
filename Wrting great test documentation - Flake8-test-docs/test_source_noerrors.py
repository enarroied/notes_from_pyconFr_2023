import requests


# This function does not raise errors with flake8
# extended with test-docs, all sections are here
# arrange, act and assert
def test_create_user(db):
    """
    arrange: given a running API instance
        connected to an in-memory database with
        the user table created and the name,
        email and password for the user
    act: when the user name, email and password
        is sent to the /user endpoint as a POST
    assert: then a 2XX reponse is returned and
        the user data is added to the user table.
    """

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
