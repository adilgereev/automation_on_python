from model.contact import Contact


def test_mod_contact(app):
    app.open_home_page()
    app.session.login(username='admin', password="secret")
    app.contact.modify_first_contact(Contact(firstname=u"Шарап modify",
                                             middlename=u"Адильгереев modify",
                                             nickname="Adil modify",
                                             company="MRM modify",
                                             address=u"Москва modify",
                                             phone_num="+7926 modify",
                                             email="adilgereev05mod@ya.ru"))
    app.return_to_home_page()
    app.session.logout()
