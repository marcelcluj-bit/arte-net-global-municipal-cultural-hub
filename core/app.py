# =====================================================================
# ARTE-NET GLOBAL OPEN-SOURCE MUNICIPAL REPOSITORY BOOTSTRAPPER
# License: MIT License (Free for any Municipality or Cultural Entity)
# Repository: https://github.com/arte-net-global/municipal-cultural-hub
# =====================================================================
import os
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Configuration
app.config['MUNICIPALITY_NAME'] = os.environ.get('MUNICIPALITY_NAME', 'Global Cultural City')
app.config['HUB_CURRENCY'] = 'ART-TOKEN'

HOME_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>ARTE-NET Hub - {{ municipality }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f6f7; color: #333; }
        .container { max-width: 800px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; }
        .badge { background: #16a085; color: white; padding: 5px 10px; border-radius: 4px; font-size: 0.9em; }
        ul { line-height: 1.8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>ARTE-NET Cultural Hub: <span class="badge">{{ municipality }}</span></h1>
        <p>Welcome to the open-source municipal node for art promotion, social incubation, and asset tokenization.</p>
        <h3>Active Modules:</h3>
        <ul>
            <li><strong>Physical Social Space Management:</strong> Active & Bookable</li>
            <li><strong>Academic & International Networks:</strong> Connected</li>
            <li><strong>Blockchain Tokenization Gateway:</strong> Operational (ERC-3643 Compliant)</li>
            <li><strong>Public Grant & Investor Portal:</strong> Synchronized</li>
        </ul>
        <p><em>Deploy your own municipal instance via <a href="https://github.com/arte-net-global/municipal-cultural-hub">GitHub</a>.</em></p>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HOME_TEMPLATE, municipality=app.config['MUNICIPALITY_NAME'])

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({
        "status": "online",
        "municipality": app.config['MUNICIPALITY_NAME'],
        "version": "1.0.0-open-source",
        "protocol": "ARTE-NET Decentralized Cultural Standard"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
