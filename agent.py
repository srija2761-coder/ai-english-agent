import ollama
import json
def correct(user_input):
    prompt = f"""
You are an English grammar correction assistant.

User Input:
{user_input}

Instructions:
1. Correct ONLY grammatical errors.
2. Preserve the original meaning.
3. Preserve the original tense whenever possible.
4. Do NOT rewrite the sentence to make it more formal or stylistic.
5. If a word or phrase is grammatically incorrect, replace it with the correct grammatical form.
6. Remove unnecessary words when needed.
7. Use the simplest grammatically correct sentence.
8. If the sentence is already correct, return it unchanged.
9. Return ONLY the corrected sentence. No explanations.

Example Corrections:
Input: I am agree with you.
Output: I agree with you.

Input: She don't like coffee.
Output: She doesn't like coffee.

Input: He go to school every day.
Output: He goes to school every day.

Input: I am knowing him.
Output: I know him.

Input: I prefer tea than coffee.
Output: I prefer tea to coffee.

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
You are an English grammar teacher.

Original Sentence:
{original}

Corrected Sentence:
{corrected}

Explain ONLY the actual grammar mistakes that were corrected.

Rules:
1. Do not mention errors that do not exist.
2. If the correction involves a preposition, explain the preposition.
3. If the correction involves verb tense, explain the tense.
4. If the correction involves subject-verb agreement, explain only that.
5. If the sentence only required capitalization or punctuation, explain only those.
6. Keep the explanation under 80 words.
7. Do not invent grammatical errors.
8. Do not add any bullet points or headings to the explanation
"""
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip()
import ollama
import json
import re

import ollama
import json
import re

def rewrite_styles(text):

    prompt = f"""
You are an English writing assistant.

Rewrite the following sentence into five different styles.

Sentence:
{text}

Return ONLY valid JSON.

{{
    "professional": "",
    "formal": "",
    "friendly": "",
    "concise": "",
    "advanced": ""
}}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    output = response["message"]["content"].strip()

    start = output.find("{")
    end = output.rfind("}") + 1

    if start != -1 and end != 0:
        json_text = output[start:end]
        return json.loads(json_text)

    return {
    "professional": "",
    "formal": "",
    "friendly": "",
    "concise": "",
    "advanced": ""
}