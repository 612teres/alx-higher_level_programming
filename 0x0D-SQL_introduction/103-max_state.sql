-- this script displays max-temp of each state by order of the state name
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
