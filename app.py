from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# List of relevant keywords for computer and electrical terms
relevant_keywords = relevant_keywords = [
    'algorithm', 'bandwidth', 'bit', 'byte', 'cache', 'compiler', 'CPU', 'data', 'database', 
    'debug', 'encryption', 'ethernet', 'firewall', 'firmware', 'GPU', 'hardware', 'IP', 
    'kernel', 'LAN', 'logic', 'memory', 'microcontroller', 'network', 'protocol', 
    'RAM', 'ROM', 'router', 'software', 'SQL', 'TCP', 'USB', 'virtualization', 'voltage',
    'amplifier', 'circuit', 'current', 'resistor', 'capacitor', 'inductor', 'transistor', 
    'diode', 'oscillator', 'power', 'signal', 'switch', 'transformer', 'watt', 'ohm',
    'API', 'binary', 'bus', 'client', 'cloud', 'data center', 'debugger', 'domain', 'firmware', 
    'gateway', 'IDE', 'internet', 'load balancer', 'protocol', 'server', 'shell', 'socket',
    'subnet', 'thread', 'token', 'UUID', 'VPN', 'websocket', 'XOR', 'zip', 'driver', 
    'encryption',  'modem', 'router', 'repository', 'version control', 'data structure',
    'queue', 'stack', 'heap', 'linker', 'loader', 'metadata', 'serialization', 'replication', 
    'synchronization', 'transaction', 'distributed system', 'container', 'deployment', 
    'microservices', 'serverless', 'load testing', 'scalability', 'latency', 'bandwidth', 'throughput',
    'client-server', 'proxy', 'endpoint', 'API key', 'authentication', 'authorization', 'cookie',
    'session', 'header', 'payload', 'endpoint', 'request', 'response', 'cache', 'CDN', 'routing'
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    term = request.args.get('term', '').capitalize()
    if term:
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{term}')
        if response.status_code == 200:
            results = response.json()
            filtered_results = []
            for item in results:
                if any(keyword in item['word'].lower() for keyword in relevant_keywords):
                    filtered_results.append(item)
            if not filtered_results:
                filtered_results = [{"word": term, "meanings": [{"definitions": [{"definition": "Term not found."}]}]}]
        else:
            filtered_results = [{"word": term, "meanings": [{"definitions": [{"definition": "Term not found."}]}]}]
    else:
        filtered_results = [{"word": "", "meanings": [{"definitions": [{"definition": "No term provided."}]}]}]
    return jsonify(filtered_results)

if __name__ == '__main__':
    app.run(debug=True)
