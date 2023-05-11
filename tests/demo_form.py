from demoqa_tests.data.users import User, Gender, Hobby, Subject
from datetime import date
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_complete_the_form():
    student = User(
        first_name='An',
        last_name='Melekhova',
        email='test@gmail.com',
        gender=Gender.female.value,
        mobile='8900050050',
        date_of_birth=date(1997, 4, 11),
        subject=Subject.arts.value,
        hobby=Hobby.reading.value,
        picture='IMAGE.jpg',
        address='Moscow, b1',
        state='Uttar Pradesh',
        city='Agra'
    )

    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_date(student)

    registration_page.submit()

    registration_page.should_registered_user_with(student)
