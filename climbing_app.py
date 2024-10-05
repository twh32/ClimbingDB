import streamlit as st

# Function to load the data with caching
@st.cache_data
def load_data():
    # Load the dataset
    data = pd.read_csv('merged_demographics.csv')

    # Ensure 'Max Grades' is treated as a string before extracting numeric values
    if 'Max Grades' in data.columns:
        data['Max Grades'] = data['Max Grades'].astype(str)
        data['grade_numeric'] = data['Max Grades'].str.extract(r'(\d+)').astype(float)  # Extract numerical values for grades
    else:
        st.error("The 'Max Grades' column is missing from the dataset.")
    
    return data

# Set up the Streamlit app with dark theme
st.set_page_config(page_title="First attempt at streamlit using climbing data", layout="wide", initial_sidebar_state="collapsed")

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Title and introductory text
st.title("First attempt at streamlit using climbing data")
st.header("This is an example of a header")
st.write("A journey of a thousand climbs starts with a single jug.")

# Load the data
data = load_data()

# Check if the required columns are present in the data
required_columns = ['Experience (yrs)', 'grade_numeric', 'success']
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    st.error(f"Missing columns: {', '.join(missing_columns)}")
else:
    # Plot: Scatter plot comparing experience and grade numeric by success
    st.subheader("How success at v grades compares to experience")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=data['Experience (yrs)'], y=data['grade_numeric'], hue=data['success'], palette='coolwarm', ax=ax)
    ax.set_title("Success at V Grades vs. Experience")
    st.pyplot(fig)

    st.divider()

    st.header("Some example code block")

    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language="python")

    st.divider()

    # Correlation Matrix Plot
    st.subheader("Correlation between Experience, Avg Pull Ups, and Max Grade")
    correlation_matrix = data[['Experience (yrs)', 'Avg Pull Ups ', 'grade_numeric']].corr()

    # Display the correlation matrix
    st.write(correlation_matrix)
    # Plot heatmap of correlations
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)
