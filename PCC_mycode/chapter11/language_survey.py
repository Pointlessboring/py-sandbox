# Define q question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# show the question, and store responses to question.
my_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_responses(response)

# Show the survey results
print("\nThank you to everyone who participated in the study")
my_survey.show_results()