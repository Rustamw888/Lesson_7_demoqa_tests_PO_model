from selene.support.conditions import have
from selene.support.shared import browser


def hobby_select(hobby: str):
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(hobby)).click()
