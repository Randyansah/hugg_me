import gradio as gr
from main import nlp
from main import selection
app=gr.Interface(fn=nlp,inputs=[gr.Number(laceholder="SELECT AN NLP TASK"),gr.Textbox(placeholder="ENTER TEXT")],\
                  outputs=["text"],title='HUGGING PHACE',\
                    description=selection)
app.launch()
