from model.contact import Contact


def test_delete_first_contact(app):
    app.open_home_page()
    app.session.login(username='admin', password="secret")
    app.contact.delete_first_contact()
    app.return_to_home_page()
    app.session.logout()
