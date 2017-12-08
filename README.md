# eTimeCard
Digital version of Purdue's time card system. (CS252/Lab 6)

# Brief Description
Aims to provide a time stamps and descriptions of work done in a much more accessible way.

For example, a TA/Purdue employee has to log in when they start working, describe what they would do and log out. They can later access all the past time-stamps
and descriptions for their own profile.

There would be a different kind of account for professors, who would be able to see all the time-stamps and descriptions of work done for all the TAs.

# Features to be implemented

1) Back-end functionality:

  a) Maintain two separate types of accounts, for TA and Professors.

  b) Create 5 API-endpoints: Landing page, Registration, Login, Logout and Dashboard

  c) Create one database table for the user validation, and then for each individual user, maintain a separate table containing all the time-stamps
     and descriptions for that individual user

  d) Display information on the dashboard, the individual's information if they are a TA, and all the TAs information in the current user is a Professor

2) Front-end functionality

  a) Create pages corresponding to the four API routes on the Back-end
  b) Integrate with back-end

# Technologies to be used

1) Python
2) Flask, Flask Forms
3) SQLAlchemy in conjunction with MYSQL
4) HTML, CSS, JS, Bootstrap
5) Flask templates
