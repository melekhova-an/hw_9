from demoqa_tests import resources


from selene import have
from selene.support.shared import browser


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')


    def fill_date(self, student):
        browser.element('#firstName').set(student.first_name)
        browser.element('#lastName').set(student.last_name)
        browser.element('#userEmail').set(student.email)
        browser.all('[name=gender]').element_by(have.value(student.gender)).element('..').click()
        browser.element('#userNumber').set(student.mobile)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(student.date_of_birth.year)
        browser.element('.react-datepicker__month-select').send_keys(student.date_of_birth.strftime('%B'))
        browser.element(f'.react-datepicker__day--0{student.date_of_birth.day}').click()
        browser.element('#subjectsInput').type(student.subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(student.hobby)).click()
        browser.element('#uploadPicture').send_keys(resources.path(student.picture))
        browser.element('#currentAddress').type(student.address)
        browser.element('#react-select-3-input').type(student.state).press_enter()
        browser.element('#react-select-4-input').type(student.city).press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_registered_user_with(self, student):
        full_name = f'{student.first_name} {student.last_name}',
        date_of_birth = f'{student.date_of_birth.day} {student.date_of_birth.strftime("%B")},{student.date_of_birth.year}'
        city = f'{student.state} {student.city}'

        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                student.email,
                student.gender,
                str(student.mobile),
                date_of_birth,
                student.subject,
                student.hobby,
                student.picture,
                student.address,
                city
            ))



