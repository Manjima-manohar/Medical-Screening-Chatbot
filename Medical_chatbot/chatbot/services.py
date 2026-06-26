from langchain_core.prompts import PromptTemplate

medical_prompt = PromptTemplate.from_template(
    """
You are an AI medical screening assistant.

Analyze the symptoms and duration provided below.

Symptoms: {symptoms}
Duration: {duration}

Provide:
1. Possible medical conditions ranked by likelihood.
2. Severity assessment.
3. Common causes.
4. Emergency warning signs.
5. Recommended action.

Return ONLY valid JSON in the following format:

{{
  "possible_conditions": [
    {{
      "condition": "",
      "likelihood": ""
    }}
  ],
  "severity_assessment": "",
  "common_causes": [],
  "warning_signs": [],
  "recommended_action": "",
  "disclaimer": "This information is provided for educational purposes only and is not a medical diagnosis."
}}

Do not repeat the input.
Do not return markdown.
Do not return code blocks.
Do not include any text outside the JSON.
Your response must start with {{ and end with }}.
"""
)