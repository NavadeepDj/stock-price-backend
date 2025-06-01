from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/get-price', methods=['GET'])
def get_price():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Missing symbol'}), 400

    try:
        ticker = yf.Ticker(symbol)
        current_price = ticker.info.get('currentPrice') or ticker.info.get('regularMarketPrice')
        
        if current_price:
            return jsonify({
                'symbol': symbol,
                'price': current_price
            })
        else:
            return jsonify({'error': 'Price not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
