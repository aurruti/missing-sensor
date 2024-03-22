import pandas as pd
import os

def classify_data(input_csv_path, output_dir):

    # Read the CSV file
    df = pd.read_csv(input_csv_path)

    # Read the timestamp CSV file
    timestamp_df = pd.read_csv('./timestamps.csv')

    

    # Define time intervals for each activity
    start_standup = start_standardized_times + 60000
    start_walk = start_standup + 30000
    start_jog = start_walk + 30000
    start_rest = start_jog + 30000
    start_squat = start_rest + 30000
    start_clap = start_squat + 15000
    start_msrc12_1 = start_clap + 10000
    start_msrc12_2 = start_msrc12_1 + 15000
    start_msrc12_3 = start_msrc12_2 + 15000
    start_msrc12_4 = start_msrc12_3 + 15000
    start_msrc12_5 = start_msrc12_4 + 15000
    start_msrc12_6 = start_msrc12_5 + 15000
    start_msrc12_7 = start_msrc12_6 + 15000
    start_msrc12_8 = start_msrc12_7 + 15000
    start_msrc12_9 = start_msrc12_8 + 15000
    start_msrc12_10 = start_msrc12_9 + 15000
    start_msrc12_11 = start_msrc12_10 + 15000
    start_msrc12_12 = start_msrc12_11 + 15000

def loop_data_folders(data_folders):
    for data_folder in data_folders:
        data_path = os.path.join('phyphox-ios', 'data', data_folder)
        for file in os.listdir(data_path):
            if file == 'converted_data.csv':
                input_csv_path = os.path.join(data_path, file)
                output_csv_path = os.path.join(data_path, 'labeled_data.csv')
                if not os.path.exists(output_csv_path):
                    classify_data(input_csv_path, data_path)
                else:
                    print(f"Skipping {input_csv_path}. Already classify.")




if __name__ == "__main__":
    # Define the folders containing raw data for left and right pockets
    data_folders = []

    # Generate elements for 20 participants with left and right pockets
    for i in range(1, 21):
        data_folders.append(f'p{i}-left-pocket')
        data_folders.append(f'p{i}-right-pocket')

    # Process data folders
    loop_data_folders(data_folders)


def label_data(input_csv_path, output_dir, start_write_by_hand, start_write_on_pc, start_standardized_times):
    """
    Classify the data based on time intervals of the data collection activity.
    ATTENTION: This function WILL OVERWRITE files with the same name in the output directory.
    Input:
        input_csv_path: str, path to the input CSV file with the raw data.
        output_dir: str, path to the output directory where labeled data will be saved.
        start_write_by_hand: int, start time of the write by hand activity in milliseconds
        start_write_on_pc: int, start time of the write on PC activity in milliseconds
        start_standardized_times: int, start time of the standardized times activity in milliseconds
        
    Returns:
        None
    """
    # Read the input CSV file
    df = pd.read_csv(input_csv_path)

    # Define time intervals for each activity
    start_standup = start_standardized_times + 60000
    start_walk = start_standup + 30000
    start_jog = start_walk + 30000
    start_rest = start_jog + 30000
    start_squat = start_rest + 30000
    start_clap = start_squat + 15000
    start_msrc12_1 = start_clap + 10000
    start_msrc12_2 = start_msrc12_1 + 15000
    start_msrc12_3 = start_msrc12_2 + 15000
    start_msrc12_4 = start_msrc12_3 + 15000
    start_msrc12_5 = start_msrc12_4 + 15000
    start_msrc12_6 = start_msrc12_5 + 15000
    start_msrc12_7 = start_msrc12_6 + 15000
    start_msrc12_8 = start_msrc12_7 + 15000
    start_msrc12_9 = start_msrc12_8 + 15000
    start_msrc12_10 = start_msrc12_9 + 15000
    start_msrc12_11 = start_msrc12_10 + 15000
    start_msrc12_12 = start_msrc12_11 + 15000

    # Create a new column 'Label' and classify the data based on time intervals
    df['Label'] = pd.cut(df['Time (ms)'], bins=[-float('inf'), start_write_by_hand, start_write_on_pc, start_standardized_times,
                                            start_standup, start_walk, start_jog, start_rest, start_squat, start_clap,
                                            start_msrc12_1, start_msrc12_2, start_msrc12_3, start_msrc12_4, start_msrc12_5,
                                            start_msrc12_6, start_msrc12_7, start_msrc12_8, start_msrc12_9, start_msrc12_10,
                                            start_msrc12_11, start_msrc12_12, float('inf')],
                      labels=['write_by_hand', 'write_on_pc', 'standardized_times', 'standup', 'walk', 'jog', 'rest',
                              'squat', 'clap', 'msrc12_1', 'msrc12_2', 'msrc12_3', 'msrc12_4', 'msrc12_5', 'msrc12_6',
                              'msrc12_7', 'msrc12_8', 'msrc12_9', 'msrc12_10', 'msrc12_11', 'msrc12_12'])

    # Define the output CSV file path
    output_csv_path = os.path.join(output_dir, 'labeled_data.csv')

    # Save the labeled data to a new CSV file
    df.to_csv(output_csv_path, index=False)

    print(f"Data labeled and saved to {output_csv_path}")