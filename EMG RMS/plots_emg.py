import pandas as pd
from matplotlib import pyplot as plt
import os

def plot_action(df, title, timecol = "X[s]", cols=["a: EMG RMS 1-1", "a: EMG RMS 1-2", "a: EMG RMS 1-3", "a: EMG RMS 1-4"], scale='log'):
    """
    Plot the EMG RMS data for an action.
    Inputs:
        df: DataFrame with the data
        title: Title of the plot
        timecol: Column name for the time (by default "X[s]")
        cols: List with the columns to plot (by default ["a: EMG RMS 1-1", "a: EMG RMS 1-2", "a: EMG RMS 1-3", "a: EMG RMS 1-4"])
        scale: Scale of the y-axis (by default 'log')
    Returns:
        None
    """

    for col in cols:
        plt.plot(df[timecol], df[col], label=col)
    plt.title(title)
    plt.xlabel("Time [s]")
    plt.ylabel("EMG [mV]")
    plt.yscale(scale)
    plt.grid()
    plt.legend()
    plt.show()
    return None

if __name__ == "__main__":
    # Parameters
    activity_dir = "by_activity_data"
    participant_dir = "P7"
    action_csv = "scroll"
    title = f"EMG - {participant_dir} - {action_csv}"

    # Load df
    path = os.path.dirname(os.path.realpath(__file__)) + f"\\{activity_dir}\\{participant_dir}\\{action_csv}.csv"
    df = pd.read_csv(path)
    plot_action(df, title)

