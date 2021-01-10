Feature: Test API Calculator Division Functionality
 Show off the API division capabilities of a calculator

Scenario Outline: Division API - Two Positive
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to divide
 Then I get result <result>

Examples: Two Positive
| url_1                            | url_2                                              | dictionary                       | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_div | {"number_1" : 6, "number_2" : 3} | 2      |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_div | {"number_1" : 6, "number_2" : 2} | 3      |

Scenario Outline: Division API - One Negative, One Positive
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to divide
 Then I get result <result>

Examples: One Negative, One Positive
| url_1                            | url_2                                              | dictionary                        | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_div | {"number_1" : 8, "number_2" : -2} | -4     |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_div | {"number_1" : 8, "number_2" : -4} | -2     |

Scenario Outline: Division API - Two Negative
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to divide
 Then I get result <result>

Examples: Two Negative
| url_1                            | url_2                                              | dictionary                         | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_div | {"number_1" : -8, "number_2" : -2} | 4      |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_div | {"number_1" : -8, "number_2" : -4} | 2      |
