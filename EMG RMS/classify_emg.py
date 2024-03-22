import os
import pandas as pd
import time

def save_to_csv_by_time_interval(df, start_time, end_time, output_file, time_column = 'X[s]'):
    """""
    Export a time interval of a given dataframe to a CSV file.
    Input:
        df: pd.DataFrame, dataframe
        start_time: int, start time with the same time unit the dataframe has
        end_time: int, end time with the same time unit the dataframe has
        output_file: str, name of the output file
        time_column: str, name of the time column (by default X[s])
    Returns:
        None
    """""
    df_time_interval = df[(df[time_column] >= start_time) & (df[time_column] <= end_time)]
    df_time_interval.to_csv(output_file, index=False)
    return None

def emg_test_classification(input_path, output_dir, start_write_by_hand, start_write_on_pc, start_standardized_times):
    """""
    Classify the EMG test based on the time intervals of the data collection activity.
    ATTENTION: This function WILL OVERWRITE files with the same name in the output directory.
    Input:
        input_path: str, path to the .xlsx file with the raw data.
        output_dir: str, path to the output directory
        start_write_by_hand: int, start time of the write by hand activity in seconds
        start_write_on_pc: int, start time of the write on PC activity in seconds
        start_standardized_times: int, start time of the standardized times activity in seconds
    Returns:
        None
    """""
    if not os.path.exists(input_path):
        raise Exception(f'The input file {input_path} does not exist. Please check the path and try again.')
    if not os.path.exists(participant_output_dir):
        raise Exception(f'The output directory {participant_output_dir} does not exist. Please create it before running the function.')
    df = pd.read_excel(input_path)


    # Time definitions
    start_standup = start_standardized_times + 60
    start_walk = start_standup + 30
    start_jog = start_walk + 30
    start_rest = start_jog + 30
    start_squat  = start_rest + 30
    start_clap  = start_squat + 15
    start_msrc12_1 = start_clap + 10
    start_msrc12_2 = start_msrc12_1 + 15
    start_msrc12_3 = start_msrc12_2 + 15
    start_msrc12_4 = start_msrc12_3 + 15
    start_msrc12_5 = start_msrc12_4 + 15
    start_msrc12_6 = start_msrc12_5 + 15
    start_msrc12_7 = start_msrc12_6 + 15
    start_msrc12_8 = start_msrc12_7 + 15
    start_msrc12_9 = start_msrc12_8 + 15
    start_msrc12_10 = start_msrc12_9 + 15
    start_msrc12_11 = start_msrc12_10 + 15
    start_msrc12_12 = start_msrc12_11 + 15

    save_to_csv_by_time_interval(df, start_write_by_hand, start_write_on_pc, output_dir + '/write_by_hand.csv')
    save_to_csv_by_time_interval(df, start_write_on_pc, start_standardized_times, output_dir + '/write_on_pc.csv')
    save_to_csv_by_time_interval(df, start_standardized_times, start_standup, output_dir + '/scroll.csv')
    save_to_csv_by_time_interval(df, start_standup, start_walk, output_dir + '/standup.csv')
    save_to_csv_by_time_interval(df, start_walk, start_jog, output_dir + '/walk.csv')
    save_to_csv_by_time_interval(df, start_jog, start_rest, output_dir + '/jog.csv')
    save_to_csv_by_time_interval(df, start_rest, start_squat, output_dir + '/rest.csv')
    save_to_csv_by_time_interval(df, start_squat, start_clap, output_dir + '/squat.csv')
    save_to_csv_by_time_interval(df, start_clap, start_msrc12_1, output_dir + '/clap.csv')
    save_to_csv_by_time_interval(df, start_msrc12_1, start_msrc12_2, output_dir + '/msrc12_1.csv')
    save_to_csv_by_time_interval(df, start_msrc12_2, start_msrc12_3, output_dir + '/msrc12_2.csv')
    save_to_csv_by_time_interval(df, start_msrc12_3, start_msrc12_4, output_dir + '/msrc12_3.csv')
    save_to_csv_by_time_interval(df, start_msrc12_4, start_msrc12_5, output_dir + '/msrc12_4.csv')
    save_to_csv_by_time_interval(df, start_msrc12_5, start_msrc12_6, output_dir + '/msrc12_5.csv')
    save_to_csv_by_time_interval(df, start_msrc12_6, start_msrc12_7, output_dir + '/msrc12_6.csv')
    save_to_csv_by_time_interval(df, start_msrc12_7, start_msrc12_8, output_dir + '/msrc12_7.csv')
    save_to_csv_by_time_interval(df, start_msrc12_8, start_msrc12_9, output_dir + '/msrc12_8.csv')
    save_to_csv_by_time_interval(df, start_msrc12_9, start_msrc12_10, output_dir + '/msrc12_9.csv')
    save_to_csv_by_time_interval(df, start_msrc12_10, start_msrc12_11, output_dir + '/msrc12_10.csv')
    save_to_csv_by_time_interval(df, start_msrc12_11, start_msrc12_12, output_dir + '/msrc12_11.csv')
    save_to_csv_by_time_interval(df, start_msrc12_12, start_msrc12_12 + 15, output_dir + '/msrc12_12.csv')

    return None

if __name__ == '__main__':
    participants_path = 'participants_data.csv'
    timestamps_path = 'timestamps.csv'
    raw_data_dir = "raw_data"
    output_data_dir = "by_activity_data"
    terminal_print = True

    # Path definitions
    self_path = os.path.realpath(__file__)
    participants_path = self_path.replace('EMG RMS\\classify_emg.py', participants_path)
    timestamps_path = self_path.replace('EMG RMS\\classify_emg.py', timestamps_path)
    participants_df = pd.read_csv(participants_path)
    timestamps_df = pd.read_csv(timestamps_path)

    if terminal_print:
        start_time = time.time()
        participant_completed = 0
    # Data processing loop
    for participant in participants_df["Participant Code"]:
        if terminal_print:
            elapsed_time = time.time() - start_time
            expected_remaining_time = elapsed_time * (len(participants_df["Participant Code"]) - participant_completed)
            print(f'[Elapsed time {elapsed_time:.0f} seconds; expected remaining time {expected_remaining_time:.0f} seconds] Processing participant {participant}...', end='\r')
            participant_completed += 1
        
        p_timestamp1 = timestamps_df[timestamps_df["Participant Code"] == participant]["Timestamp 1 (s)"].values[0]
        p_timestamp2 = timestamps_df[timestamps_df["Participant Code"] == participant]["Timestamp 2 (s)"].values[0]
        p_timestamp3 = timestamps_df[timestamps_df["Participant Code"] == participant]["Timestamp 3 (s)"].values[0]
        participant_raw_data_path = self_path.replace("classify_emg.py", "\\" + raw_data_dir + "\\" + participant + ".xlsx")
        participant_output_dir = self_path.replace("classify_emg.py", "\\" + output_data_dir + "\\" + participant)

        # Create output directory
        if not os.path.exists(participant_output_dir):
            os.makedirs(participant_output_dir)

        emg_test_classification(participant_raw_data_path, participant_output_dir, p_timestamp1, p_timestamp2, p_timestamp3)
    if terminal_print:
        print(f'Took {time.time() - start_time:.0f} seconds to process {len(participants_df["Participant Code"]+1)} participants.             ',end='\n')
        print('Processing finished!' + "Processed files are now available in " + output_data_dir + " directory.")

