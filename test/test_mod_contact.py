from model.contact import Contact


def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Для удаления"))
    app.contact.modify_first_contact(Contact(firstname=u"Шарап modify",
                                             middlename=u"Адильгереев modify",
                                             nickname="Adil modify",
                                             company="MRM modify",
                                             address=u"Москва modify",
                                             phone_num="+7926 modify",
                                             email="adilgereev05mod@ya.ru"))
