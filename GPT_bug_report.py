import openai
from openai.error import OpenAIError
import json
import sys

#set the max conversation length so it doesnt go over the token limit (a limit of 20 is 10 messages back and fourth, one for the AI and one for the user.)
MAX_CONVERSATION_LENGTH = 20

#initial prompt, so the AI knows what it's ment to do
conversation = [{"role": "user", "content": "As a developer, create bug cards using the info provided. Use technical language. Templates: \"Precondition: \n Steps to reproduce: \n Expected behaviour: \n Actual behaviour: \n\" Acceptance criteria: \"\n [step-by-step]\" Follow templates & keep it clear for devs. Do not have any disclaimers or other text outside the templates. Use markdown to format"}]

#questions to the user
print("Welcome to the proof of concept gpt-bug-writer")
print("----------------------------------------------")
precon = input("Any preconditions? (if none just press enter) ")
print("\n")
reprod = input("How is the problem caused? (bullet point notes or plain english can be used) ")
print("\n")
expect_behav = input("What is the expected behaviour? ")
print("\n")
Actual_behav = input("What is the actual behaviour? ")
print("\n")
acc_crit = input("What is the Acceptance criteria? (bullet point notes or plain english can be used) ")

if precon == "":
        precon = "none"

conversation.append({"role": "user", "content": "The preconditions are: " + precon + "The steps to reporduce are: " + reprod + "The expected behaviour is: " + expect_behav + "The actual behaviour is: " + Actual_behav + "The acceptence criteria is: " + acc_crit})

def GPTapi():
    global conversation
    openai.api_key = "OPENAI-API-KEY"
    completion = None # Declare the variable with a default value
    try:
            
            completion = openai.ChatCompletion.create(
            model="gpt-4", #this is the 8k context model
            messages=conversation
            )

    #tell the user that the openAI had a problem
    except OpenAIError as e:
        print(f"Error: {str(e)}")
    
    if completion is not None:
        # Extract what GPT replies with, append it to the array and print it
        forjson = str(completion.choices[0].message)
        response_dict = json.loads(forjson)
        content = response_dict["content"]
        conversation.append({"role": "assistant", "content": content})
        print(content)
    return
GPTapi()
print("\n")
print("\n")
print("If any edits are required you can now freely talk to the AI, type \"done\" to finish")
print("\n")
#If any other edits are required, the user can interact with the AI with context to change it.
finished = False
while finished == False:
    extra = input("? ")
    if extra == "done":
        sys.exit()
    conversation.append({"role": "user", "content": extra})
    if len(conversation) > MAX_CONVERSATION_LENGTH:
            conversation = conversation[-MAX_CONVERSATION_LENGTH:]
    GPTapi()

