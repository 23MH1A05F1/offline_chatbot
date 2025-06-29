from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load smarter model
model_name = "microsoft/DialoGPT-medium"  # Upgrade from 'small'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("🤖 Offline AI Chatbot is ready! Type 'exit' to quit.\n")

# Start chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye! Chat session ended.")
        break

    # Tokenize user input and append end-of-string token
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Generate a response without remembering previous chat (prevents loops)
    output_ids = model.generate(
        input_ids,
        max_length=150,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.75,
        no_repeat_ngram_size=3
    )

    # Decode response
    reply = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Print and save reply
    print("Bot:", reply)
    
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"You: {user_input}\nBot: {reply}\n\n")