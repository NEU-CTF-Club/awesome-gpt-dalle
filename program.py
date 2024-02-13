from openai import OpenAI
import sys
#pass in ur api key here
userkey = sys.argv[1]

client = OpenAI(api_key=userkey)

prompt = input("Enter your image prompt: ")

print(client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  n=1,
  size="1024x1024"
))
