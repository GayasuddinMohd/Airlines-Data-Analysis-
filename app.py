import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the title of the Streamlit app
st.title("Airlines Data Analysis")

# Description
st.markdown("""
This application provides an interactive interface to explore the Airlines dataset.
You can view various plots and insights extracted from the data.
""")

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Establish connection to the SQLite database
file_path = 'C:\\Users\\abc\\Desktop\\travel.sqlite'
connection = sqlite3.connect(file_path)
cursor = connection.cursor()

# List all tables in the database
def get_table_list():
    cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
    return [table[0] for table in cursor.fetchall()]

table_list = get_table_list()

# Sidebar for navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox(
    "Choose a visualization",
    ["Dataset Overview", "Planes with >100 Seats", "Tickets Booked Over Time",
     "Total Amount Earned Over Time", "Average Charges per Aircraft",
     "Occupancy Rate Analysis", "Increased Turnover with Higher Occupancy"]
)

# Load data from a table with error handling
def load_data(query):
    try:
        return pd.read_sql_query(query, connection)
    except pd.errors.DatabaseError as e:
        st.error(f"DatabaseError: {e}")
        return pd.DataFrame()

# Display content based on the selected page
if page == "Dataset Overview":
    st.write('List of tables present in the database:', table_list)
    st.write("### Example Data from Each Table")
    for table in table_list:
        st.write(f"#### Table: {table}")
        data = load_data(f"SELECT * FROM {table} LIMIT 5")
        st.write(data)

elif page == "Planes with >100 Seats":
    st.write("### How many planes have more than 100 seats?")
    if 'seats' in table_list:
        planes_with_more_seats = load_data("""
            SELECT aircraft_code, COUNT(*) as num_seats 
            FROM seats 
            GROUP BY aircraft_code 
            HAVING num_seats > 100
        """)
        st.write(planes_with_more_seats)
    else:
        st.write("Table 'seats' does not exist.")

elif page == "Tickets Booked Over Time":
    st.write("### Number of tickets booked over time")
    if 'tickets' in table_list and 'bookings' in table_list:
        tickets = load_data("""
            SELECT tickets.*, bookings.book_date 
            FROM tickets 
            INNER JOIN bookings ON tickets.book_ref = bookings.book_ref
        """)
        tickets['book_date'] = pd.to_datetime(tickets['book_date'])
        tickets['date'] = tickets['book_date'].dt.date
        x = tickets.groupby('date').size().reset_index(name='count')

        plt.figure(figsize=(10,6))
        plt.plot(x['date'], x['count'], marker='^')
        plt.xlabel('Date', fontsize=20)
        plt.ylabel('Number of Tickets', fontsize=20)
        plt.grid(True)
        st.pyplot(plt)
    else:
        st.write("Required tables ('tickets' and 'bookings') do not exist.")

elif page == "Total Amount Earned Over Time":
    st.write("### Total amount earned over time")
    if 'bookings' in table_list:
        bookings = load_data("SELECT * FROM bookings")
        bookings['book_date'] = pd.to_datetime(bookings['book_date'])
        bookings['date'] = bookings['book_date'].dt.date
        x = bookings.groupby('date')[['total_amount']].sum()

        plt.figure(figsize=(10,6))
        plt.plot(x.index, x['total_amount'], marker='^')
        plt.xlabel('Date', fontsize=20)
        plt.ylabel('Total Amount Earned', fontsize=20)
        plt.grid(True)
        st.pyplot(plt)
    else:
        st.write("Table 'bookings' does not exist.")

elif page == "Average Charges per Aircraft":
    st.write("### Average charges for each aircraft with different fare conditions")
    if 'ticket_flights' in table_list and 'flights' in table_list:
        avg_charges = load_data("""
            SELECT fare_conditions, aircraft_code, AVG(amount) AS avg_amount 
            FROM ticket_flights 
            JOIN flights ON ticket_flights.flight_id = flights.flight_id
            GROUP BY aircraft_code, fare_conditions
        """)
        plt.figure(figsize=(8,6))
        sns.barplot(data=avg_charges, x='aircraft_code', y='avg_amount', hue='fare_conditions')
        plt.xlabel('Aircraft Code', fontsize=15)
        plt.ylabel('Average Amount', fontsize=15)
        plt.title('Average Charges per Aircraft')
        plt.grid(True)
        st.pyplot(plt)
    else:
        st.write("Required tables ('ticket_flights' and 'flights') do not exist.")

elif page == "Occupancy Rate Analysis":
    st.write("### Analyzing Occupancy Rate")
    if 'boarding_passes' in table_list and 'seats' in table_list:
        occupancy_rate = load_data("""
            SELECT a.aircraft_code, AVG(a.seats_count) AS booked_seats, b.num_seats, 
            AVG(a.seats_count) / b.num_seats AS occupancy_rate
            FROM (
                SELECT aircraft_code, flights.flight_id, COUNT(*) AS seats_count
                FROM boarding_passes
                INNER JOIN flights ON boarding_passes.flight_id = flights.flight_id
                GROUP BY aircraft_code, flights.flight_id
            ) AS a
            INNER JOIN (
                SELECT aircraft_code, COUNT(*) AS num_seats
                FROM seats
                GROUP BY aircraft_code
            ) AS b ON a.aircraft_code = b.aircraft_code
            GROUP BY a.aircraft_code
        """)
        st.write(occupancy_rate)
    else:
        st.write("Required tables ('boarding_passes' and 'seats') do not exist.")

elif page == "Increased Turnover with Higher Occupancy":
    st.write("### Potential Increase in Annual Turnover with Higher Occupancy Rate")
    if 'ticket_flights' in table_list and 'flights' in table_list:
        occupancy_rate = load_data("""
            SELECT a.aircraft_code, AVG(a.seats_count) AS booked_seats, b.num_seats, 
            AVG(a.seats_count) / b.num_seats AS occupancy_rate
            FROM (
                SELECT aircraft_code, flights.flight_id, COUNT(*) AS seats_count
                FROM boarding_passes
                INNER JOIN flights ON boarding_passes.flight_id = flights.flight_id
                GROUP BY aircraft_code, flights.flight_id
            ) AS a
            INNER JOIN (
                SELECT aircraft_code, COUNT(*) AS num_seats
                FROM seats
                GROUP BY aircraft_code
            ) AS b ON a.aircraft_code = b.aircraft_code
            GROUP BY a.aircraft_code
        """)
        occupancy_rate['Inc occupancy_rate'] = occupancy_rate['occupancy_rate'] + occupancy_rate['occupancy_rate'] * 0.1

        total_revenue = load_data("""
            SELECT aircraft_code, SUM(amount) AS total_revenue 
            FROM ticket_flights
            JOIN flights ON ticket_flights.flight_id = flights.flight_id
            GROUP BY aircraft_code
        """)

        occupancy_rate['Inc Total Annual Turnover'] = (total_revenue['total_revenue']) / occupancy_rate['occupancy_rate'] * occupancy_rate['Inc occupancy_rate']
        st.write(occupancy_rate[['aircraft_code', 'Inc Total Annual Turnover']])
    else:
        st.write("Required tables ('ticket_flights' and 'flights') do not exist.")

# Close the database connection
connection.close()

# Footer
st.sidebar.info("© 2024 Airlines Data Analysis")