from selene import have, by, command
from selene.support.shared import browser

import resources


class RegistrationPage:
    def __int__(self):
        pass

    def open(self):
        browser.open("/automation-practice-form")
        browser.element('.main-header').should(have.text("Practice Form"))
        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('footer').execute_script('element.remove()')
        return self

    def fill_full_name(self, user: User):
        browser.element("#firstName").type(user.full_name.first_name)
        browser.element("#lastName").type(user.full_name.last_name)
        return self

    def fill_email(self, user: User):
        browser.element("#userEmail").type(user.email)
        return self

    def gender(self, user: User):
        if user.gender== "Female":
            browser.element('#gender-radio-2').double_click()
        elif user.gender == "Male":
            browser.element('#gender-radio-1').double_click()
        elif user.gender == "Other":
            browser.element('#gender-radio-3').double_click()
        return self

    def fill_number(self, user: User):
        browser.element("#userNumber").type(user.number)
        return self

    def fill_date_of_birth(self, user: User):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click().element(
            by.text(user.date_of_birth.month)
        ).click()
        browser.element(".react-datepicker__year-select").click().element(
            by.text(user.date_of_birth.year)
        ).click()
        # не выбирает нужную дату, если в элементе есть такая же дата в прошлом месяце
        # browser.element(".react-datepicker__month").element(by.text("28")).click()
        browser.element(
            f'.react-datepicker__day--0{user.date_of_birth.day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subject(self, user: User):
        browser.element('#currentAddress').perform(command.js.scroll_into_view)
        browser.element("#subjectsInput").type(user.subject)
        browser.element(".subjects-auto-complete__menu").element(by.text(user.subject)
                                                                 ).click()
        return self

    def fill_hobbies(self, user: User):
        browser.element("#hobbiesWrapper").element(by.text(user.hobbies)).click()
        return self

    def fill_image(self, user: User):
        browser.element(by.css("input[type=file]")).send_keys(resources.path(user.image))
        return self

    def fill_address(self, user: User):
        browser.element('#currentAddress').type(user.address)
        return self

    def fill_state_and_city(self, user: User):
        browser.element("#state").click().element(by.text(user.state)).click()
        browser.element("#city").click().element(by.text(user.city)).click()
        return self

    def click_button(self):
        browser.element("#submit").click()
        return self

    def open_form(self):
        browser.element("#example-modal-sizes-title-lg").should(
            have.text("Thanks for submitting the form")
        )
        return self

    def should_have_registrated_user_with(self, full_name, email, gender, number, date_of_birth,
                                          subjects, hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )
        return self

    def close_modal(self):
        browser.element("#closeLargeModal").click()
        return self
