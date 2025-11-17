"""
Full Name: Talan Wessman
Class-Section: IS 250-01
Assignment Title: Swtup Activity
Submission Date: November 17th
"""
"""
#define your function as calculate_average()
#prompt the user to enter the scores
#add the three scores together
#divide the total score by the number of scores entered
#display the individual scores and the average
Do not write any Python code in this section.
Your pseudocode should describe your overall approach in your own words.
"""

# Your Python code begins below this line.
#define the function
def calculate_average():
  #prompt user to enter score 1
  score1=int(input("Enter the first score: "))
  #prompt the user to enter score 2
  score2=int(input("Enter the second score: "))
  #prompt the user to enter score 3
  score3=int(input("Enter the third score: "))
  #calculate the average of the 3 scores
  average= (score1+score2+score3)/3
  #print the average of the 3 scores
  print("First score:",score1,"\n""Second score:",score2,"\n","Third Score:",score3,"\n","The average score is:",average,)


# Call your function when your program is ready
calculate_average()   
  
