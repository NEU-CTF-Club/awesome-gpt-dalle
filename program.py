from openai import OpenAI

client = OpenAI()

prompt = input("Enter your image prompt: ")

print(client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  n=1,
  size="1024x1024"
))
