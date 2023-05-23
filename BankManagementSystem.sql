use master
Drop database BankManagementSystem
CREATE DATABASE BankManagementSystem
 
CREATE TABLE Bank (
	BankName varchar(15),
	Code varchar(10),
	BankAddress varchar(50),

	CONSTRAINT Bank_pk PRIMARY KEY (Code),
	CONSTRAINT Bank_uq Unique (BankName)
);

CREATE TABLE Branch (
	BranchNumber varchar(10),
	BranchAddress varchar(50),
	BankCode varchar(10) , 

	CONSTRAINT Branch_pk PRIMARY KEY (BranchNumber),
	constraint Branch_fk foreign key (BankCode) references Bank(Code)

);

CREATE TABLE Customer (
	CustomerName varchar(100) NOT NULL,
	SSN varchar(10),
	CustomerAddress varchar(50),
	Phone varchar(12),
	CustomerPassword varchar(15) NOT NULL, 
	BankCode varchar(10), 
	BranchCode varchar(10),
  
	CONSTRAINT Customer_pk PRIMARY KEY (SSN
	                                   ),
	constraint CustomerBranch_fk foreign key (BranchCode) references Branch(BranchNumber), 
	constraint CustomerBank_fk foreign key (BankCode) references Bank(Code), 
	CONSTRAINT Customer_uq Unique (Phone)
);

CREATE TABLE Employee (
	EmployeeName varchar(15),
	SSN varchar(10),
	EmployeePassword varchar(15),
	AccessLevel varchar(10),
	BankCode varchar(10), 
	BranchCode varchar(10),

	constraint EmployeeBranch_fk foreign key (BranchCode) references Branch(BranchNumber), 
	constraint EmployeeBank_fk foreign key (BankCode) references Bank(Code), 
	CONSTRAINT Employee_pk PRIMARY KEY (SSN)
);

CREATE TABLE Account (
	 AccountType varchar(15),
	 Number varchar(17),
	 Balance float,
	 CustomerSSN varchar(10), 
	 EmployeeID varchar(10), 

	 Constraint AccountCustomer_FK foreign key (CustomerSSN) references Customer (SSN), 
	 Constraint AccountEmp_FK foreign key (EmployeeID) references Employee(SSN) ,
	 CONSTRAINT Account_pk PRIMARY KEY (Number),
);



CREATE TABLE Loan (
	LoanType varchar(15),
	Number varchar(15),
	Balance float,
	LoanStatus varchar(15),
	EmployeeSSN varchar(10), 
	CustomerSSN varchar( 10),

	Constraint LoanEmp_FK foreign key (EmployeeSSN) references Employee(SSN),
	Constraint LoanCustomer_FK foreign key (CustomerSSN) references Customer (SSN), 

	CONSTRAINT Loan_pk PRIMARY KEY (Number)
);
