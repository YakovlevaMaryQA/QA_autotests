from selene import browser, be, have

# Opened Yandex, searched for 'qa.guru', and verified that 'guru' appears in the search results

browser.open('https://ya.ru')
browser.element('[name="text"]').should(be.blank).type('qa.guru').press_enter()
browser.element('.main__center').should(have.text('guru'))
