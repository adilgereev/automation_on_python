from model.group import Group


def test_mod_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="name modify",
                                       header="header modify",
                                       footer="footer modify"))
    app.session.logout()
