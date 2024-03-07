import gradio as gr
from run import SESSION_NAME, get_response, get_session_history

theme = gr.themes.Soft(
    primary_hue="yellow",
    secondary_hue="neutral",
    neutral_hue="neutral",
    font=gr.themes.GoogleFont('Inconsolata')
)

with gr.Blocks(theme=theme) as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown('## Chatbot')
            gr.ChatInterface(
                    fn=get_response,
                    retry_btn=None,
                    undo_btn=None,
            )

        with gr.Column():
            gr.Markdown(f'## Full chat history for session: "{SESSION_NAME}"')
            gr.Interface(
                    fn=get_session_history,
                    inputs=None,
                    outputs=gr.Textbox(),
                    live=True,
                    allow_flagging="never",
            )

demo.launch()
