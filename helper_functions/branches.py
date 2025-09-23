import pandas as pd

def branch_normalize(df):
    """Normalize branch names"""
    mapping = {
        # ✅ Nairobi CBD - Fixed all variations
        "naivas nairobi cbd": "Naivas Nairobi CBD",
        "nairobi cbd": "Naivas Nairobi CBD",
        "cbd": "Naivas Nairobi CBD",
        "naivas cbd": "Naivas Nairobi CBD",
        "nairob cbd": "Naivas Nairobi CBD",
        "naivas nairobi central": "Naivas Nairobi CBD",  # Fixed: lowercase version

        # ✅ Kisumu
        "naivas kisumu": "Naivas Kisumu",
        "kisumu": "Naivas Kisumu",
        "naivas kisum": "Naivas Kisumu",
        "ksm": "Naivas Kisumu",
        "naivas-kisumu": "Naivas Kisumu",

        # ✅ Westlands
        "naivas westlands": "Naivas Westlands",
        "westlands": "Naivas Westlands",

        # ✅ Thika Road
        "naivas thika road": "Naivas Thika Road",
        "thika road": "Naivas Thika Road",
        "thika": "Naivas Thika Road",

        # ✅ Eldoret
        "naivas eldoret": "Naivas Eldoret",
        "eldoret": "Naivas Eldoret",

        # ✅ Nakuru
        "naivas nakuru": "Naivas Nakuru",
        "nakuru": "Naivas Nakuru",

        # ✅ Mombasa
        "naivas mombasa": "Naivas Mombasa",
        "mombasa": "Naivas Mombasa",

        # ✅ Machakos
        "naivas machakos": "Naivas Machakos",
        "machakos": "Naivas Machakos",

        # ✅ Kitale
        "naivas kitale": "Naivas Kitale",
        "kitale": "Naivas Kitale",

        # ✅ Nyeri
        "naivas nyeri": "Naivas Nyeri",
        "nyeri": "Naivas Nyeri"
    }

    # Clean and normalize
    branch_clean = df["branch"].str.strip().str.lower()
    branch_normalized = branch_clean.replace(mapping)

    # Debug: Show any unmapped values
    unmapped_mask = branch_clean == branch_normalized
    if unmapped_mask.any():
        print("⚠️  Unmapped branch values found:")
        print(df[unmapped_mask][["branch"]].drop_duplicates())
    else:
        print("✅ All branch values successfully mapped!")

    # Replace original branch column with normalized values
    df["branch"] = branch_normalized

    return df