from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_questions(text):
    prompt = f"Generate 3 logic-based or comprehension questions:\n{text[:1000]}"
    generated = generator(prompt, max_length=200, num_return_sequences=1)
    lines = generated[0]["generated_text"].split('\n')
    return [line for line in lines if '?' in line][:3]

def evaluate_answer(user_ans, correct_ans):
    if user_ans.strip().lower() == correct_ans.strip().lower():
        return "✅ Correct!"
    else:
        return f"❌ Incorrect. Expected: {correct_ans}"
