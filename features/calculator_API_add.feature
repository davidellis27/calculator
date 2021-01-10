Feature: Test API Calculator Addition Functionality
 Show off the API addition capabilities of a calculator

Scenario Outline: Addition API - Two Positive
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to add
 Then I get result <result>

Examples: Two Positive
| url_1                            | url_2                                              | dictionary                       | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_add | {"number_1" : 2, "number_2" : 3} | 5      |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_add | {"number_1" : 5, "number_2" : 9} | 14     |

Scenario Outline: Addition API - One Negative, One Positive
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to add
 Then I get result <result>

Examples: One Negative, One Positive
| url_1                            | url_2                                              | dictionary                        | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_add | {"number_1" : -2, "number_2" : 3} | 1      |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_add | {"number_1" : -5, "number_2" : 2} | -3     |

Scenario Outline: Addition API - Two Negative
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to add
 Then I get result <result>

Examples: Two Negative
| url_1                            | url_2                                              | dictionary                         | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_add | {"number_1" : -2, "number_2" : -3} | -5     |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_add | {"number_1" : -5, "number_2" : -7} | -12    |
