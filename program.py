from openai import OpenAI

client = OpenAI(api_key="sk-YouWinAndFoundMyGPTKey!GoGetY0urPrize")

prompt = input("Enter your image prompt: ")

print(client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  n=1,
  size="1024x1024"
))
