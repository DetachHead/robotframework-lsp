*** Settings ***
Library           DupeHybridKeywords.py

*** Variables ***
${INDENT}         ${SPACE * 4}

*** Test Cases ***
Using keyword defined multiple times fails
    [Documentation]    FAIL Keyword with same name defined multiple times.
    Defined TWICE

Keyword with embedded arguments defined multiple times fails at run-time
    [Documentation]    FAIL
    ...    Library 'DupeHybridKeywords' contains multiple keywords matching name 'Embedded twice':
    ...    ${INDENT}EMBEDDED \${ARG}
    ...    ${INDENT}Embedded \${twice}
    Embedded twice
#!  ^^^^^^^^^^^^^^ Multiple keywords matching: 'Embedded twice' in 'DupeHybridKeywords'.

Exact duplicate is accepted
    Exact dupe is OK
