*** Settings ***
Library         SwagLabsLibrary                 is_headless=${False}
Suite Setup     Set Log Level    TRACE
Test Setup      Open Swaglabs In Browser
Test Teardown   Close All Swaglabs Browser

*** Variables ***
${invalid_username_and_password_err_msg}          Epic sadface: Username and password do not match any user in this service
${locked_out_user_err_msg}                        Epic sadface: Sorry, this user has been locked out.
${username_required_err_msg}                      Epic sadface: Username is required
${password_required_err_msg}                      Epic sadface: Password is required
${valid_username}                                 standard_user
${valid_password}                                 secret_sauce

*** Test Cases ***
Verify That User Cannot Login With Invalid Username And Password
    [Template]              Verify Login Using Invalid Credentials
    ${valid_username}       invalid_password      ${invalid_username_and_password_err_msg}
    invalid_username        ${valid_password}     ${invalid_username_and_password_err_msg}
    invalid_username        invalid_password      ${invalid_username_and_password_err_msg}
    locked_out_user         ${valid_password}     ${locked_out_user_err_msg}
    ${EMPTY}                ${EMPTY}              ${username_required_err_msg}
    standard_user           ${EMPTY}              ${password_required_err_msg}
    ${EMPTY}                ${valid_password}     ${username_required_err_msg}

Verify That User With Valid Username And Password Can Successfully Login
    Login To Swaglabs        username=${valid_username}        password=${valid_password}
    Wait Until Products Page Is Visible


Verify That User Can Logout From Sauce Lab Demo App
    Login To Swaglabs        username=${valid_username}        password=${valid_password}
    Wait Until Products Page Is Visible
    Logout From Swaglabs
    Wait Until Login Page Is Visible

*** Keywords ***
Verify Login Using Invalid Credentials
    [Arguments]     ${username}         ${password}         ${exp_err_msg}
    Login To Swaglabs    username=${username}        password=${password}
    Login Error Msg Should Be    err_msg=${exp_err_msg}
    [Teardown]      Reload Swaglabs Browser
