from typing import List, Dict
from rapidfuzz import fuzz
from utils import extract_keywords


class RecipeRetriever:
    def __init__(self, recipes: List[Dict]):
        self.recipes = recipes

    def score_recipe(self, user_keywords: list, recipe_keywords: list) -> float:
        if not recipe_keywords:
            return 0

        match_score = 0

        for u in user_keywords:
            best = 0
            for r in recipe_keywords:
                score = fuzz.partial_ratio(u, r)
                if score > best:
                    best = score

            if best >= 80:
                match_score += 1

        return (match_score / len(recipe_keywords)) * 100

    def get_best_recipe(self, user_ingredients: List[str]) -> Dict | None:
        user_text = ",".join(user_ingredients)
        user_keywords = extract_keywords(user_text)

        best_recipe = None
        best_score = 0

        for recipe in self.recipes:
            recipe_keywords = recipe["ingredients_keywords"]
            score = self.score_recipe(user_keywords, recipe_keywords)

            if score > best_score:
                best_score = score
                best_recipe = recipe

        if best_recipe and best_score > 0:
            return {
                "srno": best_recipe["srno"],
                "recipe_name": best_recipe["recipe_name"],
                "cuisine": best_recipe["cuisine"],
                "course": best_recipe["course"],
                "diet": best_recipe["diet"],
                "prep_time_mins": best_recipe["prep_time"],
                "cook_time_mins": best_recipe["cook_time"],
                "total_time_mins": best_recipe["total_time"],
                "servings": best_recipe["servings"],
                "url": best_recipe["url"],
                "ingredients_text": best_recipe["ingredients_text"],
                "instructions": best_recipe["instructions"],
                "similarity_score": round(best_score, 2)
            }

        return None
