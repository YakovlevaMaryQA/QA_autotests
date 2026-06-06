from selene import browser, be, have

# Opened DuckDuckGo, searched for 'QA', and verified that 'QA' appears in the search results

browser.open('https://duckduckgo.com')
browser.element('[name="q"]').should(be.blank).type('QA').press_enter()
browser.element('html').should(have.text('QA'))
