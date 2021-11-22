from model.group import Group


def test_mod_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="name modify"))
    app.session.logout()


def test_mod_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="header modify"))
    app.session.logout()
