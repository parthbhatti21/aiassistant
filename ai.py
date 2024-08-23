from cohere import Client
import audio
api_key = "FvgXRMGeiYpsMoJfym1pffFKgquICXPs0IeHuTKi"

client = Client(api_key=api_key)
def ai(text):
    prompt = text+"generate small output"
    model = "command"

    try:
        response = client.generate(model=model, prompt=prompt)

        generations = response.generations
        for generation in generations:
            # print("Assistant: ",generation.text)
            audio.text_to_audio_and_play(generation.text)
        
    except Exception as e:
        print("An error occurred:", str(e))