use master
DROP DATABASE BankManagementSystem
CREATE DATABASE BankManagementSystem

CREATE TABLE Bank (
    Name varchar(15),
    Code varchar(10),
    Address varchar(50),

    CONSTRAINT Bank_pk PRIMARY KEY (Code),
    CONSTRAINT Bank_uq UNIQUE (Name)
);

CREATE TABLE Branch (
    Number varchar(10),
    Address varchar(50),
    BankCode varchar(10),

    CONSTRAINT Branch_pk PRIMARY KEY (Number),
    CONSTRAINT Branch_fk FOREIGN KEY (BankCode) REFERENCES Bank(Code)
);

CREATE TABLE Employee (
    Name varchar(15),
    SSN varchar(10),
    Password varchar(15),
    AccessLevel int,
    BankCode varchar(10),
    BranchCode varchar(10),

    CONSTRAINT EmployeeBranch_fk FOREIGN KEY (BranchCode) REFERENCES Branch(Number),
    CONSTRAINT EmployeeBank_fk FOREIGN KEY (BankCode) REFERENCES Bank(Code),
    CONSTRAINT Employee_pk PRIMARY KEY (SSN)
);

CREATE TABLE Admin (
    Name varchar(15),
    SSN varchar(10),
    Password varchar(15),

    CONSTRAINT Admin_PK PRIMARY KEY (SSN)
);

CREATE TABLE Account (
    AccountType varchar(15),
    Number varchar(17),
    Balance float,
    CustomerSSN varchar(10),
    EmployeeID varchar(10),

    CONSTRAINT Account_pk PRIMARY KEY (Number),
    CONSTRAINT AccountCustomer_FK FOREIGN KEY (CustomerSSN) REFERENCES Customer(SSN),
    CONSTRAINT AccountEmp_FK FOREIGN KEY (EmployeeID) REFERENCES Employee(SSN)
);

CREATE TABLE Customer (
    Name varchar(100) NOT NULL,
    SSN varchar(10),
    Address varchar(50),
    Phone varchar(12),
    Password varchar(15) NOT NULL,
    BankCode varchar(10),
    BranchCode varchar(10),
    AccountNumber varchar(17),

    CONSTRAINT Customer_pk PRIMARY KEY (SSN),
    CONSTRAINT CustomerBranch_fk FOREIGN KEY (BranchCode) REFERENCES Branch(Number),
    CONSTRAINT CustomerBank_fk FOREIGN KEY (BankCode) REFERENCES Bank(Code),
    CONSTRAINT Customer_uq UNIQUE (Phone)
);

CREATE TABLE Loan (
    Type varchar(15),
    Number int,
    Balance float,
    Status varchar(15),
    EmployeeSSN varchar(10),
    CustomerSSN varchar(10),

    CONSTRAINT LoanEmp_FK FOREIGN KEY (EmployeeSSN) REFERENCES Employee(SSN),
    CONSTRAINT LoanCustomer_FK FOREIGN KEY (CustomerSSN) REFERENCES Customer (SSN),
    CONSTRAINT Loan_pk PRIMARY KEY (Number)
);
