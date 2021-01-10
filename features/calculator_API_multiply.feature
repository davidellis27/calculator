Feature: Test API Calculator Multiplication Functionality
 Show off the API multiplication capabilities of a calculator

Scenario Outline: Multiplication API - Two Positive
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to multiply
 Then I get result <result>

Examples: Two Positive
| url_1                            | url_2                                              | dictionary                       | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_mult | {"number_1" : 2, "number_2" : 3} | 6     |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_mult | {"number_1" : 5, "number_2" : 9} | 45    |

Scenario Outline: Multiplication API - One Negative, One Positive
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to multiply
 Then I get result <result>

Examples: One Negative, One Positive
| url_1                            | url_2                                              | dictionary                        | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_mult | {"number_1" : -2, "number_2" : 3} | -6    |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_mult | {"number_1" : -5, "number_2" : 2} | -10   |

Scenario Outline: Multiplication API - Two Negative
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to multiply
 Then I get result <result>

Examples: Two Negative
| url_1                            | url_2                                              | dictionary                         | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_mult | {"number_1" : -2, "number_2" : -3} | 6     |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_mult | {"number_1" : -5, "number_2" : -7} | 35    |
