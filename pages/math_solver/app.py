from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"
@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    problem = data.get('problem')

    if not problem:
        return jsonify({'error': 'No problem provided'}), 400

    # Query OpenAI to solve the problem
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Solve this math problem: {problem}"}
            ]
        )
        solution = response.choices[0].message['content'].strip()
        return jsonify({'solution': solution})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
