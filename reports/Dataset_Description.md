# NutriVision — Dataset Description (Step 1.2)

**Author:** Ayar Mouhcine
**Project:** NutriVision — intelligent food recognition and nutritional estimation (NLP + Computer Vision)
**Scope:** Data sources, usage conditions, formats, sizes, categories, annotations, data quality, imbalance and representativeness limits.

All figures in this document come from the project notebooks:
`02_food11_data_cleaning.ipynb`, `03_usda_data_preparation.ipynb`, `04_curated_dataset_preparation.ipynb` and `05_exploratory_data_analysis.ipynb`.

---

## 1. Overview

| Source | Role in the project | Content | Size (after preparation) | Usage terms |
|---|---|---|---|---|
| Food-11 | Computer Vision: food category recognition | Food photos, 11 categories | 16,020 unique images (from 16,643) | Research purposes only (original EPFL terms) |
| USDA FoodData Central, Foundation Foods | Nutritional reference | Energy, protein, fat, carbohydrates per food | 424 food records | Public domain, CC0 1.0 |
| Curated dish dataset | Link between dishes, ingredients and USDA values; future text modality | Dishes, ingredient quantities, USDA references | 10 dishes, 9 ingredients, 35 annotations | Created by the project team |

**Important gap:** Food-11 has images but no text or ingredients. The curated dataset has ingredients but no images or text. No image–text pairs exist yet (see section 5).

---

## 2. Food-11

### 2.1 Source and usage conditions

- **Original authors and host:** Singla, Yuan and Ebrahimi (2016), EPFL Multimedia Signal Processing Group, "Food/Non-food Image Classification and Food Categorization using Pre-Trained GoogLeNet Model". Dataset page: https://www.epfl.ch/labs/mmspg/downloads/food-image-datasets/
- **Terms stated by EPFL:** free use, copying, modification and distribution of the data for **research purposes only**, provided "as is" with no warranty and no maintenance or support obligation.
- **Copy used in this project:** the Kaggle mirror https://www.kaggle.com/datasets/trolukovich/food11-image-dataset, downloaded as `archive.zip` (1,163,229,310 bytes, about 1.16 GB, which matches the size EPFL lists for Food-11).
  - The label shown on a mirror may differ from the original authors' terms. The stricter original condition (research only) is applied to this project.
