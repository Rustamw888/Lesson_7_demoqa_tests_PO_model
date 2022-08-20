from selene.support.shared import browser

from lesson.model.pages.student_registration_page import StudentRegistrationForm, ModalDialogSubmittingForm

form = StudentRegistrationForm()
result = ModalDialogSubmittingForm()


def opened_practice_form():
    browser.open('/automation-practice-form')
