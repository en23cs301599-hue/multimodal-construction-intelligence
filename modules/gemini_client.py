import json
from google import genai
from PIL import Image


def analyze_ppe(image: Image.Image, api_key: str):
    """
    Analyze a construction-site image for visible PPE
    and safety hazards.
    """

    client = genai.Client(api_key=api_key)

    prompt = """
You are an AI-assisted construction site safety screening system.

Analyze the uploaded construction-site image.

Check visible workers for:
1. Safety helmet
2. High-visibility vest
3. Safety footwear
4. Safety harness, when elevated work makes it relevant

Also identify visible construction-site hazards.

IMPORTANT:
- Only report things that can reasonably be observed.
- If something cannot be determined, say "Not Clearly Visible".
- Do not claim that the image proves legal compliance.
- This is an AI screening tool, not a professional safety certification.

Return ONLY valid JSON in this exact structure:

{
    "safety_score": 0,
    "overall_status": "Safe",
    "ppe_detection": {
        "helmet": {
            "status": "Detected",
            "compliance": true
        },
        "high_visibility_vest": {
            "status": "Detected",
            "compliance": true
        },
        "safety_footwear": {
            "status": "Not Clearly Visible",
            "compliance": false
        },
        "safety_harness": {
            "status": "Not Applicable",
            "compliance": true
        }
    },
    "hazards": [
        {
            "hazard": "Example hazard",
            "severity": "Low",
            "remedy": "Recommended corrective action"
        }
    ]
}

Allowed overall_status:
Safe, Needs Improvement, Unsafe

Allowed severity:
Low, Medium, High, Critical

safety_score must be an integer from 0 to 100.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt, image]
        )

        text = response.text.strip()

        # Remove Markdown JSON fences if Gemini adds them
        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        return json.loads(text)

    except Exception as e:

        return {
            "error": str(e)
        }
