"""Converts the time column in the CSV file to milliseconds and classify the unlabeled data - supervised training"""
import pandas as pd
import os

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

def process_data_folders(data_folders):
    for data_folder in data_folders:
        data_path = os.path.join('phyphox-ios', 'data', data_folder)
        for file in os.listdir(data_path):
            if file.endswith('.csv'):
                input_csv_path = os.path.join(data_path, file)
                output_csv_path = os.path.join(data_path, 'converted_data.csv')
                if not os.path.exists(output_csv_path):
                    convert_csv(input_csv_path)
                else:
                    print(f"Skipping {input_csv_path}. Already converted.")


if __name__ == "__main__":
    # Define the folders containing raw data for left and right pockets
    data_folders = []

    # Generate elements for 20 participants with left and right pockets
    for i in range(1, 21):
        data_folders.append(f'p{i}-left-pocket')
        data_folders.append(f'p{i}-right-pocket')

    # Process data folders
    process_data_folders(data_folders)




    

    