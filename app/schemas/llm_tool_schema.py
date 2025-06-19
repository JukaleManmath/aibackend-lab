tools = [
    {
        "name": "summarize_text",
        "description": "Summarizes a given text into a short version using TextBlob.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The input text to summarize"
                }
            },
            "required": ["text"]
        }
    },
    {
        "name": "translate_to_french",
        "description": "Translates the given English text to French using TextBlob.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The English text to be translated into French"
                }
            },
            "required": ["text"]
        }
    },
    {
        "name": "password_strength",
        "description": "Evaluates the strength of a password as Weak, Moderate, or Strong.",
        "parameters": {
            "type": "object",
            "properties": {
                "password": {
                    "type": "string",
                    "description": "The password to evaluate"
                }
            },
            "required": ["password"]
        }
    }
]
