import os

# Path to the dataset (we'll set this after unzipping)
dataset_path = "plantvillage dataset/color"

# List all disease classes
classes = os.listdir(dataset_path)
print(f"✅ Total disease classes found: {len(classes)}")
print("\n📋 All classes:")
for i, c in enumerate(classes):
    count = len(os.listdir(os.path.join(dataset_path, c)))
    print(f"  {i+1}. {c} — {count} images")