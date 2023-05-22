use master
Drop database BankManagementSystem
CREATE DATABASE BankManagementSystem
 
CREATE TABLE Bank (
	Name varchar(15),
	Code varchar(10),
	Address varchar(50),

	CONSTRAINT Bank_pk PRIMARY KEY (Code),
	CONSTRAINT Bank_uq Unique (Name)
);

CREATE TABLE Branch (
	Number varchar(10),
	Address varchar(50),
	BankCode varchar(10), 

	CONSTRAINT Branch_pk PRIMARY KEY (Number),
	CONSTRAINT Branch_fk foreign key (BankCode) references Bank(Code)

);

CREATE TABLE Customer (
	Name varchar(100) NOT NULL,
	SSN varchar(10),
	Address varchar(50),
	Phone varchar(12),
	Password varchar(15) NOT NULL, 
	BankCode varchar(10), 
	BranchCode varchar(10),
  
	CONSTRAINT Customer_pk PRIMARY KEY (SSN),
	CONSTRAINT CustomerBranch_fk foreign key (BranchCode) references Branch(Number), 
	CONSTRAINT CustomerBank_fk foreign key (BankCode) references Bank(Code), 
	CONSTRAINT Customer_uq Unique (Phone)
);

CREATE TABLE Employee (
	Name varchar(15),
	SSN varchar(10),
	Password varchar(15),
	AccessLevel varchar(10),
	BankCode varchar(10), 
	BranchCode varchar(10),

	CONSTRAINT EmployeeBranch_fk foreign key (BranchCode) references Branch(Number), 
	CONSTRAINT EmployeeBank_fk foreign key (BankCode) references Bank(Code), 
	CONSTRAINT Employee_pk PRIMARY KEY (SSN)
);

CREATE TABLE Account (
	 AccountType varchar(15),
	 Number varchar(17),
	 Balance float,
	 CustomerSSN varchar(10), 
	 EmployeeID varchar(10), 

	 CONSTRAINT AccountCustomer_FK Foreign KEY (CustomerSSN) references Customer (SSN), 
	 CONSTRAINT AccountEmp_FK Foreign KEY (EmployeeID) references Employee(SSN),
	 CONSTRAINT Account_pk PRIMARY KEY (Number)
);



CREATE TABLE Loan (
	Type varchar(15),
	Number varchar(15),
	Balance float,
	Status varchar(15),
	EmployeeSSN varchar(10), 
	CustomerSSN varchar(10),

	CONSTRAINT LoanEmp_FK FOREIGN KEY (EmployeeSSN) references Employee(SSN),
	CONSTRAINT LoanCustomer_FK FOREIGN KEY (CustomerSSN) references Customer (SSN), 
	CONSTRAINT Loan_pk PRIMARY KEY (Number) 
);
