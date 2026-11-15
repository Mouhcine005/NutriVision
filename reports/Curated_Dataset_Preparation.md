# Curated Dataset — Preparation and Documentation

## 1. Overview

The curated dataset was created as part of the NutriVision project to connect food dishes with structured ingredient annotations and nutritional information.

Food-11 provides food-category labels but does not contain ingredient-level annotations or nutritional composition. The curated dataset addresses this limitation by associating each dish with a list of ingredients, their quantities, corresponding USDA FoodData Central identifiers, and estimated nutritional values.

The initial version contains 10 manually defined dishes and serves as a foundation for future dataset expansion.

## 2. Dataset Structure

The curated dataset is stored in:

`data/processed/curated/`

It consists of four CSV files.

| File | Description |
|---|---|
| `ingredient_reference.csv` | Ingredient identifiers linked to USDA FDC records |
| `dishes.csv` | Dish identifiers, names, and categories |
| `ingredients.csv` | Dish-to-ingredient relationships and ingredient quantities |
| `dish_nutrition.csv` | Aggregated nutritional estimates for each dish |

### 2.1 Ingredient Reference

Each ingredient has a unique internal identifier (`ingredient_id`) and a corresponding USDA FoodData Central identifier (`usda_fdc_id`).

The initial reference table contains 9 ingredients:

1. Tomatoes, grape, raw
2. Eggs, Grade A, large, whole
3. Onions, yellow, raw
4. Potatoes, russet, without skin, raw
5. Rice, white, long grain, unenriched, raw
6. Ground beef, 90% lean / 10% fat, raw
7. Chicken breast, boneless, skinless, raw
8. Salmon, Atlantic, farm raised, raw
9. Spaghetti, dry, enriched

The USDA FDC identifiers were selected from the downloaded USDA Foundation Foods dataset and linked to the corresponding nutritional records.

### 2.2 Dish Table

The initial dataset contains 10 dishes:

| Dish ID | Dish Name | Category |
|---|---|---|
| DISH001 | Chicken with Rice | Rice-based |
| DISH002 | Beef with Rice | Rice-based |
| DISH003 | Salmon with Rice | Rice-based |
| DISH004 | Vegetable Omelette | Egg-based |
| DISH005 | Chicken Pasta | Pasta |
| DISH006 | Spaghetti with Ground Beef | Pasta |
| DISH007 | Baked Potato with Chicken | Potato-based |
| DISH008 | Tomato and Egg Dish | Egg-based |
| DISH009 | Chicken and Vegetable Bowl | Mixed |
| DISH010 | Beef and Potato Bowl | Mixed |

### 2.3 Ingredient Annotations

The `ingredients.csv` file contains 35 ingredient annotations across the 10 dishes.

Each record includes:

- `dish_id`: Identifier of the associated dish.
- `ingredient_id`: Identifier of the ingredient.
- `quantity_g`: Ingredient quantity expressed in grams.

The quantities represent proposed recipe annotations rather than experimentally measured or independently verified recipe quantities.

The following conventions were used:

- Meat and fish quantities represent raw weights.
- Rice and pasta quantities represent dry weights.
- Vegetables represent raw weights.
- Egg quantities represent raw whole-egg weight.

Only ingredients available in the initial USDA reference table were included.

## 3. USDA Nutritional Reference

The nutritional information was obtained from the USDA FoodData Central Foundation Foods dataset.

The selected USDA records provide the following nutritional variables:

- Calories (`calories_kcal`)
- Protein (`protein_g`)
- Fat (`fat_g`)
- Carbohydrates (`carbohydrates_g`)

The selected ingredient references were checked for missing nutritional values. All 9 records contained values for the four selected nutritional variables.

The original USDA energy method was retained in the reference dataset through the `energy_method` field.

Different energy calculation methods may be present, including standard Energy and Atwater General or Specific Factors. The selected calorie value follows the energy-selection priority established during USDA data preparation.

