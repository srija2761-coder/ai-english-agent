import ollama

def correct(user_input):
     prompt=f"""
Consider you as a English Grammar Corrector
Correct the grammartical errors in the user's sentence
User Input:{user_input}

Rules:
1.Correct the grammar only
2.Do not change the meaning 
3.Keep the original tense unless it is grammatically incorrect
4.Your output must be identical to the corrected sentence
5.Don't rewrite the given sentence in a more formal or different style.

Task: Return only the corrected sentence

"""
     
     response=ollama.chat(
          model="llama3.2",
          messages=[{
               "role":"user",
               "content":prompt
          }]
     )

     return response["message"]["content"]

def explain(original, corrected):
    prompt = f"""
You are an English grammar assistant.

RULES:
- Do NOT give long explanations
- Do NOT teach grammar concepts
- Mention the tense used and tense rules
- Do NOT repeat the sentence multiple times
- Do NOT use headings or bullet points
- Keep response in 3-4 simple sentences only

TASK:
1. Say what is wrong in the original sentence
2. Say why it is wrong in a simple way
3. Confirm why corrected sentence is right
Original Sentence:
{original}

Corrected Sentence:
{corrected}

"""
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip()