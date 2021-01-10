Feature: Test API Calculator Subtraction Functionality
 Show off the API subtraction capabilities of a calculator

Scenario Outline: Subtraction API - Two Positive
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to subtract
 Then I get result <result>

Examples: Two Positive
| url_1                            | url_2                                              | dictionary                       | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_sub | {"number_1" : 2, "number_2" : 3} | -1     |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_sub | {"number_1" : 5, "number_2" : 9} | -4     |

Scenario Outline: Subtraction API - One Negative, One Positive
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to subtract
 Then I get result <result>

Examples: One Negative, One Positive
| url_1                            | url_2                                              | dictionary                        | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_sub | {"number_1" : -2, "number_2" : 3} | -5     |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_sub | {"number_1" : -5, "number_2" : 2} | -7     |

Scenario Outline: Subtraction API - Two Negative
 Given Calculator API is available <url_1>
 When I pass <url_2> and <dictionary> to calculator API to subtract
 Then I get result <result>

Examples: Two Negative
| url_1                            | url_2                                              | dictionary                         | result |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_sub | {"number_1" : -2, "number_2" : -3} | 1      |
| http://localhost:5000/calculator | http://localhost:5000/calculator/v1/calculator_sub | {"number_1" : -5, "number_2" : -7} | 2      |
