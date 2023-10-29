
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

#correlation matrix (make it in pandas to find correlation between all the heiggts and )

# Read the CSV files into pandas DataFrames
demographics_df = pd.read_csv("demographics.csv")
climbers_df = pd.read_csv("climbing_data.csv")

grade_climbers_df=pd.read_csv("grade_climbing_data.csv")

# Merge the DataFrames based on the 'Name' column
merged_df = pd.merge(climbers_df, demographics_df, on='climber_name', how='left')
grademerge_df=pd.merge(grade_climbers_df, demographics_df, on='climber_name', how='left')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("merged_demographics.csv", index=False)
df=pd.read_csv('merged_demographics.csv')


merged_df.to_csv("grade_merge_demographics.csv", index=False)
df=pd.read_csv('grade_merge_demographics.csv')
print(merged_df.columns)




# Load the CSV file into a DataFrame
demographics_df = pd.read_csv("demographics.csv")
climbers_df = pd.read_csv("climbing_data.csv")

climbers_df.drop(["video_name"], axis = 1, inplace=True)
print(demographics_df.head)
merged_df = pd.merge(climbers_df, demographics_df, on='climber_name', how='left')


merged_df.to_csv("merged_demographics.csv", index=False)
data = pd.read_csv('merged_demographics.csv')
print(data)

data['climber_name'] = data['climber_name'].astype('category')
data['Gender'] = data['Gender'].astype('category')



def convert_time_to_seconds(time_str):
    # Parse the time string into a datetime object
    time_obj = datetime.strptime(time_str, "%M:%S")

    # Extract minutes and seconds and convert to total seconds
    total_seconds = time_obj.minute * 60 + time_obj.second

    return total_seconds

def parse_grades(grade):
    grade = int(grade[-1])

    return grade
print(data.columns)
data['climbing_time'] = data['climbing_time'].apply(convert_time_to_seconds)
data['start_time'] = data['start_time'].apply(convert_time_to_seconds)
data['end_time'] = data['end_time'].apply(convert_time_to_seconds)

data['grade'] = data['grade'].apply(parse_grades)
print(merged_df.head())
#boxplot

# sns.boxplot(x='Age ', y='climbing_time', data=merged_df)
# plt.title('Age vs Climbing Time')
# plt.show() 
#scatter plot 
# plt.scatter(merged_df['Experience (yrs)'], merged_df['Max Grades'])
# plt.title('Experience vs Max Grades')
# plt.xlabel('Experience (years)')
# plt.ylabel('Max Grades')
# plt.show()
# #bar graph
# Calculate average total hand and foot movements for each player
# Convert these columns to numeric type for aggregation
cols_to_convert = ['right_hand_moves', 'left_hand_moves']
merged_df[cols_to_convert] = merged_df[cols_to_convert].apply(pd.to_numeric, errors='coerce')

# Calculate the average total right and left hand moves for each climber
avg_hand_moves_per_climber = merged_df.groupby('climber_name').agg({
    'right_hand_moves': 'mean',
    'left_hand_moves': 'mean'
}).reset_index()

# Sort the dataframe by climber names
avg_hand_moves_per_climber = avg_hand_moves_per_climber.sort_values('climber_name', ascending=True)

# Bar Chart
barWidth = 0.35
r1 = range(len(avg_hand_moves_per_climber))
r2 = [x + barWidth for x in r1]

plt.figure(figsize=(15, 7))

plt.bar(r1, avg_hand_moves_per_climber['right_hand_moves'], color='turquoise', width=barWidth, edgecolor='grey', label='Avg Right Hand Moves')
plt.bar(r2, avg_hand_moves_per_climber['left_hand_moves'], color='blue', width=barWidth, edgecolor='grey', label='Avg Left Hand Moves')

plt.xlabel('Climbers', fontweight='bold')
plt.xticks([r + barWidth / 2 for r in range(len(avg_hand_moves_per_climber))], avg_hand_moves_per_climber['climber_name'], rotation=90)
plt.title('Average Right Hand vs Left Hand Moves by Climber')

plt.legend()
plt.show()
cols_to_convert = ['total_num_moves', 'Experience (yrs)']
merged_df[cols_to_convert] = merged_df[cols_to_convert].apply(pd.to_numeric, errors='coerce')

# Get the experience level for each climber (assuming one experience level per climber)

# Calculate the average total number of moves for each climber
avg_moves_per_climber = merged_df.groupby('climber_name')['total_num_moves'].mean().reset_index()

# Get the experience level for each climber (assuming one experience level per climber)
experience_per_climber = merged_df.groupby('climber_name')['Experience (yrs)'].mean().reset_index()

