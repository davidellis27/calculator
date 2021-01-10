Feature: Test CLI Calculator Addition Functionality
 Show off the CLI addition capabilities of a calculator

Scenario: Addition CLI - Two Positive
 Given Calculator CLI app is run
 When I input 2 and 3 to calculator CLI to add
 Then I get result 5

Scenario:Addition CLI - One Negative, One Positive
 Given Calculator CLI app is run
 When I input -2 and 3 to calculator CLI to add
 Then I get result 1

Scenario: Addition CLI - Two Negative
 Given Calculator CLI app is run
 When I input -2 and -3 to calculator CLI to add
 Then I get result -5

Scenario Outline: Addition CLI - Two Numbers
 Given Calculator CLI app is run
 When I input <number1> and <number2> to calculator CLI to add
 Then I get result <result> 

Examples:
| number1 | number2 | result |
| 2       | 3       | 5      |
| -2      | 3       | 1      |
| -2      | -3      | -5     |

Scenario Outline: Addition CLI - Two Numbers with Grouped Examples
 Given Calculator CLI app is run
 When I input <number1> and <number2> to calculator CLI to add
 Then I get result <result> 

Examples: Two Positive
| number1 | number2 | result |
| 2       | 3       | 5      |
| 2       | 3       | 5      |

Examples: One Negative, One Positive
| number1 | number2 | result |
| -2      | 3       | 1      |
| -2      | 3       | 1      |

Examples: Two Negative
| number1 | number2 | result |
| -2      | -3      | -5     |
| -2      | -3      | -5     |