Missing nutrient values were not replaced with zero.

## 4. Nutritional Calculation Methodology

Nutritional contributions were calculated using the ingredient quantities and the corresponding USDA nutritional reference values.

For each ingredient:

**Nutrient contribution = (Ingredient quantity in grams / 100) × USDA nutrient value per 100 g**

For example, 150 g of raw chicken breast with a reference value of 112 kcal per 100 g contributes:

(150 / 100) × 112 = 168 kcal

The same calculation was applied to protein, fat, and carbohydrates.

The nutritional contributions were then aggregated by dish by summing the contributions of all its ingredients.

The resulting `dish_nutrition.csv` contains:

- `dish_id`
- `dish_name`
- `category`
- `total_ingredient_weight_g`
- `calories_kcal`
- `protein_g`
- `fat_g`
- `carbohydrates_g`

These values represent estimates based on the listed ingredient quantities and their USDA reference values.

They should not be interpreted as experimentally measured nutritional values of cooked meals.

## 5. Validation Results

Several validation checks were performed during dataset construction.

### Ingredient Reference Validation

- 9 ingredient references created.
- All 9 USDA FDC identifiers matched available records.
- No missing values among the four selected nutritional variables.

### Dish and Ingredient Annotation Validation

- 10 unique dishes.
- 35 ingredient annotations.
- 9 unique ingredients.
- No invalid dish identifiers.
- No invalid ingredient identifiers.
- No missing or non-positive ingredient quantities.
- No duplicate dish-ingredient combinations.

### Nutritional Calculation Validation

- 35 ingredient-level nutritional calculations completed.
- No missing calculated nutritional values.
- 10 dish-level nutritional estimates generated.
- No missing dish-level nutritional values.
- No negative nutritional values.
- No invalid total ingredient weights.

All implemented validation checks passed.

## 6. Known Limitations

The initial curated dataset has several limitations that must be considered in future development.

### Limited Dataset Size

The current version contains only 10 dishes and 9 ingredients. It is a preliminary dataset intended to validate the structure and processing methodology.

A larger and more diverse collection of dishes and ingredients will be necessary for meaningful experimentation.

### Proposed Recipe Quantities

The ingredient quantities were manually defined as initial recipe examples. They have not yet been independently verified against standardized recipes or measured food preparations.

Future versions should incorporate documented recipe sources and more reliable ingredient quantities.

### Limited Ingredient Coverage

The current reference table does not cover all ingredients commonly used in meals. Cooking oil, salt, spices, and additional vegetables are not yet represented.

These ingredients should be added through appropriate USDA references rather than assigned estimated nutritional values without documentation.

### Raw and Dry Ingredient Assumptions

The nutritional calculations use raw or dry USDA reference records. Ingredient quantities must therefore follow the corresponding raw or dry measurement state.

Cooking-related changes, such as water absorption, water loss, oil absorption, and nutrient retention, are not modeled.

### Estimated Nutritional Composition

Dish-level nutritional values are calculated by summing the nutritional contributions of their ingredients.

They do not represent laboratory measurements of prepared dishes and may differ from the actual nutritional composition of cooked meals.

## 7. Future Improvements

Future development should focus on:

1. Expanding the dataset from 10 dishes to approximately 30–50 or more.
2. Adding more ingredients and matching them to suitable USDA Foundation Foods records.
3. Incorporating documented recipe sources and more reliable ingredient quantities.
4. Recording ingredient preparation states and relevant cooking assumptions.
5. Including additional food categories to improve dataset diversity.
6. Maintaining traceability between dishes, ingredients, USDA references, and calculated nutritional values.

## 8. Conclusion

The first version of the NutriVision curated dataset has been successfully structured, linked to USDA Foundation Foods nutritional references, and validated.

It establishes a reproducible initial workflow for connecting food dishes with ingredient-level annotations and estimated nutritional composition.

The dataset will serve as a foundation for future development of the NutriVision multimodal food recognition and nutritional estimation system.