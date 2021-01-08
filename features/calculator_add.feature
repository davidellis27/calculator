Feature: Test Calculator Addition Functionality
 Show off the addition capabilities of a calculator

Scenario: Addition - Two Positive
 Given Calculator app is run
 When I input 2 and 3 to calculator to add
 Then I get result 5

Scenario:Addition - One Negative, One Positive
 Given Calculator app is run
 When I input -2 and 3 to calculator to add
 Then I get result 1

Scenario: Addition - Two Negative
 Given Calculator app is run
 When I input -2 and -3 to calculator to add
 Then I get result -5

Scenario Outline: Addition - Two Numbers
 Given Calculator app is run
 When I input <number1> and <number2> to calculator to add
 Then I get result <result> 

Examples:
| number1 | number2 | result |
| 2       | 3       | 5      |
| -2      | 3       | 1      |
| -2      | -3      | -5     |

Scenario Outline: Addition - Two Numbers with Grouped Examples
 Given Calculator app is run
 When I input <number1> and <number2> to calculator to add
 Then I get result <result> 

Examples: Two Positive
| number1 | number2 | result |
| 2       | 3       | 5      |
| 2       | 3       | 5      |

Examples: One Negative, One Positive
| number1 | number2 | result |
| -2      | 3       | 1      |
| -2      | 3       | 1      |

Examples: Two Negtive
| number1 | number2 | result |
| -2      | -3      | -5     |
| -2      | -3      | -5     |
