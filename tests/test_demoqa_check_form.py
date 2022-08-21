from lesson.model import application_manager
from lesson.model.data.data import Student

student = Student(
    first_name='Rustam',
    last_name='Tyapaev',
    email='test@gmail.com',
    gender='Other',
    mobile_number='1234567890',
    date_of_birth='19 December,1988',
    birth_day='19',
    birth_month='11',
    birth_month_str='December',
    birth_year='1988',
    subjects=['Computer Science', 'English'],
    hobbies=['Sports', 'Reading', 'Music'],
    photo='picture.png',
    current_address='ulica Pushkina dom Kolotushkina',
    state='NCR',
    city='Delhi'
)


def test_submit_form():
    # GIVEN
    application_manager.opened_practice_form()

    # WHEN
    (application_manager.form
        .set_first_name(student.first_name)
        .set_last_name(student.last_name)
        .set_email(student.email)
        .set_gender(student.gender)
        .set_mobile_number(student.mobile_number)
        .set_birth_date(student.birth_year, student.birth_month, student.birth_day)
        .set_subjects(student.subjects)
        .subjects_should_have(student.subjects)
        .set_hobbies(student.hobbies)
        .set_photo(student.photo)
        .set_current_address(student.current_address)
        .set_state(student.state)
        .set_city(student.city)
        .submit()
    )

    # THEN
    application_manager.result.verify_sent_data(
        student.full_name(student.first_name, student.last_name),
        student.email,
        student.gender,
        student.mobile_number,
        student.date_of_birth,
        student.subjects,
        student.hobbies,
        student.photo,
        student.current_address,
        student.state_and_city(student.state, student.city)
    )
