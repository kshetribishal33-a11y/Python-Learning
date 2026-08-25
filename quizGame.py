quiz={
    "Capital of Nepal? ": "kathmandu",
    "National Animal of Nepal? ": "cow",
    "National Bird of Nepal? ": "danphe",
    "9/3" :"3"
}

score =0
for question, answer in quiz.items():
    user_answer=input(question+ "")

    if user_answer.lower() == answer:
        print("Correct!")
        score+=1

    else:
        print("Wrong!")
        print("Correct answer is ",answer)

print("Your score:", score, "/", len(quiz))