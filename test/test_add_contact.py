from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username='admin', password="secret")
    app.contact.create(Contact(firstname=u"Шарап", middlename=u"Адильгереев", nickname="Adil", company="MRM",
                               address=u"Москва", phone_num="+7926", email="adilgereev05@ya.ru"))
    app.return_to_home_page()
    app.session.logout()
