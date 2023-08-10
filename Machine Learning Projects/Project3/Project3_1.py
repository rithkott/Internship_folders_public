import openai

api_key = ""

openai.api_key = api_key

def get_answer(question,knowledge):
    prompt = f"Answer the following question based on the knowledge i am providing. Dont answer from what you have been trained. if you cant answer from the knowledge given tell that you dont have enough information to answer the same: {question} Knowledge: {knowledge} \nAnswer:"
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo", 
        prompt=prompt,
        max_tokens=500 
    )
    
    answer = response.choices[0].text if response.choices else "No answer found"
    return answer


while True:
    user_question = input("Ask me a question: ")
    knowledge=""
    if user_question.lower() == "exit":
        print("Goodbye!")
        break
    
    answer = get_answer(user_question,knowledge)
    print("Answer:", answer)
