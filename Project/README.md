# IU INTERNATIONAL UNIVERSITY OF APPLIED SCIENCES

### Build a Data Mart in SQL (DLBDSPBDM01)
A SQL database designed to be utilized for a functional Airbnb in PostgreSQL.
PostgreSQL was chosen from numerous popular SQL Databases because it has Full ACID compliance, the diverse data types, less strict license requirements, more advanced queries due to high-level SQL Compliance (Table inheritance, window functions, etc.), flexibility (options to add new data types, customized functions) and the ability to use Multi-Version Concurrency Control (MVCC) which is great for high transaction volumes.

## Purpose
The datamart project is meant to understand how a datamart is modelled, developed and used with examples.

# Development Planning - UML Schemas
## UML Diagram (Revised)
Diagram - Entity Relationship Model (ERM)
![Finalized ERM Diagram](/images/ERM_Finalization.png)

## Data Dictionary
The following tables have been revised in the finalization phase to reflect the database current state.
You can also find the Excel file in the documents folder. The script `sql/data_dictionary.sql` can be run in a query to output the table.
![Finalized Dictionary Diagram](/images/data_dictionary_p1.png)
![Finalized Dictionary Diagram](/images/data_dictionary_p2.png)

# Database Tables Summary
Here's a brief summary of all the tables in the database:
1. **Access Level:** Defines different access levels and roles within the system.
2. **AccessLevelAllowedOperations:** Represents allowed operations for each access level.
3. **Activity Log:** Logs user activities, queries, and execution timestamps.
4. **Admin:** Contains information about administrators.
5. **Allowed Operations:** Describes permitted database operations.
6. **Amenity:** Represents different amenities with categories.
7. **Amenity Categories:** Contains categories of amenities.
8. **Booking:** Stores details about property bookings, including guests, hosts, and payments.
9. **Chat:** Manages chat sessions between hosts and guests.
10. **Country:** Provides information about different countries.
11. **Guest:** Represents information about guests.
12. **Host:** Contains information about hosts.
13. **Language:** Lists various languages.
14. **Media:** Stores information about media files, including owner and file details.
15. **Message:** Manages messages exchanged between users.
16. **Payment:** Contains payment details for property bookings.
17. **Payment Method:** Describes different payment methods.
18. **Payment Method Name:** Contains names of payment methods.
19. **Payment Status:** Represents payment statuses.
20. **Preferences:** Stores user preferences, including language and contact settings.
21. **Preferences Amenity, Country, Property Type:** Link preferences with amenities, countries, and property types.
22. **Promo:** Manages promotional codes and their details.
23. **Property:** Represents properties with location, capacity, and amenities.
24. **Property Amenity:** Links properties with amenities.
25. **Property Images:** Links properties with images.
26. **Property Review:** Links properties with reviews.
27. **Property Type:** Describes different property types.
28. **Review:** Contains user reviews, ratings, and comments.
29. **Review Type:** Describes the entity being reviewed.
30. **User:** Stores user information, including guests, hosts, and administrators.
31. **User Type:** Defines different user types.

# How to get started
## Dependencies
-PostgreSQL

-pgAdmin4

## Install Postgresql (Ubuntu 22.04 LTS)
Linux Installation Script - PSQL Account creation, database deployment, table creations and data insertion.
![Linux Installation Script](/images/install_script.gif)
According to the documentation on Ubuntu: https://ubuntu.com/server/docs/databases-postgresql

## Installation instructions for Linux
1. `git clone https://github.com/DeusNexus/iu-sql-airbnb.git`
2. `sudo chmod +x install.sh && ./install.sh` (Can take 3-10 minutes due to row-wise sql insertions)
3. Open pgAdmin4 and fill out the following connection information: 
    - Register Server, Name: Localhost
    - Connection, Host name/address: localhost, Port: 5432, Username: postgres
    - The databasese from your localhost should now show up including the `airbnb_test` database created by the `install.sh` script
4. Expand views Localhost > Databases and right-click on airbnb_test, set owner to `postgres` if issues with ownership read permissions.
5. Now you can interact with the `airbnb_test` and see the tables/views under airbnb_test > Schemas > Tables and/or Views.
6. E.g. see the View of `property_view` by right-click > View/Edit Data > All Rows to see the view rows.

## Installation platform independent (fast)
1. Make sure Postgres and pgAdmin4 are installed.
2. Open pgAdmin4, Register new Localhost serverand fill out the following connection information: 
    - Register Server, Name: Localhost
    - Connection, Host name/address: localhost, Port: 5432, Username: postgres
3. Create a new database, e.g. name it `airbnb_test` by right-click Databases > Create > Database ...:
    - Database: `airbnb_test`
    - Owner: `postgres`
4. After the new database shows up right-click on it, Restore and select for Filename (database dump): ./sql/airbnb_pgadmin4.sql
5. The complete database should now been initialized and you can interact with it similar to install steps 5 & 6 for Linux.

# Metadata Overview
To see the metadata of the database, first let pgAdmin4 analyze each table so the stats are up-to-date. The code below can be used by pasting it in a Query and is found in `./sql/analyze_metadata.sql`.

# Table Creation and Data Insertions
The linux installation script uses the individual SQL files to create the database (which takes longer) however this allows for viewing the SQL files in plain text (UTF-8). These can be found in the folder `./sql/create_table_scripts`. Once all tables are created, the table entries are inserted which can be found in the `./sql/insert_rows_scripts` folder.

# Example Queries
Under `./sql/views` several SQL scripts have been included that can create a view. Tables can be joined and using SELECT statement the desired columns can be displayed.

**View Chat Guest Host ID**
Shows how we can map the user id for both guest and host. This can be used to join different tables.

![View Chat Guest Host ID](/images/view_chat_guest_host_id.png)

**View Media Owner by Host**
Shows Media Files owner by different hosts.

![View Media Owner by Host](/images/view_media_owner_by_host.png)

**View Preferences Property Amenity Country**
Shows the preferences of a user by joining on the different foreign table keys for Property, Amenity and Country.

![View Preferences Property Amenity Country](/images/view_preferences_pac.png)

**View Property**
Shows details about a property after joining all the relevant foreign keys.

![View Property](/images/view_property.png)

**View Review Booking**
Shows reviews with detailed information after joining relevent booking tables.

![View Review Booking](/images/view_review_booking.png)

# Database Views
In the database under Views `property_view` can be observed which shows several tables joined to get a rich description of each property.

# Reflection
Throughout the process of creating the SQL Data Mart for Airbnb, I have gained invaluable insights into database design, implementation, and management. Working with PostgreSQL provided a deep understanding of its features, including Full ACID compliance, diverse data types, and the advantages of Multi-Version Concurrency Control (MVCC) for high transaction volumes. The development journey enhanced my skills in conceptualizing and modeling a datamart, incorporating UML schemas, and refining the data dictionary. Addressing challenges, such as table relationships, primary and foreign keys, and optimizing queries, strengthened my problem-solving abilities. The iterative process of revising the UML diagram and data dictionary underscored the importance of precision in database modeling. Hands-on experience in creating tables, populating data, and implementing complex queries deepened my comprehension of real-world database scenarios. Overall, this project has been a comprehensive exploration, expanding my knowledge of SQL databases and their practical applications.

# Conclusion
The SQL Datamart AirBnB project has learned me a great deal. I know how to properly JOIN tables now using primary and foreign keys, design many-to-many tables for look ups, use SELECT, GROUPBY and other statements to build a real-world database using state-of-the-art database systems.

# Disclaimer
The developed application is licensed under the GNU General Public License.