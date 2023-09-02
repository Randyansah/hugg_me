import gradio as gr
from main import nlp
app=gr.Interface(fn=nlp,inputs=([gr.Textbox(placeholder="SELECT AN OPTION"),gr.Textbox(placeholder="ENTER TEXT")]), outputs=gr.outputs.Textbox(label="Generated Text"))