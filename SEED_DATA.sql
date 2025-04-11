CREATE TABLE users (
    user_id nvarchar(255) PRIMARY KEY ,
    title  nvarchar(10) NOT NULL,
    user_name VARCHAR(100) NOT NULL,
    surname nvarchar (100) NOT NULL,
    id_number  nvarchar (13) NOT NULL,
    dob DATE NOT NULL,
    gender  nvarchar(10) NOT NULL,
    phone_no nvarchar(30) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    );



 CREATE TABLE payment_details (
    payment_details_id nvarchar(255) PRIMARY KEY,
    user_id nvarchar(255) NOT NULL,
    monthly_payment_day INT NOT NULL,
    card_number NVARCHAR(4) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE vehicles (
    vehicle_id nvarchar(255) PRIMARY KEY,
    user_id nvarchar(255) NOT NULL,
    make NVARCHAR(100) NOT NULL,
    model NVARCHAR(100) NOT NULL,
    year INT NOT NULL,
    license_plate NVARCHAR(20) UNIQUE NOT NULL,
    vin NVARCHAR(17) UNIQUE NOT NULL,
    current_mileage int NOT NULL,
    purchase_date DATE NOT NULL,
    estimated_current_value DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE policies (
    policy_id nvarchar(255) PRIMARY KEY,
    user_id nvarchar(255) NOT NULL,
    vehicle_id nvarchar(255) NOT NULL,
    policy_number NVARCHAR(50) UNIQUE NOT NULL,
    start_date DATE NOT NULL,
    premium DECIMAL(10,2) NOT NULL,
    coverage_type NVARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);


CREATE TABLE claims (
    claim_id nvarchar(255) PRIMARY KEY,
    policy_id nvarchar(255) NOT NULL,
    user_id nvarchar(255) NOT NULL,
    incident nvarchar(50) NOT NULL,
    incident_date DATE NOT NULL,
    claim_amount DECIMAL(10,2),
    claim_status nvarchar(40) DEFAULT 'Pending',
    description nvarchar(max),
    claim_duration VARCHAR(255) DEFAULT 'Not Available',
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE documents (
    document_id  Nvarchar(255) PRIMARY KEY,
    claim_id nvarchar (255) NOT NULL,
    images nvarchar(max) NOT NULL,
    affidavit  nvarchar (255) NOT NULL,
    police_report nvarchar (255) NOT NULL,
    FOREIGN KEY (claim_id) REFERENCES claims(claim_id)
);

CREATE TABLE recent_activity (
    id VARCHAR(255) PRIMARY KEY,
    activity VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT GETUTCDATE(),
);

INSERT INTO users (
    user_id, title, user_name, surname, id_number, dob, gender,
    phone_no, email, password_hash, address
)
VALUES (
    '9424e7c5-d49f-4490-aa23-68ed13168c30',
    'Mr',
    'Jack',
    'Smith',
    '1234567891238',
    '2000-09-12',
    'Male',
    '0736248869',
    'Jack_Deso@gmail.com',
    'scrypt:32768:8:1$0Y83Ta8ROu2sNKIE$a418c7bad6af029b8ba396ba2e1e2b3539c608b14d551ed150e4960c73341e455c2f522340ebe0349abcbd2d535ffd384100298badf941cc9a26e1de20b6e723',
    '123 main Street'
);


INSERT INTO users (
    user_id, title, user_name, surname, id_number, dob, gender,
    phone_no, email, password_hash, address
)
VALUES (
    '855e4568-e45f-438a-a814-84512bf85b98',
    'Mr',
    'Admin',
    'Admin',
    '5555555555555',
    '2000-06-12',
    'Male',
    '1234567893',
    'admin@gmail.com',
    'scrypt:32768:8:1$qrDZIAskxyTumAPO$a97046df843770e3b409bd626f94a4608f22d44cb7d18316fe35a6565e95f511d535d666a5f4394614c6805929035e95e07be5026e39942646da3d91c49040ab',
    '123 main Street'
);




-- Insert into users
INSERT INTO users VALUES
('U001', 'Mr', 'John', 'Smith', '9001011234567', '1990-01-01', 'Male', '0812345678', 'john.smith@example.com', 'hash123', '123 Main St'),
('U002', 'Ms', 'Sarah', 'Brown', '9202022345678', '1992-02-02', 'Female', '0823456789', 'sarah.brown@example.com', 'hash456', '456 Second St'),
('U003', 'Mrs', 'Alice', 'Johnson', '8803033456789', '1988-03-03', 'Female', '0834567890', 'alice.j@example.com', 'hash789', '789 Third St'),
('U004', 'Mr', 'David', 'Lee', '9304044567890', '1993-04-04', 'Male', '0845678901', 'david.lee@example.com', 'hash101', '321 Fourth St'),
('U005', 'Dr', 'James', 'Wilson', '8505055678901', '1985-05-05', 'Male', '0856789012', 'james.w@example.com', 'hash202', '654 Fifth Ave'),
('U006', 'Mr', 'Mike', 'Taylor', '8706066789012', '1987-06-06', 'Male', '0867890123', 'mike.t@example.com', 'hash303', '987 Sixth Blvd'),
('U007', 'Ms', 'Linda', 'White', '8907077890123', '1989-07-07', 'Female', '0878901234', 'linda.w@example.com', 'hash404', '111 Seventh Rd'),
('U008', 'Mr', 'Tom', 'Clark', '9108088901234', '1991-08-08', 'Male', '0889012345', 'tom.clark@example.com', 'hash505', '222 Eighth Dr'),
('U009', 'Mrs', 'Rachel', 'Hall', '9409099012345', '1994-09-09', 'Female', '0890123456', 'rachel.h@example.com', 'hash606', '333 Ninth St'),
('U010', 'Dr', 'Chris', 'Evans', '8601010123456', '1986-01-01', 'Male', '0801234567', 'chris.evans@example.com', 'hash707', '444 Tenth Ave');

-- Insert into payment_details
INSERT INTO payment_details VALUES
('PD001', 'U001', 1, '1234'),
('PD002', 'U002', 2, '2345'),
('PD003', 'U003', 3, '3456'),
('PD004', 'U004', 4, '4567'),
('PD005', 'U005', 5, '5678'),
('PD006', 'U006', 6, '6789'),
('PD007', 'U007', 7, '7890'),
('PD008', 'U008', 8, '8901'),
('PD009', 'U009', 9, '9012'),
('PD010', 'U010', 10, '0123');

-- Insert into vehicles
INSERT INTO vehicles VALUES
('V001', 'U001', 'Toyota', 'Corolla', 2015, 'CA12345', 'VIN00001', 75000, '2015-06-01', 120000.00),
('V002', 'U002', 'Honda', 'Civic', 2017, 'CJ23456', 'VIN00002', 60000, '2017-07-15', 140000.00),
('V003', 'U003', 'Ford', 'Fiesta', 2014, 'CK34567', 'VIN00003', 80000, '2014-05-10', 100000.00),
('V004', 'U004', 'BMW', '320i', 2018, 'CL45678', 'VIN00004', 40000, '2018-09-20', 210000.00),
('V005', 'U005', 'Audi', 'A4', 2019, 'CA56789', 'VIN00005', 35000, '2019-03-22', 250000.00),
('V006', 'U006', 'Nissan', 'Micra', 2013, 'CB67890', 'VIN00006', 90000, '2013-02-12', 85000.00),
('V007', 'U007', 'Mazda', '3', 2016, 'CC78901', 'VIN00007', 70000, '2016-11-05', 130000.00),
('V008', 'U008', 'Chevrolet', 'Spark', 2012, 'CD89012', 'VIN00008', 95000, '2012-01-17', 60000.00),
('V009', 'U009', 'Hyundai', 'i20', 2020, 'CE90123', 'VIN00009', 20000, '2020-06-11', 180000.00),
('V010', 'U010', 'Kia', 'Rio', 2021, 'CF01234', 'VIN00010', 15000, '2021-08-19', 190000.00);

-- Insert into policies
INSERT INTO policies VALUES
('P001', 'U001', 'V001', 'POL1001', '2022-01-01', 500.00, 'Comprehensive'),
('P002', 'U002', 'V002', 'POL1002', '2022-02-01', 450.00, 'Third Party'),
('P003', 'U003', 'V003', 'POL1003', '2022-03-01', 400.00, 'Comprehensive'),
('P004', 'U004', 'V004', 'POL1004', '2022-04-01', 550.00, 'Third Party Fire & Theft'),
('P005', 'U005', 'V005', 'POL1005', '2022-05-01', 600.00, 'Comprehensive'),
('P006', 'U006', 'V006', 'POL1006', '2022-06-01', 420.00, 'Third Party'),
('P007', 'U007', 'V007', 'POL1007', '2022-07-01', 480.00, 'Comprehensive'),
('P008', 'U008', 'V008', 'POL1008', '2022-08-01', 390.00, 'Third Party'),
('P009', 'U009', 'V009', 'POL1009', '2022-09-01', 520.00, 'Comprehensive'),
('P010', 'U010', 'V010', 'POL1010', '2022-10-01', 610.00, 'Third Party Fire & Theft');

-- Insert into claims
INSERT INTO claims VALUES
('C001', 'P001', 'U001', 'Accident', '2023-01-10', 10000.00, 'Approved', 'Rear-end collision', '10 days'),
('C002', 'P002', 'U002', 'Theft', '2023-02-12', 15000.00, 'Rejected', 'Stolen vehicle', '5 days'),
('C003', 'P003', 'U003', 'Hail Damage', '2023-03-20', 3000.00, 'Pending', 'Hailstorm damage to roof', 'Not Available'),
('C004', 'P004', 'U004', 'Fire', '2023-04-15', 20000.00, 'Approved', 'Engine fire', '12 days'),
('C005', 'P005', 'U005', 'Flood', '2023-05-22', 12000.00, 'In Review', 'Flooded during heavy rain', '7 days'),
('C006', 'P006', 'U006', 'Accident', '2023-06-30', 8000.00, 'Approved', 'Hit a pole', '6 days'),
('C007', 'P007', 'U007', 'Theft', '2023-07-25', 9000.00, 'Pending', 'Stolen radio', 'Not Available'),
('C008', 'P008', 'U008', 'Accident', '2023-08-14', 11000.00, 'Rejected', 'Minor fender bender', '4 days'),
('C009', 'P009', 'U009', 'Fire', '2023-09-18', 13000.00, 'In Review', 'Electrical fire', '9 days'),
('C010', 'P010', 'U010', 'Theft', '2023-10-05', 16000.00, 'Approved', 'Vehicle theft', '8 days');

-- Insert into documents
INSERT INTO documents VALUES
('D001', 'C001', 'img001.jpg', 'affidavit001.pdf', 'police001.pdf'),
('D002', 'C002', 'img002.jpg', 'affidavit002.pdf', 'police002.pdf'),
('D003', 'C003', 'img003.jpg', 'affidavit003.pdf', 'police003.pdf'),
('D004', 'C004', 'img004.jpg', 'affidavit004.pdf', 'police004.pdf'),
('D005', 'C005', 'img005.jpg', 'affidavit005.pdf', 'police005.pdf'),
('D006', 'C006', 'img006.jpg', 'affidavit006.pdf', 'police006.pdf'),
('D007', 'C007', 'img007.jpg', 'affidavit007.pdf', 'police007.pdf'),
('D008', 'C008', 'img008.jpg', 'affidavit008.pdf', 'police008.pdf'),
('D009', 'C009', 'img009.jpg', 'affidavit009.pdf', 'police009.pdf'),
('D010', 'C010', 'img010.jpg', 'affidavit010.pdf', 'police010.pdf');

-- Insert into recent_activity
INSERT INTO recent_activity VALUES
('A001', 'User U001 filed claim C001', GETUTCDATE()),
('A002', 'User U002 filed claim C002', GETUTCDATE()),
('A003', 'User U003 filed claim C003', GETUTCDATE()),
('A004', 'User U004 filed claim C004', GETUTCDATE()),
('A005', 'User U005 filed claim C005', GETUTCDATE()),
('A006', 'User U006 filed claim C006', GETUTCDATE()),
('A007', 'User U007 filed claim C007', GETUTCDATE()),
('A008', 'User U008 filed claim C008', GETUTCDATE()),
('A009', 'User U009 filed claim C009', GETUTCDATE()),
('A010', 'User U010 filed claim C010', GETUTCDATE());




INSERT INTO users (user_id, title, user_name, surname, id_number, dob, gender, phone_no, email, password_hash, address) VALUES
('u11', 'Mr', 'Thabo', 'Nkosi', '9401025800083', '1994-01-02', 'Male', '0836000001', 'thabo.nkosi@example.com', 'hashed11', '111 Oak Lane'),
('u12', 'Mrs', 'Nandi', 'Dlamini', '9203054700084', '1992-03-05', 'Female', '0836000002', 'nandi.dlamini@example.com', 'hashed12', '112 Oak Lane'),
('u13', 'Ms', 'Kea', 'Molefe', '8807035200085', '1988-07-03', 'Female', '0836000003', 'kea.molefe@example.com', 'hashed13', '113 Oak Lane'),
('u14', 'Dr', 'Lesego', 'Khoza', '8501055600086', '1985-01-05', 'Male', '0836000004', 'lesego.khoza@example.com', 'hashed14', '114 Oak Lane'),
('u15', 'Mr', 'Simon', 'Peters', '9102085800087', '1991-02-08', 'Male', '0836000005', 'simon.peters@example.com', 'hashed15', '115 Oak Lane'),
('u16', 'Miss', 'Tumi', 'Mokoena', '9706096200088', '1997-06-09', 'Female', '0836000006', 'tumi.mokoena@example.com', 'hashed16', '116 Oak Lane'),
('u17', 'Mr', 'Kabelo', 'Zulu', '9307015900089', '1993-07-01', 'Male', '0836000007', 'kabelo.zulu@example.com', 'hashed17', '117 Oak Lane'),
('u18', 'Ms', 'Refilwe', 'Maphoto', '9001015000090', '1990-01-01', 'Female', '0836000008', 'refilwe.maphoto@example.com', 'hashed18', '118 Oak Lane'),
('u19', 'Mr', 'Sizwe', 'Gumede', '8904065300091', '1989-04-06', 'Male', '0836000009', 'sizwe.gumede@example.com', 'hashed19', '119 Oak Lane'),
('u20', 'Mrs', 'Lerato', 'Matlala', '8608075400092', '1986-08-07', 'Female', '0836000010', 'lerato.matlala@example.com', 'hashed20', '120 Oak Lane'),
('u21', 'Ms', 'Nthabiseng', 'Moloi', '9501015800093', '1995-01-01', 'Female', '0836000011', 'nthabi.moloi@example.com', 'hashed21', '121 Oak Lane'),
('u22', 'Mr', 'Gift', 'Motsoeneng', '9102045900094', '1991-02-04', 'Male', '0836000012', 'gift.motso@example.com', 'hashed22', '122 Oak Lane'),
('u23', 'Miss', 'Bonolo', 'Selepe', '9308035600095', '1993-08-03', 'Female', '0836000013', 'bonolo.selepe@example.com', 'hashed23', '123 Oak Lane'),
('u24', 'Mr', 'Tshepo', 'Madiba', '8704015100096', '1987-04-01', 'Male', '0836000014', 'tshepo.madiba@example.com', 'hashed24', '124 Oak Lane'),
('u25', 'Mrs', 'Nomsa', 'Nhlapo', '9202014700097', '1992-02-01', 'Female', '0836000015', 'nomsa.nhlapo@example.com', 'hashed25', '125 Oak Lane'),
('u26', 'Dr', 'Mandla', 'Mahlangu', '8406025700098', '1984-06-02', 'Male', '0836000016', 'mandla.mahlangu@example.com', 'hashed26', '126 Oak Lane'),
('u27', 'Mr', 'Andile', 'Ngcobo', '9607116100099', '1996-07-11', 'Male', '0836000017', 'andile.ngcobo@example.com', 'hashed27', '127 Oak Lane'),
('u28', 'Ms', 'Palesa', 'Motlhabane', '9809026300100', '1998-09-02', 'Female', '0836000018', 'palesa.m@example.com', 'hashed28', '128 Oak Lane'),
('u29', 'Mr', 'Bongani', 'Majola', '8701035200101', '1987-01-03', 'Male', '0836000019', 'bongani.majola@example.com', 'hashed29', '129 Oak Lane'),
('u30', 'Mrs', 'Zanele', 'Ntuli', '9402085800102', '1994-02-08', 'Female', '0836000020', 'zanele.ntuli@example.com', 'hashed30', '130 Oak Lane');


INSERT INTO payment_details (payment_details_id, user_id, monthly_payment_day, card_number) VALUES
('p11', 'u11', 5, '1111'),
('p12', 'u12', 10, '2222'),
('p13', 'u13', 12, '3333'),
('p14', 'u14', 8, '4444'),
('p15', 'u15', 25, '5555'),
('p16', 'u16', 14, '6666'),
('p17', 'u17', 19, '7777'),
('p18', 'u18', 30, '8888'),
('p19', 'u19', 7, '9999'),
('p20', 'u20', 11, '1010'),
('p21', 'u21', 9, '1112'),
('p22', 'u22', 15, '1213'),
('p23', 'u23', 28, '1314'),
('p24', 'u24', 3, '1415'),
('p25', 'u25', 6, '1516'),
('p26', 'u26', 2, '1617'),
('p27', 'u27', 20, '1718'),
('p28', 'u28', 13, '1819'),
('p29', 'u29', 26, '1920'),
('p30', 'u30', 4, '2021');



INSERT INTO vehicles (vehicle_id, user_id, make, model, year, license_plate, vin, current_mileage, purchase_date, estimated_current_value) VALUES
('v11', 'u11', 'Toyota', 'Corolla', 2017, 'CA11111', '1HGCM82633A001111', 87000, '2017-03-12', 98000.00),
('v12', 'u12', 'Honda', 'Civic', 2019, 'CA22222', '1HGCM82633A002222', 56000, '2019-06-18', 125000.00),
('v13', 'u13', 'Ford', 'Focus', 2020, 'CA33333', '1HGCM82633A003333', 41000, '2020-11-23', 148000.00),
('v14', 'u14', 'VW', 'Polo', 2015, 'CA44444', '1HGCM82633A004444', 99000, '2015-04-10', 87000.00),
('v15', 'u15', 'Hyundai', 'i20', 2016, 'CA55555', '1HGCM82633A005555', 94000, '2016-09-19', 89000.00),
('v16', 'u16', 'Nissan', 'Micra', 2014, 'CA66666', '1HGCM82633A006666', 101000, '2014-07-08', 69000.00),
('v17', 'u17', 'Mazda', 'CX-3', 2018, 'CA77777', '1HGCM82633A007777', 67000, '2018-12-01', 110000.00),
('v18', 'u18', 'Kia', 'Picanto', 2021, 'CA88888', '1HGCM82633A008888', 22000, '2021-05-30', 155000.00),
('v19', 'u19', 'Renault', 'Clio', 2013, 'CA99999', '1HGCM82633A009999', 118000, '2013-02-15', 45000.00),
('v20', 'u20', 'Suzuki', 'Swift', 2022, 'CA00001', '1HGCM82633A010000', 15000, '2022-10-10', 165000.00),
('v21', 'u21', 'Toyota', 'Yaris', 2016, 'CA00002', '1HGCM82633A010001', 73000, '2016-01-03', 81000.00),
('v22', 'u22', 'VW', 'Golf', 2020, 'CA00003', '1HGCM82633A010002', 47000, '2020-09-09', 140000.00),
('v23', 'u23', 'Hyundai', 'Creta', 2021, 'CA00004', '1HGCM82633A010003', 33000, '2021-06-20', 160000.00),
('v24', 'u24', 'Ford', 'Fiesta', 2017, 'CA00005', '1HGCM82633A010004', 78000, '2017-11-27', 97000.00),
('v25', 'u25', 'Nissan', 'Qashqai', 2019, 'CA00006', '1HGCM82633A010005', 59000, '2019-03-13', 128000.00),
('v26', 'u26', 'Honda', 'Jazz', 2015, 'CA00007', '1HGCM82633A010006', 86000, '2015-08-14', 73000.00),
('v27', 'u27', 'Toyota', 'Avanza', 2018, 'CA00008', '1HGCM82633A010007', 64000, '2018-05-19', 115000.00),
('v28', 'u28', 'Suzuki', 'Baleno', 2022, 'CA00009', '1HGCM82633A010008', 12000, '2022-01-15', 172000.00),
('v29', 'u29', 'Mazda', '2', 2016, 'CA00010', '1HGCM82633A010009', 91000, '2016-12-05', 86000.00),
('v30', 'u30', 'Kia', 'Rio', 2019, 'CA00011', '1HGCM82633A010010', 58000, '2019-07-07', 123000.00);


INSERT INTO policies (policy_id, user_id, vehicle_id, policy_number, start_date, premium, coverage_type) VALUES
('pol11', 'u11', 'v11', 'PN1111', '2022-01-01', 850.00, 'Comprehensive'),
('pol12', 'u12', 'v12', 'PN2222', '2022-02-01', 920.00, 'Comprehensive'),
('pol13', 'u13', 'v13', 'PN3333', '2022-03-01', 880.00, 'Third Party'),
('pol14', 'u14', 'v14', 'PN4444', '2021-05-01', 700.00, 'Comprehensive'),
('pol15', 'u15', 'v15', 'PN5555', '2021-06-01', 790.00, 'Comprehensive'),
('pol16', 'u16', 'v16', 'PN6666', '2020-07-01', 660.00, 'Third Party'),
('pol17', 'u17', 'v17', 'PN7777', '2021-08-01', 880.00, 'Comprehensive'),
('pol18', 'u18', 'v18', 'PN8888', '2022-10-01', 980.00, 'Comprehensive'),
('pol19', 'u19', 'v19', 'PN9999', '2019-03-01', 600.00, 'Third Party'),
('pol20', 'u20', 'v20', 'PN0001', '2023-01-01', 1020.00, 'Comprehensive'),
('pol21', 'u21', 'v21', 'PN0002', '2021-01-01', 770.00, 'Comprehensive'),
('pol22', 'u22', 'v22', 'PN0003', '2022-03-01', 950.00, 'Third Party'),
('pol23', 'u23', 'v23', 'PN0004', '2022-06-01', 870.00, 'Comprehensive'),
('pol24', 'u24', 'v24', 'PN0005', '2021-11-01', 710.00, 'Comprehensive'),
('pol25', 'u25', 'v25', 'PN0006', '2020-03-01', 850.00, 'Third Party'),
('pol26', 'u26', 'v26', 'PN0007', '2021-08-01', 690.00, 'Comprehensive'),
('pol27', 'u27', 'v27', 'PN0008', '2021-05-01', 920.00, 'Comprehensive'),
('pol28', 'u28', 'v28', 'PN0009', '2023-01-01', 1080.00, 'Comprehensive'),
('pol29', 'u29', 'v29', 'PN0010', '2020-12-01', 750.00, 'Third Party'),
('pol30', 'u30', 'v30', 'PN0011', '2022-07-01', 940.00, 'Comprehensive');


INSERT INTO claims (claim_id, policy_id, user_id, incident, incident_date, claim_amount, claim_status, description, claim_duration) VALUES
('c11', 'pol11', 'u11', 'Accident', '2023-01-20', 12000.00, 'Approved', 'Rear-end collision', '10 days'),
('c12', 'pol12', 'u12', 'Theft', '2023-02-15', 15000.00, 'Pending', 'Car stereo stolen', 'Not Available'),
('c13', 'pol13', 'u13', 'Accident', '2023-03-10', 8000.00, 'Rejected', 'Hit a pole', '4 days'),
('c14', 'pol14', 'u14', 'Vandalism', '2022-05-12', 4500.00, 'Approved', 'Scratched paint', '3 days'),
('c15', 'pol15', 'u15', 'Fire', '2022-06-22', 22000.00, 'Pending', 'Engine fire', 'Not Available'),
('c16', 'pol16', 'u16', 'Flood', '2022-07-18', 18000.00, 'Approved', 'Interior damaged by water', '7 days'),
('c17', 'pol17', 'u17', 'Theft', '2023-08-01', 21000.00, 'Pending', 'Whole car stolen', 'Not Available'),
('c18', 'pol18', 'u18', 'Accident', '2023-09-05', 13000.00, 'Approved', 'Side collision', '6 days'),
('c19', 'pol19', 'u19', 'Accident', '2020-10-10', 7000.00, 'Approved', 'Minor bumper damage', '2 days'),
('c20', 'pol20', 'u20', 'Vandalism', '2023-11-20', 5500.00, 'Pending', 'Broken mirror', 'Not Available'),
('c21', 'pol21', 'u21', 'Accident', '2022-01-11', 12000.00, 'Approved', 'Fender bender', '5 days'),
('c22', 'pol22', 'u22', 'Theft', '2022-03-05', 9500.00, 'Rejected', 'Spare tire stolen', '2 days'),
('c23', 'pol23', 'u23', 'Fire', '2022-06-25', 16000.00, 'Approved', 'Electrical fire', '6 days'),
('c24', 'pol24', 'u24', 'Accident', '2022-11-13', 8700.00, 'Pending', 'Rear-ended by another driver', 'Not Available'),
('c25', 'pol25', 'u25', 'Flood', '2021-03-07', 14000.00, 'Approved', 'Heavy rain damage', '5 days'),
('c26', 'pol26', 'u26', 'Vandalism', '2021-08-14', 4300.00, 'Approved', 'Keyed paint', '2 days'),
('c27', 'pol27', 'u27', 'Accident', '2021-05-10', 12300.00, 'Approved', 'Crashed into pole', '7 days'),
('c28', 'pol28', 'u28', 'Theft', '2023-01-17', 17500.00, 'Pending', 'Laptop stolen from car', 'Not Available'),
('c29', 'pol29', 'u29', 'Accident', '2020-12-03', 9200.00, 'Approved', 'Side panel damage', '3 days'),
('c30', 'pol30', 'u30', 'Fire', '2022-07-20', 15500.00, 'Rejected', 'Engine fire due to fault', '6 days');



INSERT INTO documents (document_id, claim_id, images, affidavit, police_report) VALUES
('d11', 'c11', 'img11.jpg', 'aff11.pdf', 'rep11.pdf'),
('d12', 'c12', 'img12.jpg', 'aff12.pdf', 'rep12.pdf'),
('d13', 'c13', 'img13.jpg', 'aff13.pdf', 'rep13.pdf'),
('d14', 'c14', 'img14.jpg', 'aff14.pdf', 'rep14.pdf'),
('d15', 'c15', 'img15.jpg', 'aff15.pdf', 'rep15.pdf'),
('d16', 'c16', 'img16.jpg', 'aff16.pdf', 'rep16.pdf'),
('d17', 'c17', 'img17.jpg', 'aff17.pdf', 'rep17.pdf'),
('d18', 'c18', 'img18.jpg', 'aff18.pdf', 'rep18.pdf'),
('d19', 'c19', 'img19.jpg', 'aff19.pdf', 'rep19.pdf'),
('d20', 'c20', 'img20.jpg', 'aff20.pdf', 'rep20.pdf'),
('d21', 'c21', 'img21.jpg', 'aff21.pdf', 'rep21.pdf'),
('d22', 'c22', 'img22.jpg', 'aff22.pdf', 'rep22.pdf'),
('d23', 'c23', 'img23.jpg', 'aff23.pdf', 'rep23.pdf'),
('d24', 'c24', 'img24.jpg', 'aff24.pdf', 'rep24.pdf'),
('d25', 'c25', 'img25.jpg', 'aff25.pdf', 'rep25.pdf'),
('d26', 'c26', 'img26.jpg', 'aff26.pdf', 'rep26.pdf'),
('d27', 'c27', 'img27.jpg', 'aff27.pdf', 'rep27.pdf'),
('d28', 'c28', 'img28.jpg', 'aff28.pdf', 'rep28.pdf'),
('d29', 'c29', 'img29.jpg', 'aff29.pdf', 'rep29.pdf'),
('d30', 'c30', 'img30.jpg', 'aff30.pdf', 'rep30.pdf');

INSERT INTO recent_activity (id, activity, created_at) VALUES
('a11', 'Claim submitted by user u11', GETUTCDATE()),
('a12', 'Policy updated for user u12', GETUTCDATE()),
('a13', 'Document uploaded for claim c13', GETUTCDATE()),
('a14', 'Claim approved for user u14', GETUTCDATE()),
('a15', 'Payment processed for user u15', GETUTCDATE()),
('a16', 'New vehicle added by user u16', GETUTCDATE()),
('a17', 'Claim under review for user u17', GETUTCDATE()),
('a18', 'Document missing for claim c18', GETUTCDATE()),
('a19', 'Policy renewal started by u19', GETUTCDATE()),
('a20', 'User u20 updated address', GETUTCDATE()),
('a21', 'New vehicle added by u21', GETUTCDATE()),
('a22', 'Claim submitted by user u22', GETUTCDATE()),
('a23', 'Policy updated for user u23', GETUTCDATE()),
('a24', 'Claim approved for user u24', GETUTCDATE()),
('a25', 'Claim under review for user u25', GETUTCDATE()),
('a26', 'Claim rejected for user u26', GETUTCDATE()),
('a27', 'Claim submitted by user u27', GETUTCDATE()),
('a28', 'New policy created for user u28', GETUTCDATE()),
('a29', 'Payment failed for user u29', GETUTCDATE()),
('a30', 'Affidavit missing for claim c30', GETUTCDATE());
