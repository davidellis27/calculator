Feature: Test Calculator Multiplication Functionality
 Show off the multiplication features of a calcuator

Scenario:Multiplication - Two Positive
 Given Calculator app is run
 When I input 2 and 3 to calculator to multiply
 Then I get result 6

Scenario:Multiplication - One Negative, One Positive
 Given Calculator app is run
 When I input -2 and 3 to calculator to multiply
 Then I get result -6

Scenario:Multiplication - Two Negative
 Given Calculator app is run
 When I input -2 and -3 to calculator to multiply
 Then I get result 6
