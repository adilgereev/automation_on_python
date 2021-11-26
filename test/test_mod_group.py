from model.group import Group


def test_mod_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Для модификации"))
    app.group.modify_first_group(Group(name="name modify"))


def test_mod_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Для модификации"))
    app.group.modify_first_group(Group(header="header modify"))
