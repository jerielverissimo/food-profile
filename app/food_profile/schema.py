from marshmallow import Schema, fields

class FoodProfileSchema(Schema):
    profile_id = fields.Str(required=True)
    category = fields.Str(required=True)
    foods_to_exclude = fields.List(fields.Str, required=True)
    ingredients_on_labeling = fields.List(fields.Str)
    recipes = fields.List(fields.Str, required=True)
    processed_foods = fields.List(fields.Str, required=True)

