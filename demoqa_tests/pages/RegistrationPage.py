from selene import have, by, command
from selene.support.shared import browser

import resources
from demoqa_tests.users.user import User


class RegistrationPage:
    def __int__(self):
        pass

    def open(self):
        browser.open("/automation-practice-form")
        browser.element('.main-header').should(have.text("Practice Form"))
        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('footer').execute_script('element.remove()')
        return self

    def register_user(self, user: User):
        browser.element("#firstName").type(user.full_name["first_name"])
        browser.element("#lastName").type(user.full_name["last_name"])
        browser.element("#userEmail").type(user.email)
        if user.gender == "Female":
            browser.element('#gender-radio-2').double_click()
        elif user.gender == "Male":
            browser.element('#gender-radio-1').double_click()
        elif user.gender == "Other":
            browser.element('#gender-radio-3').double_click()
        browser.element("#userNumber").type(user.number)
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').send_keys(
            user.date_of_birth.strftime('%B')
        ).click()
        browser.element('.react-datepicker__year-select').click().send_keys(
            user.date_of_birth.strftime('%Y')
        ).click()
        browser.element(
            f'.react-datepicker__day--0{user.date_of_birth.strftime("%d")}'
        ).click()
        browser.element('#currentAddress').perform(command.js.scroll_into_view)
        browser.element("#subjectsInput").type(user.subject)
        browser.element(".subjects-auto-complete__menu").element(
            by.text(user.subject)
        ).click()
        browser.element("#hobbiesWrapper").element(by.text(user.hobbies[0])).click()
        browser.element(by.css("input[type=file]")).send_keys(
            resources.path(user.image)
        )
        browser.element('#currentAddress').type(user.address)
        browser.element("#state").click().element(by.text(user.state)).click()
        browser.element("#city").click().element(by.text(user.city)).click()
        browser.element("#submit").click()
        return self

    def modal_form(self, user: User):
        browser.element("#example-modal-sizes-title-lg").should(
            have.text("Thanks for submitting the form")
        )
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.full_name["first_name"]} {user.full_name["last_name"]}',
                f'{user.email}',
                f'{user.gender}',
                f'{user.number}',
                '{0} {1},{2}'.format(
                    user.date_of_birth.strftime("%d"),
                    user.date_of_birth.strftime("%B"),
                    user.date_of_birth.strftime("%Y"),
                ),
                f'{user.subject}',
                f'{user.hobbies[0]}',
                f'{user.image}',
                f'{user.address}',
                f'{user.state} {user.city}',
            )
        )
        browser.element("#closeLargeModal").click()
        return self
