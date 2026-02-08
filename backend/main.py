from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from dataset_loader import load_recipes_from_excel
from recipe_retriever import RecipeRetriever
from llm_client import LocalLLMClient

app = FastAPI(title="IndianFoodBot API", version="3.0")

DATASET_PATH = "data/IndianFoodDatasetXLS.xlsx"

recipes_data = load_recipes_from_excel(DATASET_PATH)
retriever = RecipeRetriever(recipes_data)

# FAST MODEL FOR LOW-END LAPTOP
llm = LocalLLMClient(model_name="tinyllama")


class RecipeQuery(BaseModel):
    ingredients: List[str]


@app.get("/")
def home():
    return {"message": "Welcome to IndianFoodBot API. Go to /docs to test."}


@app.post("/chat")
def chat(query: RecipeQuery):
    best_recipe = retriever.get_best_recipe(query.ingredients)

    if not best_recipe:
        return {
            "status": "no_match",
            "message": "No recipe found for given ingredients."
        }

    prompt = f"""
You are IndianFoodBot, a friendly Indian cooking assistant.

User ingredients: {query.ingredients}

Recipe Name: {best_recipe['recipe_name']}
Cuisine: {best_recipe['cuisine']}
Course: {best_recipe['course']}
Diet: {best_recipe['diet']}
Total Time: {best_recipe['total_time_mins']} mins

Ingredients:
{best_recipe['ingredients_text']}

Instructions:
{best_recipe['instructions']}

Now respond like a chatbot:
- Give step-by-step instructions
- Keep it simple
- Keep response within 10 lines
"""

    try:
        chatbot_response = llm.generate_response(prompt)
    except Exception as e:
        chatbot_response = f"⚠️ LLM error: {str(e)}"

    return {
        "status": "success",
        "best_match": best_recipe,
        "chatbot_response": chatbot_response
    }
