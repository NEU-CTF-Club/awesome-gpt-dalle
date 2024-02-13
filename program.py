from openai import OpenAI

userkey = input("Enter your api key I won't give you mine")

client = OpenAI(api_key=userkey)

prompt = input("Enter your image prompt: ")

print(client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  n=1,
  size="1024x1024"
))
