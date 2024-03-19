#script to convert time to sec and classify unlabeled data by time
import pandas as pd
import os

# Define the path to the CSV file
# p1l_path = os.path.join('phyphox-ios', 'raw-data', 'p1-left-pocket', 'Raw Data.csv')
# p1r_path = os.path.join('phyphox-ios', 'raw-data', 'p1-right-pocket', 'Raw Data.csv')
# # Read the CSV file
# df1l = pd.read_csv(p1l_path)
# df1r = pd.read_csv(p1r_path)

# # Convert the "Time (s)" column to seconds
# df1l['Time (s)'] = df1l['Time (s)'].apply(lambda x: float(x) * 1000)  # Convert to milliseconds
# df1r['Time (s)'] = df1r['Time (s)'].apply(lambda x: float(x) * 1000)  # Convert to milliseconds

# # Save the modified data to a new CSV file
# output_p1l_path = os.path.join(os.path.dirname(p1l_path), 'converted_data.csv')
# df1l.to_csv(output_p1l_path, index=False)

def convert_csv(input_csv_path):
    # Read the CSV file
    df = pd.read_csv(input_csv_path)

    # Convert the "Time (s)" column to milliseconds
    df['Time (ms)'] = df['Time (s)'].apply(lambda x: float(x) * 1000)  # Convert to milliseconds
    #Delete the duplicated Time column
    df.drop(columns=['Time (s)'], inplace=True)

    # Reorder the columns with 'Time (ms)' as the first column
    df = df[['Time (ms)'] + [col for col in df.columns if col != 'Time (ms)']]
            
    # Save the modified data to a new CSV file
    output_csv_path = os.path.join(os.path.dirname(input_csv_path), 'converted_data.csv')
    df.to_csv(output_csv_path, index=False)

    print(f"Conversion completed for {input_csv_path}. Results saved to 'converted_data.csv'")

# Define the folders containing raw data for left and right pockets
# pockets_folders = ['p1-left-pocket', 'p1-right-pocket']
    
pockets_folders = []

# Generate elements for 20 participants with left and right pockets
for i in range(1, 21):
    pockets_folders.append(f'p{i}-left-pocket')
    pockets_folders.append(f'p{i}-right-pocket')

for pocket_folder in pockets_folders:
    pocket_path = os.path.join('phyphox-ios', 'raw-data', pocket_folder)
    for file in os.listdir(pocket_path):
        if file.endswith('.csv'):
            input_csv_path = os.path.join(pocket_path, file)
            output_csv_path = os.path.join(pocket_path, 'converted_data.csv')
            if not os.path.exists(output_csv_path):
                convert_csv(input_csv_path)
            else:
                print(f"Skipping {input_csv_path}. Already converted.")

