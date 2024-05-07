#KBC
#Use list data type to store questions and their correct answers
questions = [
  ["Who is the PM of India", "Putin", "Rahul", "Modi", "None", 3],
  ["What is the capital of Italy", "Madrid", "Rome", "Delhi", "Dhaka", 2],
  ["What is the currency of Japan", "Rupaih", "Euro", "Rupee", "Yen", 4],
  [
    "Who invented the light bulb", "Edison", "Graham Bell", "Newton", "None", 1
  ],
  [
    "What is the 2nd tallest mountain in the world", "K2", "Mount Everest",
    "Kailash", "Niligiris", 1
  ],
  [
    "What is the largest mammal in the world", "Bats", "Human", "Whale",
    "Snake"
  ], ["Who discovered America", "Colombus", "Fracis", "Pop", "Mc Arthur", 1],
  [
    "What is the second largest desert in the world", "Kalahari",
    "Arctic Polar", "Thar", "Amazon", 2
  ], ["Who discovered gravity", "Edison", "Graham Bell", "Newton", "None", 3],
  [
    "Who was the first woman to win a Nobel Prize", "Nelson Mandela",
    "Marie Curie", "Karl Barry", "Annie Ernaux", 2
  ]
]

levels = [1000, 2000, 4000, 8000, 10000, 20000, 40000, 80000, 160000, 320000]

for i in range(0,len(questions)):
  question=questions[i]
  print(f"Question for Rs{levels[i]}:")
  print(questions[i][0])
  print(f"1.{question[1]}     2.{question[2]}")
  print(f"3.{question[3]}     4.{question[4]}")
  reply=int(input("Enter the option[1-4] or 0 to quit:"))
  if reply==0:
    money=levels[i-1]
    print(f"quit with money {money}")
  if(reply==question[-1]):
    print(f"Correct answer, Won {levels[i]}")
  else:
    print("Wrong answer")
    break


#Dsiplay the final amount the person is taking home after playing the game
