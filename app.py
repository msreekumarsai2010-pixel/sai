import random
import gradio as gr

def random_response(message, history):
    return random.choice(["Yes", "No"])
title = "SAIGPT - Created by Sreekumar.M"
description = "Testing of chatbot"
demo = gr.ChatInterface(
    random_response, 
    title = title,
    description= description,
    type="messages", 
    autofocus=False)

if __name__ == "__main__":
    demo.launch()