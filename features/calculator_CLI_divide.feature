Feature: Test Calculator Division Functionality
 Show off the division capabilities of a calculator

Scenario:Division - Two Positive
 Given Calculator CLI app is run
 When I input 6 and 2 to calculator to divide
 Then I get result 3

Scenario:Division - One Negative, One Positive
 Given Calculator CLI app is run
 When I input 6 and 3 to calculator to divide
 Then I get result 2

Scenario:Division - Two Negative
 Given Calculator CLI app is run
 When I input 21 and 3 to calculator to divide
 Then I get result 7
