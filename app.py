import gradio as gr
from chatbot import ai_chatbot
import json
import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", 'branding.json'))) as f:
    brand_info = json.load(f)['brand']

with gr.Blocks(title=brand_info["organizationName"]) as demo:
    
    gr.HTML(
        f"<div style='display: flex; align-items: center; justify-content: center; margin-bottom: 20px;'>"
        f"<img src='{brand_info['logo']['title']}' alt='{brand_info['organizationName']} Logo' style='height: 100px;'>"
        "</div>"
    )
    gr.ChatInterface(
        fn=ai_chatbot,
        title=brand_info["organizationName"],
        description=brand_info["slogan"],
        examples=[
            ["Hi, how are you?", []],
            ["What is AI?", []],
            ["Can you explain machine learning?", []],
            ["How does a neural network work?", []],
            ["What is natural language processing?", []]
        ],
    )

if __name__ == "__main__":
    demo.launch()