# Merge the two dataframes on climber_name
final_df = pd.merge(avg_moves_per_climber, experience_per_climber, on='climber_name')

# Sort the dataframe by experience
final_df = final_df.sort_values('Experience (yrs)', ascending=True)

# Bar Chart
barWidth = 0.3
r1 = range(len(final_df))
r2 = [x + barWidth for x in r1]

plt.figure(figsize=(15, 7))

plt.bar(r1, final_df['total_num_moves'], color='turquoise', width=barWidth, edgecolor='grey', label='Avg Num of Moves')
plt.bar(r2, final_df['Experience (yrs)'], color='blue', width=barWidth, edgecolor='grey', label='Experience (yrs)')

plt.xlabel('Climbers', fontweight='bold')
plt.xticks([r + barWidth / 2 for r in range(len(final_df))], final_df['climber_name'], rotation=90)
plt.title('Average Number of Moves and Experience by Climber')

plt.legend()
plt.show()
cols_to_convert = ['right_hand_moves', 'left_hand_moves', 'right_leg_moves', 'left_leg_moves', 'climbing_time']
merged_df[cols_to_convert] = merged_df[cols_to_convert].apply(pd.to_numeric, errors='coerce')

avg_hand_foot_moves_per_player = merged_df.groupby('climber_name').agg({
    'right_hand_moves': 'mean',
    'left_hand_moves': 'mean',
    'right_leg_moves': 'mean',
    'left_leg_moves': 'mean',
    'climbing_time': 'mean'
}).reset_index()

# Continue with your existing code for aggregating the average movements and time
avg_hand_foot_moves_per_player = merged_df.groupby('climber_name').agg({
    'right_hand_moves': 'mean',
    'left_hand_moves': 'mean',
    'right_leg_moves': 'mean',
    'left_leg_moves': 'mean',
    'climbing_time': 'mean'
}).reset_index()

# Create the bar plot
barWidth = 0.2
fig = plt.figure(figsize =(12, 8))

# Set the bar positions
r1 = np.arange(len(avg_hand_foot_moves_per_player['climber_name']))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

# Create the bars
plt.bar(r1, avg_hand_foot_moves_per_player['right_hand_moves'], color ='b', width = barWidth, edgecolor ='grey', label ='right_hand_moves')
plt.bar(r2, avg_hand_foot_moves_per_player['left_hand_moves'], color ='c', width = barWidth, edgecolor ='grey', label ='left_hand_moves')
plt.bar(r3, avg_hand_foot_moves_per_player['right_leg_moves'], color ='m', width = barWidth, edgecolor ='grey', label ='right_leg_moves')
plt.bar(r4, avg_hand_foot_moves_per_player['left_leg_moves'], color ='y', width = barWidth, edgecolor ='grey', label ='left_leg_moves')
plt.bar(r5, avg_hand_foot_moves_per_player['climbing_time'], color ='r', width = barWidth, edgecolor ='grey', label ='climbing_time')

# Add labels and title
plt.xlabel('Climbers', fontweight ='bold')
plt.ylabel('Average Values')
plt.title('Average Hand/Foot Movements and Time by Climber')
plt.xticks([r + barWidth for r in range(len(avg_hand_foot_moves_per_player['climber_name']))], avg_hand_foot_moves_per_player['climber_name'], rotation=90)

# Show legend
plt.legend()

# Show the plot
plt.show()



# Your existing code to create the correlation matrix
quant_df = data.drop(['route', 'success', 'Gender', 'climbing_time', 'start_time', 'end_time'], axis=1)
quant_df = quant_df[quant_df['climber_name'] != "Ethan"]
quant_df = quant_df[quant_df['climber_name'] != "Tristan"]
print(np.unique(quant_df['climber_name']))

quant_df.drop(['climber_name'], axis=1, inplace=True)
corr_matrix = quant_df.corr()

# Create a heatmap of the correlation matrix
plt.matshow(corr_matrix)

# Add column labels as axes
plt.xticks(range(len(quant_df.columns)), quant_df.columns, rotation=90)
plt.yticks(range(len(quant_df.columns)), quant_df.columns)
print(corr_matrix)
corr_matrix.to_csv('correlation_matrix.csv')

plt.show()



















# Assume the DataFrame is loaded in merged_df
# Replace the following line with actual code to load your DataFrame
# merged_df = pd.read_csv("your_file.csv")



