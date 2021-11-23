from model.group import Group


def test_mod_group_name(app):
    app.group.modify_first_group(Group(name="name modify"))


def test_mod_group_header(app):
    app.group.modify_first_group(Group(header="header modify"))
