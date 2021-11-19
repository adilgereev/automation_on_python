# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username='admin', password="secret")
    app.contact.create(Contact(firstname=u"Шарап", middlename=u"Адильгереев", nickname="Adil", company="MRM",
                               address=u"Москва", phone_num="+7926", email="adilgereev05@ya.ru"))
    app.return_to_home_page()
    app.session.logout()
