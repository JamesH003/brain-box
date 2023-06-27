# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/brain-box/main/run.py) | ![screenshot](documentation/testing/linter-testing-run.png) | Pass: No Errors |
| questions.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/brain-box/main/questions.py) | ![screenshot](documentation/testing/linter-testing-questions.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/chrome-testing.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/firefox-testing.png) | Works as expected |
| Edge | ![screenshot](documentation/testing/edge-testing.png) | Works as expected |
| Safari | ![screenshot](documentation/testing/safari-testing.png) | Does not work on Safari |
| Brave | ![screenshot](documentation/testing/brave-testing.png) | Works as expected |
| Opera | ![screenshot](documentation/testing/opera-testing.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testing/iphone-responsiveness.png) | Not responsive |
| Tablet (DevTools) | ![screenshot](documentation/testing/ipad-responsiveness.png) | Not responsive |
| Desktop | ![screenshot](documentation/testing/desktop-responsiveness.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](documentation/testing/lighthouse-testing.png) | Few warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Screenshot |
| --- | --- | --- | --- | --- |
| Name Input | | | | |
| | Enter a name | Field will only accept 2-15 letters | Pass | ![screenshot](documentation/testing/def-prog-min-letters.png) |
| Category Selection | | | | |
| | Enter 1 or 2 to choose a category | Field will only accept 1 or 2 | Pass | ![screenshot](documentation/testing/def-prog-numbers.png) |
| Answer Input | | | | |
| | Enter a,b,c,d to select an answer | Field will only accept the letters a,b,c,d uppercase or lowercase | Pass | ![screenshot](documentation/testing/def-prog-abcd.png) |
| Play Again | | | | |
| | Enter yes/no to play again | Field will accept any input that begin with y or n | Pass | ![screenshot](documentation/testing/def-prog-yn.png) |


## Bugs

- Unable to input text to the terminal on Safari desktop or mobile.

    ![screenshot](documentation/testing/safari-testing.png)

- Flag emojis not displaying on all browsers tested

    ![screenshot](documentation/testing/flags-bug.png)


There are no remaining bugs that I am aware of.
