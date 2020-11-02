def inputTime():
  print("Please input your athletes' times. Minimum of 4 and a maximum of 8. Input '//' to finish input")
  ix = 0
  for ix in range (0,7):
    print("Hello World")
def main():
  global genders
  global gender
  global athleteCount
  global athleteTime
  print("Hello, would you like to view record times or input into the database?")
  response = input()
  if(str(response.casefold("Input"))):
    inputTime()
print("Hi")
main()