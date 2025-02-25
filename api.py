from flask import Flask, request, jsonify, Response
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

weights = './checkpoint-550'

model = AutoModelForCausalLM.from_pretrained(weights)
tokenizer = AutoTokenizer.from_pretrained(weights)

pipe = pipeline(
   task="text-generation",
   model=model,
   tokenizer=tokenizer,
   max_length=200
)

prompts_responses = {}

@app.route('/ask', methods=['POST'])
def ask():
    """Receive a prompt and generate a response."""
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    result = pipe(f"[s][INST] {prompt} [/INST]")
    full_response = result[0]['generated_text']

    return jsonify({"response": full_response})



@app.route('/stream', methods=['POST'])
def ask2():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    def generate_response():
        yield "Starting response generation...\n"
        time.sleep(1)  # Simulate delay

        result = pipe(f"[s][INST] {prompt} [/INST]")

        full_response = result[0]['generated_text']
        for chunk in full_response.split():
            yield f"{chunk} "
            time.sleep(0.1) 

        yield "\nResponse generation complete."

    return Response(generate_response(), content_type='text/plain')


@app.route('/health', methods=['GET'])
def mock_response():
    """Mock endpoint to return a fixed response."""

    message = "healthy"

    return jsonify({"response": message})


@app.route('/responses', methods=['GET'])
def get_responses():
    """Return all prompts and responses."""
    return jsonify(prompts_responses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)

