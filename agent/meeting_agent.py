import openai

def extract_summary_and_actions(transcript, openai_api_key):
    openai.api_key = openai_api_key

    system_prompt = "You are an assistant that reads a meeting transcript and extracts a summary and action items in structured format."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Transcript:\n{transcript}\n\nExtract the summary, participants, and a table of action items (task, person, due date)."}
        ]
    )

    return response['choices'][0]['message']['content']
