from selene import browser, have, by, command


def test_practice_form():
    browser.open("/automation-practice-form")
    browser.element('.main-header').should(have.text("Practice Form"))
    browser.element('#fixedban').execute_script('element.remove()')
    browser.element('footer').execute_script('element.remove()')

    # browser.element('#fixedban').execute_script('element.scroll_into_view')
    # browser.element('#fixedban').perform(command.js.scroll_into_view)
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

    # browser.element("#subjectsContainer").type('Com')
    # browser.all("locator").element(by.text("Commerce")).click()

    browser.element("#hobbiesWrapper").element(by.text("Reading")).click()
    browser.element("#hobbiesWrapper").element(by.text("Music")).click()
    browser.element(by.css("input[type=file]")).send_keys(
        r"C:\Users\user\Downloads\Screenshot_1.png"
    )
    browser.element('#currentAddress').type('Almaty, street Testovaya 1, 44')
    browser.element("#state").click().element(by.text("Haryana")).click()
    browser.element("#city").click().element(by.text("Karnal")).click()
    browser.element("#submit").click()
