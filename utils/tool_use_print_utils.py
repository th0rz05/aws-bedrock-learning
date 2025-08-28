# utils/tool_use_print_utils.py
import logging

def header():
    print("=" * 60)
    print("🌤️  Weather Assistant (powered by Bedrock)")
    print("Type a location (or 'x' to exit).")
    print("=" * 60)

def footer():
    print("=" * 60)
    print("Goodbye! 👋")
    print("=" * 60)

def separator():
    print("-" * 60)

def call_to_bedrock(conversation):
    logging.info("[Bedrock] Sending conversation:")
    for msg in conversation:
        logging.info(f"  {msg['role']}: {msg['content']}")

def model_response(text):
    print(f"\n🤖 Model: {text}\n")

def tool_use(tool_name, input_data):
    print(f"🔧 Using {tool_name} with input: {input_data}")
