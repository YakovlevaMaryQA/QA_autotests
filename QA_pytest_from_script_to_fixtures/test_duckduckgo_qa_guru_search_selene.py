from selene import browser, be, have

def test_browser_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('QA').press_enter()
    browser.element('html').should(have.text('QA'))
    assert browser.should(have.title_containing('QA'))
    print(' По запросу "QA" результаты найдены на странице')

def test_browser_search_negative(open_browser):
    random_string = 'sfdghfdshhhhhhhhhhhhhhhhhhhhhhhhhhрр'
    browser.element('[name="q"]').should(be.blank).type(random_string).press_enter()
    assert browser.element('#web_content_wrapper').should(have.text('ничего не найдено'))
    print('По запросу "sfdghfdshhhhhhhhhhhhhhhhhhhhhhhhhhрр" результаты не найдены на странице')
