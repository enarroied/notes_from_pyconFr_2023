import requests


# This function does not contain the arrange section
# required for good test documentation, flake8
# extended with test-docs will raise an error
def test_create_user(db):
    """
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
