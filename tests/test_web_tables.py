import pytest
from selene import have
from selene.support.by import text

from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


@pytest.fixture(scope='session')
def fixture_part3():
    browser.open('https://demoqa.com/webtables') \
        .driver \
        .set_window_size(1920, 1080)
    yield
    browser.close()
    browser.quit()
    print("Домашняя работа - завершена!")


def test_web_tables_form():
    # открываем страницу с таблицей
    browser.open('https://demoqa.com/webtables').driver.set_window_size(1920, 1080)

    # удаляем вторую строку
    s("#delete-record-2").click()

    # считываем значение поля ДО редактирования
    old_value = s("//div[@role='row'][.//*[@id='edit-record-3']]/*").text

    # редактируем имя
    s("#edit-record-3").click()
    s("#firstName").clear().type("newName")
    s("#submit").click()

    # считываем значение поля ПОСЛЕ редактирования
    new_value = s("//div[@role='row'][.//*[@id='edit-record-3']]/*").text

    # проверяем что значение изменилось на валидное
    assert old_value != new_value
    s("//div[@role='row'][.//*[@id='edit-record-3']]/*").should(have.text("newName"))

    # добавление нового пользователя с заполнением данных в форме
    s("#addNewRecordButton").click()
    s("#firstName").type("newFirstName")
    s("#lastName").type("newLastName")
    s("#userEmail").type("name@example.com")
    s("#age").type("33")
    s("#salary").type("350000")
    s("#department").type("newDepartment")
    s("#submit").click()

    # проверяем, что пользователь появился
    ss("//div[@role='row'][.//*[@id='edit-record-3']]/*").find_by(text("newFirstName"))
