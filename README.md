
## Bank Complaint Intent Classification API

This repository provides a Python API that classifies bank complaint text into predefined categories and subcategories, leveraging the power of a pre-trained machine learning model.

**Requirements:**

-   Python 3.9 or later
-   Docker (for containerized deployment)
-   Docker Compose (optional, but recommended for multi-container management)

**Dependencies:**

-   torch: The core PyTorch library for deep learning.
-   transformers: Provides pre-trained models for various NLP tasks, including text classification.
-   quart: A lightweight, asynchronous web framework for building REST APIs in Python.
-   aiohttp: An asynchronous HTTP client/server library for inter-process communication.

**Installation:**

1.  Clone the Repository:

```
	git clone https://github.com/your-username/intent-classifier.git
```

2.  Install Dependencies:
```
	pip install -r requirements.txt
```

**Running the API:**

**1. Using Docker (Recommended):**

a. Build the Docker Image:
```
	docker build -t intent-classifier .
```

b. Run the Container:

This command starts the API service in the background, mapping the container's port 8000 to the host machine's port 8000:
```
	docker-compose up -d
```

**2. Running Without Docker:**
```
	python api.py
```
- **Using the API:**
	curl request 
```
curl --location 'http://0.0.0.0:9001/classify' \
--header 'Content-Type: application/json' \
--data '{
    "text": "bank excess charges occured"
}'
```
	The API expects a POST request to the `/classify` endpoint with the following JSON data containing the complaint text:
```

	{
	  "text": "This is a complaint about late fees."
	}
```
The API will respond with JSON indicating the predicted category and subcategory of the complaint:
```
	{
	  "category": "DEPOSIT",
	  "type": "SB/CA/TERM DEPOSIT ACCOUNTS",
	  "subtype": "Dispute in charges deducted",
	  "error": None
	}
```

Testing GHA

- **Using cURL**
```
	curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"text": "I'm having trouble transferring money to another bank."}'

```
