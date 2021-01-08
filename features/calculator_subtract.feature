Feature: Test Calculator Subtraction Functionality
 Show off the subtraction capabilities of a calculator

Scenario:Subtraction - Two Positive
 Given Calculator app is run
 When I input 2 and 3 to calculator to subtract
 Then I get result -1

Scenario:Subtraction - One Negative, One Positive
 Given Calculator app is run
 When I input -2 and 3 to calculator to subtract
 Then I get result -5

Scenario:Subtraction - Two Negative
 Given Calculator app is run
 When I input -2 and -3 to calculator to subtract
 Then I get result 1
