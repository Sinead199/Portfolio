DROP DATABASE IF EXISTS hotelDB;

CREATE DATABASE hotelDB;

USE hotelDB;

-- Table: roomType
CREATE TABLE RoomType (
	RoomTypeId int NOT NULL primary key auto_increment,
    RoomType varchar(7) NOT NULL,
    BasePrice decimal(6,2) NOT NULL
);

-- Table: room
CREATE TABLE Room (
    RoomNo int  NOT NULL primary key,
    RoomTypeId int NOT NULL,
    ADA boolean NOT NULL,
    StndOccupancy int NOT NULL,
    MaxOccupancy int NOT NULL,
    ExtraPerson decimal(2,0) NULL,
    
    foreign key fk_Room_RoomTypeId (RoomTypeId)
		references RoomType(RoomTypeId)
);

-- Table: roomAmenity
CREATE TABLE Amenity (
    AmenityId int NOT NULL primary key auto_increment,
    AmenityType varchar(12) NOT NULL,
    JacuzziCharge decimal(2,0) NULL
);

-- Table: reservation
CREATE TABLE Reservation (
    ResId int NOT NULL primary key,
    Adults int NOT NULL,
    Children int NOT NULL,
    StartDate date NOT NULL,
    EndDate date NOT NULL,
    TotalCost decimal(6,2) NOT NULL
);

-- Table: guest
CREATE TABLE Guest (
    GuestId int NOT NULL auto_increment primary key,
    Fname varchar(50) NOT NULL,
    Lname varchar(50) NOT NULL,
    Address varchar(60) NOT NULL,
    City varchar(30) NOT NULL,
    State char(2) NOT NULL,
    Zip char(5) NOT NULL,
    Phone varchar(14) NOT NULL
);

-- Table: roomAmenity
-- Bridge table
CREATE TABLE RoomAmenity (
	RoomNo int NOT NULL,
    AmenityId int NOT NULL,
    
    foreign key fk_RoomAmenity_RoomNo (RoomNo)
		references Room(RoomNo),
	foreign key fk_RoomAmenity_AmenityId (AmenityId)
		references Amenity(AmenityId)
);

-- Table: roomRes
-- Bridge table
CREATE TABLE RoomRes (
	ResId int NOT NULL,
	RoomNo int NOT NULL,
    
    foreign key fk_RoomRes_ResId (ResId)
		references Reservation(ResId) ON DELETE CASCADE,
	foreign key fk_RoomRes_RoomNo (RoomNo)
		references Room(RoomNo) ON DELETE CASCADE
);

-- Table: guestRes
-- Bridge table
CREATE TABLE GuestRes (
	ResId int NOT NULL,
	GuestId int NOT NULL,
    
    foreign key fk_GuestRes_ResId (ResId)
		references Reservation(ResId) ON DELETE CASCADE,
	foreign key fk_GuestRes_GuestId (GuestId)
		references Guest(GuestId) ON DELETE CASCADE
);