- **Image provenance:** according to the authors' presentation, the images were collected from social media (for example Instagram and Flickr) and from the Food-101 dataset. Rights to individual photos belong to their original owners.
- **Our use and redistribution:** academic coursework (Master's project), which falls under "research purposes". The raw images are **not redistributed**: the Git repository excludes `data/raw/` and `data/processed/`, and contains only code, notebooks, reports and three small summary figures.

### 2.2 Format and size

- 11 categories: Bread, Dairy product, Dessert, Egg, Fried food, Meat, Noodles-Pasta, Rice, Seafood, Soup, Vegetable-Fruit.
- Original splits (training / validation / evaluation): **9,866 / 3,430 / 3,347** images, **16,643** in total.
- Kaggle layout: `training/`, `validation/`, `evaluation/`, each with one folder per category. (The EPFL page describes a `{ClassID}_{ImageID}.jpg` naming convention; the Kaggle copy is organised by category folder instead.)
- Integrity check with Pillow: all 16,643 images opened without error. All are **JPEG** in **RGB** mode.
- Image properties below are computed on the deduplicated set of 16,020 images:

| Property | Min | Median | Mean | Max |
|---|---|---|---|---|
| Width (px) | 220 | 512 | 532.1 | 9,542 |
| Height (px) | 207 | 512 | 496.3 | 6,144 |
| Aspect ratio (width / height) | 0.56 | 1.00 | 1.09 | 2.61 |
| File size (KB) | 6.2 | 48.3 | 70.1 | 9,874.5 |

- There are **825 distinct image sizes**. 512×512 is the most common (9,283 images, 57.9%); the 8 most common sizes together cover 13,576 images (84.7%).
- Size outliers are rare: 907 images are wider than 512 px (5.7%), 721 are taller than 512 px (4.5%), 197 have a side above 1,024 px (1.2%) and 171 files exceed 500 KB (1.1%). Only 2 images have a side below 224 px.
- A fixed-size resize is therefore sufficient for model input; no outlier removal is planned.

### 2.3 Categories and annotations

- Labels are **dish-level categories** only. There are no ingredient labels, bounding boxes or text descriptions.
- The labels were provided by the dataset authors. The annotation procedure is not documented in the sources consulted. No manual annotation of Food-11 was performed by this project.
- Categories are broad: each one groups several kinds of dishes (for example Soup ranges from a latte-art-style bowl to a red stew), as the sample grid in notebook 05 shows.

### 2.4 Duplicates, errors and missing data

- **Missing or corrupt files:** none. All 16,643 images are valid.
- **Duplicates:** exact duplicates were detected with SHA-256 hashes: **622 duplicate groups** containing **1,245 images**. Duplicates also appeared **across the original splits**, which would cause data leakage between training and evaluation.
- **Treatment:** global deduplication keeping one image per group removed 623 images, leaving **16,020 unique images**. The 11 categories all remain, and no hash appears in more than one new split.
- **Possible remaining errors:** label noise and off-topic photos cannot be excluded. The sample grid shows examples of weak images (a market stall labelled Vegetable-Fruit, a butter tub in Dairy product, a very dark Dessert photo). These were not removed. Near-duplicates (resized or re-compressed copies) are not detected by exact hashing.

### 2.5 New splits

New stratified splits were created after deduplication (about 60% / 20% / 20%):

| Split | Images |
|---|---|
| Training | 9,612 |
| Validation | 3,204 |
| Evaluation | 3,204 |
| **Total** | **16,020** |

The cleaned dataset is stored as a CSV manifest, not as copies of the images. The manifest keeps the original split in `split`, the new one in `new_split`, and records path, size, hash and other properties for each image. The new split assignment (`new_split`) must be used for all later work.

- `data/processed/food11/food11_clean_manifest.csv` (16,020 rows, 13 columns)
- `data/processed/food11/food11_split_summary.csv`

### 2.6 Class imbalance and representativeness

| Category | Training | Validation | Evaluation | Total |
|---|---|---|---|---|
| Dessert | 1,435 | 478 | 478 | 2,391 |
| Soup | 1,430 | 477 | 477 | 2,384 |
| Meat | 1,258 | 419 | 420 | 2,097 |
| Egg | 986 | 329 | 328 | 1,643 |
| Bread | 974 | 325 | 325 | 1,624 |
| Seafood | 843 | 281 | 281 | 1,405 |
| Fried food | 837 | 279 | 279 | 1,395 |
| Vegetable-Fruit | 696 | 232 | 232 | 1,160 |
| Noodles-Pasta | 440 | 146 | 147 | 733 |
| Dairy product | 430 | 144 | 143 | 717 |
| Rice | 283 | 94 | 94 | 471 |

- **Imbalance:** Dessert (2,391) to Rice (471) is about **5:1**. Evaluation should report macro-averaged metrics (for example macro-F1) as well as accuracy, and class weighting should be considered.
- **Stratification:** every category has 60% of its images in training (Rice 60.1% from rounding).
- **Representativeness limits:** the images come from social media and existing datasets, so they reflect what people choose to photograph and post. Categories are coarse, and the dataset has no information about cuisine, portion size or ingredients. Results on Food-11 should not be assumed to hold for other cuisines or for real-world portions without further testing.

---

## 3. USDA FoodData Central — Foundation Foods

### 3.1 Source and usage conditions

- **Publisher:** U.S. Department of Agriculture, Agricultural Research Service, FoodData Central: https://fdc.nal.usda.gov/
- **Terms:** FoodData Central data are in the public domain and published under **CC0 1.0 Universal**.
- **File used:** `data/raw/usda_foundation/FoodData_Central_foundation_food_json_2026-10-29.json` (Foundation Foods, October 2026 release as named in the downloaded file)
- **Date downloaded:** 15 November 2026
- **Suggested citation:** U.S. Department of Agriculture, Agricultural Research Service. FoodData Central. fdc.nal.usda.gov. Accessed 15 November 2026.

### 3.2 Format and content

- JSON, with **424 food records**. Foundation Foods provides expanded nutrient and food-component data for basic foods and ingredients, not for prepared dishes.
- Fields extracted into `data/processed/usda_foundation_nutrition.csv` (424 rows, 8 columns): `fdc_id`, `food_name`, `calories_kcal`, `protein_g`, `fat_g`, `carbohydrates_g`, `energy_nutrient_id`, `energy_method`.
- **Energy rule:** energy is taken from nutrient ID 1008 (standard Energy) when present, otherwise 2048 (Atwater Specific Factors), otherwise 2047 (Atwater General Factors). The method used for each food is stored in `energy_method`, because the sources are not strictly identical.

### 3.3 Missing values, duplicates and errors

| Column | Missing values (of 424) | Share |
|---|---|---|
| `calories_kcal` | 50 | 11.8% |
| `protein_g` | 17 | 4.0% |
| `fat_g` | 31 | 7.3% |
| `carbohydrates_g` | 60 | 14.2% |

- **Negative carbohydrate values:** 10 were found and replaced with missing values (not zero), since a negative amount is not physically valid and zero would invent data. No negative carbohydrate values remain.
- Missing values were **preserved**, not imputed.
- Duplicate FDC IDs were checked in notebook 03.
- **Limits:** 424 foods is a small catalogue, so not every ingredient of a real meal can be matched. Values are laboratory or derived reference values for the food as listed, and they do not describe cooked, seasoned or mixed dishes.

---

## 4. Curated dish dataset

### 4.1 Collection and annotation procedure

The dataset was created **manually by the project team** to connect dishes, ingredients, ingredient quantities and USDA references. It is an initial dataset intended to be expanded. Ingredient quantities were proposed manually. They were not taken from standardised recipes and were not independently validated.

### 4.2 Content and files (`data/processed/curated/`)

| File | Content | Rows |
|---|---|---|
| `dishes.csv` | `dish_id`, `dish_name`, `category` | 10 |
| `ingredients.csv` | `dish_id`, `ingredient_id`, `quantity_g` (dish–ingredient annotations) | 35 |
| `ingredient_reference.csv` | `ingredient_id`, `usda_fdc_id`, `usda_food_name` | 9 |
| `dish_nutrition.csv` | Calculated total weight, calories, protein, fat, carbohydrates per dish | 10 |
| `dish_food11_mapping.csv` | Category-level link from each dish to a Food-11 class | 10 |

- **Ingredients (9):** tomatoes, eggs, onions, potatoes, rice, ground beef, chicken breast, salmon, spaghetti. Each is linked to a USDA FDC ID.
- **Dishes (10):** Chicken with Rice, Beef with Rice, Salmon with Rice, Vegetable Omelette, Chicken Pasta, Spaghetti with Ground Beef, Baked Potato with Chicken, Tomato and Egg Dish, Chicken and Vegetable Bowl, Beef and Potato Bowl.
- **Dish categories:** Rice-based (3 dishes), Egg-based (2), Pasta (2), Potato-based (1), Mixed (2).

### 4.3 Validation performed

10 unique dishes; 35 annotations; no invalid dish or ingredient IDs; no missing or non-positive quantities; no duplicate dish–ingredient pairs; no missing calculated nutritional values; no negative nutritional values.

### 4.4 Limitations

- Quantities are manually proposed estimates, not validated standard recipes.
- Weights refer to **raw or dry** ingredients.
- Calculated nutrition is an **estimate**, not a laboratory-measured value for the cooked meal.
- Cooking-related changes, oil, salt and spices are **not** included.
- Only 10 dishes and 9 ingredients: the dataset is far too small for training and serves as a prototype and evaluation reference.

---

## 5. Linking images and text (current state)

- Food-11 has images and category labels but **no text**. The curated dataset has dishes and ingredients but **no images and no text descriptions**.
- A coarse category-level link is stored in `dish_food11_mapping.csv`. **7 of 10 dishes** map to a Food-11 class:

| Curated category | Dishes | Food-11 class | Food-11 images |
|---|---|---|---|
| Rice-based | 3 | Rice | 471 |
| Egg-based | 2 | Egg | 1,643 |
| Pasta | 2 | Noodles-Pasta | 733 |
| Potato-based | 1 | none | — |
| Mixed | 2 | none | — |

- This mapping is a **heuristic**. It states that two items are the same kind of dish, not that a particular image shows a particular dish. For example, a Food-11 Rice image may show plain fried rice, not Chicken with Rice.
- **Consequence:** no verified image–text pairs exist at this stage, so the multimodal research question cannot yet be tested. Paired image–text data (for example short text descriptions written for a manually selected sample of Food-11 images) must be constructed in a later stage.

---

## 6. Summary of known limitations

1. Food-11 labels are dish-level; there are no ingredient labels.
2. Class imbalance of about 5:1 (Dessert vs Rice).
3. Possible label noise and near-duplicates that exact hashing cannot detect.
4. Images come from social media, so they are not guaranteed to represent real-world meals or cuisines.
5. USDA Foundation Foods has only 424 foods, with missing values (up to 14.2% for carbohydrates).
6. The curated dataset is small and its quantities are unvalidated estimates for raw ingredients.
7. No image–text pairs exist yet.

---

## 7. References for this document

1. Singla, A., Yuan, L., Ebrahimi, T. (2016). Food/Non-food Image Classification and Food Categorization using Pre-Trained GoogLeNet Model. EPFL Multimedia Signal Processing Group. Dataset page: https://www.epfl.ch/labs/mmspg/downloads/food-image-datasets/
2. Food-11 image dataset (Kaggle mirror). https://www.kaggle.com/datasets/trolukovich/food11-image-dataset
3. U.S. Department of Agriculture, Agricultural Research Service. FoodData Central. https://fdc.nal.usda.gov/ (Foundation Foods documentation: https://fdc.nal.usda.gov/Foundation_Foods_Documentation.html)
