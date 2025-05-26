from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from request import ModelRequest
import torch.nn.functional as Fnc
class Model():
    def __new__(cls, context):
        cls.context = context
        if not hasattr(cls, 'instance'):
            cls.instance = super(Model, cls).__new__(cls)
        cls.tokenizer = AutoTokenizer.from_pretrained("VidishaKhalpada/intent-classifier")
        cls.model = AutoModelForSequenceClassification.from_pretrained("VidishaKhalpada/intent-classifier")
        cls.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        cls.model.to(cls.device)
        cls.threshold = 0.5
        return cls.instance

    async def inference(self,  request: ModelRequest):
        inputs = self.tokenizer(request.text, return_tensors="pt")
        inputs = {key: value.to(self.device) for key, value in inputs.items()}
        with torch.no_grad():
            logits = self.model(**inputs).logits
            probabilities = Fnc.softmax(logits, dim=1)
            print("All logits:", logits)
            print("Probabilities:", probabilities)
        if probabilities.max() < self.threshold:
            return 11
        else:
            return logits.argmax().item()
