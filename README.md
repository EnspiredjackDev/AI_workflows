# AI Workflows  
  
## Info
- Uses GPT-4 API to create a bug report in a given template using a step-by-step guide of user input.  
- Output can be edited again by the AI from another prompt by the user at the end with full context given to the AI  
- Max messages between the AI and the user can be set by editing `MAX_CONVERSATION_LENGTH` it is 20 by default  

## Requirements  
- The openai library must be installed to run the API  
- A GPT-4 cabable API key must be used to get the full capacity of AI  

## Issues  
- GPT-4 is quite slow so a prompt could take upto a minute for a response, depending how busy openAI's servers are  

## GPT-3?
To change to GPT-3 edit `model="gpt-4"` to `model="gpt-3.5-turbo"` on line 37
