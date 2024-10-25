from flask import Flask, request, jsonify
from ast_engine import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data.get('rule_string')
    ast = create_rule(rule_string)
    return jsonify(ast)

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.json
    rules = data.get('rules')
    combined_ast = combine_rules(rules)
    return jsonify(combined_ast)

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json
    ast = data.get('ast')
    user_data = data.get('data')
    result = evaluate_rule(ast, user_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
