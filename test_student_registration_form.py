from selene import browser, be, have


def test_fill_form(set_browser):
    browser.element('#firstName').type('Katya')
    browser.element('#lastName').type('Bal')
    browser.element('#userEmail').type('katyabal@mail.ru')
    browser.element('#userNumber').type('1234567891')
    browser.element('#currentAddress').type('Batumi')

    browser.element('#subjectsInput').type('c')
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Chemistry')).click()

    browser.driver.execute_script("document.getElementById('gender-radio-2').click()")

    browser.element('label[for="hobbies-checkbox-3"]').should(be.visible).click()

    browser.element('#uploadPicture').send_keys('/Users/ekblb/Documents/Python/qa_guru/qa_guru_hm_selene/picture.jpg')

    browser.element('#dateOfBirth-wrapper').click().element('.react-datepicker__month-select').send_keys('January')
    browser.element('.react-datepicker__year-select').send_keys('1997')
    browser.all('.react-datepicker__week').element_by(have.text('8')).click()

    browser.element('#state').click().all('[id^="react-select"][id*="option"]').element_by(have.text('NCR')).click()
    browser.element('#city').click().all('[id^="react-select"][id*="option"]').element_by(have.text('Delhi')).click()

    browser.save_screenshot('result.png')

    browser.element('#submit').click()

    browser.element('html').should(have.text('Thanks for submitting the form'))
