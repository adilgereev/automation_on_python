from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname=u"Шарап", middlename=u"Адильгереев", nickname="Adil", company="MRM",
                               address=u"Москва", phone_num="+7926", email="adilgereev05@ya.ru"))
