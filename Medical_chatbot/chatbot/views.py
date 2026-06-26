import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import google.generativeai as genai

from .services import medical_prompt

# Configure Gemini API
genai.configure(api_key="YOUR_REAL_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")


class MedicalScreeningAPIView(APIView):

    def post(self, request):

        symptoms = request.data.get("symptoms", "").strip()
        duration = request.data.get("duration", "").strip()

        if not symptoms or not duration:
            return Response(
                {"error": "Symptoms and duration are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        prompt = medical_prompt.format(
            symptoms=symptoms,
            duration=duration
        )

        try:
            response = model.generate_content(prompt)

            result_text = response.text.strip()

            try:
                result_json = json.loads(result_text)

                return Response(
                    result_json,
                    status=status.HTTP_200_OK
                )

            except json.JSONDecodeError:
                return Response(
                    {
                        "error": "Gemini returned invalid JSON",
                        "raw_response": result_text
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )