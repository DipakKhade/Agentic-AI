from tiktoken import encoding_for_model

en = encoding_for_model("gpt-4")

user_input = "what is 2+2"
token = en.encode(user_input)

print('tokens', token)

decoded_token = en.decode(token)

print('decoded token', decoded_token)