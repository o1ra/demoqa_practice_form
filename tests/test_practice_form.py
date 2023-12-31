import os

from selene import browser, have, by, command


def test_practice_form():
    browser.open("/automation-practice-form")
    browser.element('.main-header').should(have.text("Practice Form"))
    browser.element('#fixedban').execute_script('element.remove()')
    browser.element('footer').execute_script(
        'element.remove()'
    )  # browser.element('#fixedban').perform(command.js.scroll_into_view)

    browser.element("#firstName").type('Irina')
    browser.element("#lastName").type('Kirillova')
    browser.element("#userEmail").type('IrinaQA@gmail.com')
    browser.element('#gender-radio-2').double_click()
    browser.element("#userNumber").type('8909898900')
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element(
        by.text("March")
    ).click()
    browser.element(".react-datepicker__year-select").click().element(
        by.text("1993")
    ).click()
    # не выбирает нужную дату, если в элементе есть такая же дата в прошлом месяце
    # browser.element(".react-datepicker__month").element(by.text("28")).click()
    browser.element(
        ".react-datepicker__day--028:not(.react-datepicker__day--outside-month)"
    ).click()
    browser.element('#currentAddress').perform(command.js.scroll_into_view)
    browser.element("#subjectsInput").type('Com')
    browser.element(".subjects-auto-complete__menu").element(
        by.text("Commerce")
    ).click()
    browser.element("#hobbiesWrapper").element(by.text("Reading")).click()
    browser.element("#hobbiesWrapper").element(by.text("Music")).click()
    browser.element(by.css("input[type=file]")).send_keys(
        os.path.abspath('resourses/img/Screenshot_1.png')
    )
    browser.element('#currentAddress').type('Almaty, street Testovaya 1, 44')
    browser.element("#state").click().element(by.text("Haryana")).click()
    browser.element("#city").click().element(by.text("Karnal")).click()
    browser.element("#submit").click()

    browser.element("#example-modal-sizes-title-lg").should(
        have.text("Thanks for submitting the form")
    )

    browser.element('.table-responsive').all('td:nth-of-type(2)').should(
        have.texts(
            'Irina Kirillova',
            'IrinaQA@gmail.com',
            'Female',
            '8909898900',
            '28 March,1993',
            'Commerce',
            'Reading, Music',
            'Screenshot_1.png',
            'Almaty, street Testovaya 1, 44',
            'Haryana Karnal',
        )
    )

    browser.element("#closeLargeModal").click()
