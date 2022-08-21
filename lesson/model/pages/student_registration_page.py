from selene import command, have
from selene.support.shared import browser

from lesson.model.controls.checkboxes import hobby_select
from selene.support.shared.jquery_style import s
from lesson.model.controls.dropdown import Dropdown
from lesson.model.controls.modal_content import Table
from lesson.model.controls.tags_input import TagsInput
from lesson.model.utils import resources


class StudentRegistrationForm:
    def set_first_name(self, value: str):
        browser.element('#firstName').type(value)
        return self

    def set_last_name(self, value: str):
        browser.element('#lastName').type(value)
        return self

    def set_email(self, value: str):
        browser.element('#userEmail').type(value)
        return self

    def set_gender(self, value):
        s('#genterWrapper').all('.custom-radio').element_by(have.exact_text(value)).click()
        return self

    def set_mobile_number(self, value: str):
        browser.element('#userNumber').type(value)
        return self

    def set_birth_date(self, year: str, month: str, day: str):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__year-select').s(f'[value="{year}"]').click()
        s('.react-datepicker__month-select').s(f'[value="{month}"]').click()
        s(f'.react-datepicker__day--0{day}').click()
        return self

    def set_subjects(self, values: list):
        for value in values:
            TagsInput(browser.element('#subjectsInput')).add(value)
        return self

    def subjects_should_have(self, values: list):
        TagsInput(browser.element('#subjectsContainer')).element.all('#css-12jo7m5').should(have.text(' '.join(values)))
        return self

    def set_hobbies(self, values: list):
        for value in values:
            hobby_select(value)
        return self

    def set_photo(self, file: str):
        s('#uploadPicture').send_keys(resources(file))
        return self

    def set_current_address(self, value: str):
        browser.element('#currentAddress').type(value)
        return self

    def set_state(self, value: str):
        Dropdown(browser.element('#state')).select(value)
        return self

    def set_city(self, value: str):
        Dropdown(browser.element('#city')).autocomplete(value)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)


class ModalDialogSubmittingForm:
    def __init__(self):
        self.element = browser.element('.modal-content')
        self.table = Table(self.element.element('.table'))

    def verify_sent_data(self, *values):
        for i in range(len(values)):
            if isinstance(values[i], list):
                value = ', '.join(values[i])
            else:
                value = values[i]
            self.table.path_to_cell(i + 1, column=2).should(have.exact_text(value))
