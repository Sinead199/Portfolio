-- 1) Write a query that returns a list of reservations that end in July 2023, including the name of the guest, 
-- the room number(s), and the reservation dates.

SELECT 
	g.fname `First Name`,
    g.lname `Last Name`,
    rr.roomno `Room Number`,
    r.startdate `Start Date`,
    r.enddate `End Date`
FROM Guest as g
JOIN GuestRes as gr ON gr.GuestId = g.GuestId
JOIN Reservation as r ON gr.ResId = r.ResId
JOIN RoomRes as rr ON r.ResId = rr.ResId
WHERE r.EndDate LIKE '2023-07%';

-- First Name   Last Name 	Room Number Start Date 	End Date
-- Sinead		Kelly		205			2023-06-28	2023-07-02
-- Walter		Holaway		204			2023-07-13	2023-07-14
-- Wilfred		Vise		401			2023-07-18	2023-07-21
-- Bettyann		Seery		303			2023-07-28	2023-07-29

-- 2) Write a query that returns a list of all reservations for rooms with a jacuzzi, displaying the guest's name,
-- the room number, and the dates of the reservation.

SELECT 
	g.fname `First Name`,
    g.lname `Last Name`,
    r.roomno `Room Number`,
    res.startdate `Start Date`,
    res.enddate `End Date`
FROM Amenity as a
JOIN RoomAmenity as ra ON ra.AmenityId = a.AmenityId
JOIN Room as r ON r.RoomNo = ra.RoomNo
JOIN RoomRes as rr ON rr.RoomNo = ra.RoomNo
JOIN Reservation as res ON res.ResId = rr.ResId
JOIN GuestRes as gr ON gr.ResId = res.ResId
JOIN Guest as g ON g.GuestId = gr.GuestId
WHERE AmenityType LIKE 'Jacuzzi';

# First Name	Last Name	Room Number	Start Date	End Date
-- Karie		Yang		201			2023-03-06	2023-03-07
-- Bettyann		Seery		203			2023-02-05	2023-02-10
-- Karie		Yang		203			2023-09-13	2023-09-15
-- Sinead		Kelly		205			2023-06-28	2023-07-02
-- Wilfred		Vise		207			2023-04-23	2023-04-24
-- Walter		Holaway		301			2023-04-09	2023-04-13
-- Mack			Simmer		301			2023-11-22	2023-11-25
-- Bettyann		Seery		303			2023-07-28	2023-07-29
-- Duane		Cullison	305			2023-02-22	2023-02-24
-- Bettyann		Seery		305			2023-08-30	2023-09-01
-- Sinead		Kelly		307			2023-03-17	2023-03-20

-- 3) Write a query that returns all the rooms reserved for a specific guest, including the guest's name, 
-- the room(s) reserved, the starting date of the reservation, and how many people were included in the reservation. 
-- (Choose a guest's name from the existing data.)

SELECT 
	rr.roomno `Room number`,
    g.fname `First name`,
    g.lname `Last name`,
    res.startdate `Start date`,
    res.adults `Adults`,
    res.children `Children`
FROM Guest as g
JOIN GuestRes as gr ON gr.GuestId = g.GuestId
JOIN Reservation as res ON res.ResId = gr.ResId
JOIN RoomRes as rr ON rr.ResId = res.ResId
WHERE g.fname LIKE 'Sinead' AND g.lname LIKE 'Kelly';

# Room number	First name	Last name	Start date	Adults	Children
-- 307			Sinead		Kelly		2023-03-17	1		1
-- 205			Sinead		Kelly		2023-06-28	2		0

-- 4) Write a query that returns a list of rooms, reservation ID, and per-room cost for each reservation. The results 
-- should include all rooms, whether or not there is a reservation associated with the room.

SELECT
	r.roomno `Room number`,
    rr.resid `Reservation ID`,
    rt.baseprice `Base Price`
    FROM RoomType as rt
    RIGHT OUTER JOIN Room as r ON r.RoomTypeId = rt.RoomTypeId
    LEFT OUTER JOIN RoomRes as rr ON rr.RoomNo = r.RoomNo
