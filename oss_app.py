import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto"
)

conversation_history = [
    {"role": "system", "content": "You are a helpful personal assistant. Keep answers simple, safe, and clear."}
]

def chat_fn(message, chat_history):
    global conversation_history

    if not message.strip():
        return "", chat_history

    conversation_history.append({"role": "user", "content": message})

    text = tokenizer.apply_chat_template(
        conversation_history,
        tokenize=False,
        add_generation_prompt=True
    )

    model_inputs = tokenizer([text], return_tensors="pt")

    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=200,
        temperature=0.7
    )

    generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    conversation_history.append({"role": "assistant", "content": response})

    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": response})

    return "", chat_history

def clear_chat():
    global conversation_history
    conversation_history = [
        {"role": "system", "content": "You are a helpful personal assistant. Keep answers simple, safe, and clear."}
    ]
    return []

with gr.Blocks() as demo:
    gr.Markdown("# Open Source Assistant - Qwen2.5")
    chatbot = gr.Chatbot(height=500)
    msg = gr.Textbox(label="Message", placeholder="Type your question here...")
    clear = gr.Button("Clear Chat")

    msg.submit(chat_fn, [msg, chatbot], [msg, chatbot])
    clear.click(clear_chat, outputs=[chatbot])

demo.launch()