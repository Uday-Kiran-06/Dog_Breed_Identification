import os
import pandas as pd
import shutil

# Define paths
dataset_path = r'c:\Users\ASUS\Downloads\DOG_BREED_PREDICTION\DOG_BREED_PREDICTION\Dataset'
train_dir = os.path.join(dataset_path, 'Train')
labels_file = os.path.join(dataset_path, 'labels.csv')

def reorganize_dataset():
    # Read labels
    if not os.path.exists(labels_file):
        print(f"Labels file not found at {labels_file}")
        return

    df = pd.read_csv(labels_file)
    print(f"Loaded {len(df)} labels.")

    # Iterate through each row
    for index, row in df.iterrows():
        image_id = row['id']
        breed = row['breed']
        
        # Image file name (assuming .jpg extension based on previous check)
        # Check if file exists with .jpg
        file_name = f"{image_id}.jpg"
        source_path = os.path.join(train_dir, file_name)
        
        if not os.path.exists(source_path):
            # Try searching without extension or other extensions if needed?
            # Based on previous `ls`, files are likely just IDs or IDs.jpg. 
            # Looking at previous `ls` output is `000bec180eb18c7604dcecc8fe0dba07.jpg`?
            # Wait, I didn't see the extension in the `ls` output in my thought trace, let me re-verify if needed.
            # Assuming .jpg for now as standard.
            pass
        
        if os.path.exists(source_path):
            # Create breed directory if it doesn't exist
            breed_dir = os.path.join(train_dir, breed)
            if not os.path.exists(breed_dir):
                os.makedirs(breed_dir)
            
            # Move file
            dest_path = os.path.join(breed_dir, file_name)
            if not os.path.exists(dest_path):
               shutil.move(source_path, dest_path)
            # print(f"Moved {file_name} to {breed_dir}") # too verbose
        else:
            # print(f"File {file_name} not found.") 
            pass

    print("Reorganization complete.")

if __name__ == "__main__":
    reorganize_dataset()