ORDER BY r.Roomno;

-- Room number  Reservation ID  Base Price
-- 201			4				174.99
-- 202			7				174.99
-- 203			2				174.99
-- 203			21				174.99
-- 204			16				174.99
-- 205			15				149.99
-- 206			12				149.99
-- 206			23				149.99
-- 207			10				149.99
-- 208			13				149.99
-- 208			20				149.99
-- 301			9				174.99
-- 301			24				174.99
-- 302			6				174.99
-- 302			25				174.99
-- 303			18				174.99
-- 304			14				174.99
-- 305			3				149.99
-- 305			19				149.99
-- 306 		   NULL 			149.99
-- 307			5				149.99
-- 308			1				149.99
-- 401			11				399.99
-- 401			17				399.99
-- 401			22				399.99
-- 402		   NULL				399.99

-- 5) Write a query that returns all the rooms accommodating at least three guests and that are reserved on any date in April 2023.

SELECT
	rr.roomno `Room Number`,
	r.adults + r.children as `Guests`,
    r.startdate `Start Date`,
    r.enddate `End Date`
FROM Reservation r
JOIN RoomRes rr ON rr.ResId = r.ResId
WHERE (r.adults + r.children >= 3) AND (r.startdate LIKE '%2023-04' OR r.enddate LIKE '%2023-04');

-- There are no rooms reserved for at least 3 guests and are reserved for April

-- Room Number	Guests	Start Date	End Date
-- 304			3	    2023-06-17	2023-06-18
-- 204			4		2023-07-13	2023-07-14
-- 401			6		2023-07-18	2023-07-21
-- 303			3		2023-07-28	2023-07-29
-- 203			4		2023-09-13	2023-09-15
-- 401			4		2023-11-22	2023-11-25
-- 301			4		2023-11-22	2023-11-25

-- 6) Write a query that returns a list of all guest names and the number of reservations per guest, sorted starting with the guest 
-- with the most reservations and then by the guest's last name.

SELECT
	g.fname `First Name`, 
	g.lname `Last Name`, 
	count(gr.guestid) AS `Reservation Count`
FROM guest g
JOIN guestres gr ON gr.guestid=g.guestid
GROUP BY g.guestid
ORDER BY `Reservation Count` DESC;

# First Name	Last Name	Reservation Count
-- Mack			Simmer		4
-- Bettyann		Seery		3
-- Sinead		Kelly		2
-- Duane		Cullison	2
-- Karie		Yang		2
-- Aurore		Lipton		2
-- Walter		Holaway		2
-- Wilfred		Vise		2
-- Maritza		Tilton		2
-- Joleen		Tison		2
-- Zachery		Luechtefeld	1

SELECT
	g.fname `First Name`, 
	g.lname `Last Name`, 
	count(gr.guestid) AS `Reservation Count`
FROM guest g
JOIN guestres gr ON gr.guestid=g.guestid
GROUP BY g.guestid
ORDER BY g.lname ASC;

# First Name	Last Name	Reservation Count
-- Duane	   	Cullison	2
-- Walter		Holaway		2
-- Sinead		Kelly		2
-- Aurore		Lipton		2
-- Zachery		Luechtefeld	1
-- Bettyann		Seery		3
-- Mack			Simmer		4
-- Maritza		Tilton		2
-- Joleen		Tison		2
-- Wilfred		Vise		2
-- Karie		Yang		2

-- 7) Write a query that displays the name, address, and phone number of a guest based on their phone number. (Choose a phone number 
-- from the existing data.)

SELECT
	fname `First Name`,
    lname `Last Name`,
    address `Address`,
    phone `Phone Number`
FROM Guest 
WHERE phone ='(814) 485-2615';

# First Name	Last Name	    Address	         Phone Number
-- Zachery	    Luechtefeld	    7 Poplar Dr.	(814) 485-2615
