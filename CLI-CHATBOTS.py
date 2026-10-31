
import ollama

print("================================")
print("       CLI AI CHATBOT")
print("================================")
print("AI: Hello! How can I help you?")
print("Type 'exit' to stop the chatbot.")

while True:

    # Get input from user
    user_input = input("\nYou: ")

    # Stop chatbot
    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break

    # Generate AI response
    response = ollama.generate(
        model="llama3.2",
        prompt=user_input
    )

    # Display AI response
    print("\nAI:", response["response"])
