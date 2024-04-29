from model import Model
from request import ModelRequest
from quart import Quart, request
import aiohttp
from flair.models import TextClassifier
from flair.data import Sentence

app = Quart(__name__)

model = None
classifier = TextClassifier.load('en-sentiment')

@app.before_serving
async def startup():
    app.client = aiohttp.ClientSession()
    global model
    model = Model(app)

def score_to_category(score):
    if score > 0.33:
        return "Positive"
    elif score < -0.33:
        return "Negative"
    else:
        return "Neutral"

@app.route('/classify', methods=['POST'])

async def embed():
    global model
    data = await request.get_json()
    req = ModelRequest(**data)
    label = await model.inference(req)

    category_map = {
        0: {"cat_id": 450, "category": "DEPOSIT", "type": "SB/CA/TERM DEPOSIT ACCOUNTS", "subtype": "Dispute in charges deducted", "error": None},
        1: {"cat_id": 464, "category": "DEPOSIT", "type": "SB/ CA/TERM DEPOSIT ACCOUNTS", "subtype": "Minimum Balance Charges related", "error": None},
        2: {"cat_id": 764, "category": "DIGITAL BANKING", "type": "ATM RELATED", "subtype": "Dispute in ATM AMC Charges", "error": None},
        3: {"cat_id": 518, "category": "DIGITAL BANKING", "type": "FUND REMITTANCE: NEFT/ RTGS/ IMPS through Branch", "subtype": "Dispute in charges deducted", "error": None},
        4: {"cat_id": 621, "category": "LOANS & ADVANCES", "type": "Education Loans", "subtype": "Discrepancy in Char (Processing Fee/Documentation charges", "error": None},
        5: {"cat_id": 631, "category": "LOANS & ADVANCES", "type": "Govt Scheme loans", "subtype": "Discrepancy in Charges (Processing Fee/Documentation charges", "error": None},
        6: {"cat_id": 641, "category": "LOANS & ADVANCES", "type": "Home loans", "subtype": "Discrepancy in Charges (Processing Fee/Documentation charges", "error": None},
        7: {"cat_id": 654, "category": "LOANS & ADVANCES", "type": "OTHER ADVANCES", "subtype": "Discrepancy in Charges (Processing Fee/Documentation charges", "error": None},
        8: {"cat_id": 664, "category": "LOANS & ADVANCES", "type": "Personal loans", "subtype": "Discrepancy in Charges (Processing Fee/Documentation charges", "error": None},
        9: {"cat_id": 675, "category": "LOANS & ADVANCES", "type": "SME ADVANCES", "subtype": "Discrepancy in Charges (Processing Fee/Documentation charges", "error": None},
        10: {"cat_id": 685, "category": "LOANS & ADVANCES", "type": "VEHICLE LOANS", "subtype": "Discrepancy in Charges (Processing Fee/Documentation charges", "error": None},
        11: {"error": "Out of Scope"}
    }

    text = data['text']
    sentence = Sentence(text)
    classifier.predict(sentence)
    sentiment_label = sentence.labels[0].value
    sentiment_score = sentence.labels[0].score

    category_response = category_map[label]
    category_response['sentiment_label'] = sentiment_label
    category_response['sentiment_score'] = sentiment_score
    category_response['sentiment_category'] = score_to_category(sentiment_score)

    return category_response


if __name__ == "__main__":
    app.run()
