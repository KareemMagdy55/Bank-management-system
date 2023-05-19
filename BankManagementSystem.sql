CREATE DATABASE BankManagementSystem
 
CREATE TABLE Bank (
	Name varchar(15),
	Code varchar(4),
	Adress varchar(50),

	CONSTRAINT Bank_pk PRIMARY KEY (Code),
	CONSTRAINT Bank_uq Unique (Name)
);

CREATE TABLE Branch (
	BranchNumber int,
	CONSTRAINT Branch_pk PRIMARY KEY (BranchNumber)
);

CREATE TABLE Customer (
	Name varchar(15) NOT NULL,
	SSN varchar(9),
	Adress varchar(50),
	Phone varchar(12),
	Password varchar(15) NOT NULL, 
  
	CONSTRAINT Customer_pk PRIMARY KEY (SSN),
	CONSTRAINT Customer_uq Unique (Phone)
);

CREATE TABLE Account (
	 Type varchar(15),
	 Number varchar(17),
	 Balance float,

	 CONSTRAINT Account_pk PRIMARY KEY (Number),
);

CREATE TABLE Employee (
	Name varchar(15),
	SSN varchar(9),
	Password varchar(15),
	AccessLevel int,

	CONSTRAINT Employee_pk PRIMARY KEY (SSN),
);

CREATE TABLE Loan (
	Type varchar(15),
	Number varchar(15),
	Balance float,

	CONSTRAINT Loan_pk PRIMARY KEY (Number)
);