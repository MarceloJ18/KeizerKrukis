'''
This .py file is to contain all the functions that were created
in the execution of the EDA (automating graphic creation)
'''
import pandas as pd
import matplotlib.pyplot as plt


'''
We defined a global color code that will be used thoughout 
the exploration of the datasets
'''
col_code = ['#66d4db',
            '#caf0f2',
            '#969ea7',
            '#d9dde2', 
            '#66b3b8',
            '#66888b', 
            '#66a4a9', 
            '#7dadb0', 
            '#008992']




#creating a function that will automate the creation of piecharts
def auto_pie(
        series: pd.DataFrame, 
        title: str, 
        legend_title: str, 
        label_top: str, 
        label_bottom: str):
    
    '''
    This function creates a Pie-Chart displaying
    the percentage correspondent to every slice

    Arguments:
  - series(pd.DataFrame): more specifically the variable that
will be analyzed.
  - title(str): The title to display above the chart.
  - legent_title(str): The title to display on top of the
  legend
  - label_top(str): the label of the category to be displayed on top
  - label_bottom(str): the label of the category to be displayed in the bottom
  **Note**: This function is only applicable for variables with
            binary distribution
    
    '''

    # setting the color palette that will be used
    colours = col_code
    
    # creating the pie chart
    fig, ax = plt.subplots()
    ax.pie(series.value_counts(), 
    labels=series.value_counts().index, 
    colors=colours, 
    autopct='%1.2f%%', 
    textprops={'fontsize': 16})
    
    # setting the title and legend
    ax.set_title(title, fontsize=16)
    ax.legend(title=legend_title,
              labels=[label_top, label_bottom],
    loc='upper right')
    
    # removing the y-label
    ax.set_ylabel('')
    
    # displaying the chart
    plt.show()

#creating a function to automate the creation of bar charts
def auto_bar(series: pd.Series,
             title: str,
             x_axis_label: str,
             y_axis_label: str):

    '''
    This function creates a Pie-Chart displaying
    the percentage correspondent to every slice

    Arguments:
  - series(pd.DataFrame): more specifically the variable that
will be analyzed.
  - title(str): The title to display above the chart.
  - x_axis_label(str): The label to be displayed on the x-axis
  - y_axis_label(str): The label to be displayed on the y-axis

  **Note**: This function is only applicable for variables with
            binary distribution
    
    '''


    # Calculating the value counts for each unique value in the series
    value_counts = series.value_counts()

    # Creating the bar chart
    plt.bar(value_counts.index,
            value_counts.values,
            color='#caf0f2', 
            edgecolor='black',
            linewidth=1.2)

    # Setting the title and axis labels
    plt.title(title, fontsize=16)
    plt.xlabel(x_axis_label, fontsize=12)
    plt.ylabel(y_axis_label, fontsize=12)

    # Displaying the created chart
    plt.show()
    