Feature: Test Calculator Division Functionality
 Show off the division capabilities of a calculator

Scenario:Division - Two Positive
 Given Calculator app is run
 When I input 2 and 3 to calculator to divide
 Then I get result -1

Scenario:Division - One Negative, One Positive
 Given Calculator app is run
 When I input -2 and 3 to calculator to divide
 Then I get result -5

Scenario:Division - Two Negative
 Given Calculator app is run
 When I input -2 and -3 to calculator to divide
 Then I get result 1