# tallest players
max_height = merged_df['Height '].max()
tallest_climbers = merged_df[merged_df['Height '] == max_height]['climber_name'].unique()
print(f"The tallest height is {max_height}")
print(f"Climbers with the tallest height: {', '.join(tallest_climbers)}")
tallest_players = merged_df[merged_df['Height '] == merged_df['Height '].max()]['climber_name'].unique()

#shortest players
min_height = merged_df['Height '].min()
shortest_climbers = merged_df[merged_df['Height '] == min_height]['climber_name'].unique()
print(f"The tallest height is {min_height}")
print(f"Climbers with the shortest height: {', '.join(shortest_climbers)}")
shortest_players = merged_df[merged_df['Height '] == merged_df['Height '].min()]['climber_name'].unique()



# print(f"Tallest players: {', '.join(tallest_players)}")
# print(f"Shortest players: {', '.join(shortest_players)}")

# # Calculate the average number of moves for each player
# avg_moves_per_player = merged_df.groupby('climber_name')['total_num_moves'].mean().reset_index()

# # Plotting
# plt.figure(figsize=(10, 6))
# for name in tallest_players:
#     plt.scatter(avg_moves_per_player[avg_moves_per_player['climber_name'] == name]['total_num_moves'],
#                 merged_df[merged_df['climber_name'] == name]['Height'].mean(),
#                 color='red',
#                 label=f'Tallest - {name}')

# for name in shortest_players:
#     plt.scatter(avg_moves_per_player[avg_moves_per_player['climber_name'] == name]['total_num_moves'],
#                 merged_df[merged_df['climber_name'] == name]['Height'].mean(),
#                 color='blue',
#                 label=f'Shortest - {name}')

# plt.scatter(avg_moves_per_player['total_num_moves'], merged_df.groupby('climber_name')['Height'].mean().reset_index()['Height'],
#             color='green',
#             label='Others')

# plt.xlabel('Average Number of Moves')
# plt.ylabel('Height')
# plt.legend()
# plt.title('Average Number of Moves Based on Height')
# plt.show()

# print(df)
# print(df.columns)

#visualization ideas
# Get the person with the highest and lowest grades
# highest_grade = merged_df['grade'].max()
# lowest_grade = merged_df['grade'].min()
# highest_grade_person = merged_df[merged_df['grade'] == highest_grade]
# lowest_grade_person = merged_df[merged_df['grade'] == lowest_grade]

# print(highest_grade_person)
# highest_grade = merged_df['grade'].max()
# print("highest grade:")
# print(highest_grade)
# highest_grade_data = merged_df[merged_df['grade'] == highest_grade]
# highest_grade_person = highest_grade_data.iloc[0]
# print("highest: ")
# print(highest_grade_person)

# # print(lowest_grade_person)
# lowest_grade = merged_df['grade'].min()
# lowest_grade_data = merged_df[merged_df['grade'] == lowest_grade]
# lowest_grade_person = lowest_grade_data.iloc[0]
# print("lowest: ")
# print(lowest_grade_person)



# Visualization 1: Compare the difference in total number of steps
# plt.figure(figsize=(10, 6))
# plt.bar(['Highest Grade', 'Lowest Grade'], [highest_grade_person['total_steps'].mean(), lowest_grade_person['total_steps'].mean()])
# plt.title('Total Steps Comparison')
# plt.xlabel('Grade')
# plt.ylabel('Total Steps')
# plt.show()

# # Visualization 2: Compare the difference in avg time to complete a route
# plt.figure(figsize=(10, 6))
# plt.bar(['Highest Grade', 'Lowest Grade'], [highest_grade_person['avg_time'].mean(), lowest_grade_person['avg_time'].mean()])
# plt.title('Average Time to Complete a Route')
# plt.xlabel('Grade')
# plt.ylabel('Average Time (seconds)')
# plt.show()

# # Visualization 3: Moves per minute
# plt.figure(figsize=(10, 6))
# sns.barplot(x='climber_name', y='moves_per_minute', data=merged_df)
# plt.title('Moves Per Minute Comparison')
# plt.xlabel('Climber')
# plt.ylabel('Moves Per Minute')
# plt.show()

# # Visualization 4: Height vs Number of Moves
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='height', y='total_moves', data=merged_df)
# plt.title('Height vs Number of Moves')
# plt.xlabel('Height (cm)')
# plt.ylabel('Total Moves')
# plt.show()
# #get person with highest grade and personlowest grade and compare the difference in total number of steps in takes in total (label graph)
# #get person with highest grade and personlowest grade and compare the difference in avg time in takes in total to complete a route (label graph)
# #compare the moves per minute between people 
# #compare height with number of moves you take (to answer this question: does being shorter on avergae make you take more moves or less moves)