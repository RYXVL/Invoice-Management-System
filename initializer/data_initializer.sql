USE ims;

INSERT IGNORE INTO Company (company_name, company_street_name, company_street_no, company_city, company_state, company_postal_code, company_country, company_email, company_phone_no)
VALUES 
('Alpha Dynamics', 'Pine Lane', 142, 'Riverton', 'AZ', '85001', 'USA', 'contact@alphadynamics.com', '4805556789'),
('BrightWave Solutions', 'Cedar Street', 58, 'Greenfield', 'WI', '53201', 'USA', 'info@brightwave.com', '4145552456'),
('NexGen Ventures', 'Birch Avenue', 73, 'Hillcrest', 'NV', '89001', 'USA', 'support@nexgen.com', '7025553390'),
('SkyLine Technologies', 'Willow Road', 310, 'Lakeside', 'MN', '55001', 'USA', 'hello@skyline.com', '6125557645'),
('EchoStar Innovations', 'Spruce Boulevard', 88, 'Brookfield', 'KY', '40004', 'USA', 'sales@echostar.com', '5025552837');

INSERT IGNORE INTO Employee (employee_user_name, employee_password, employee_id, employee_first_name, employee_last_name, employee_email, employee_phone_no, employee_hire_date, employee_street_name, employee_street_no, employee_city, employee_state, employee_postal_code, employee_country, company_id, is_admin)
VALUES 
('admin1', 'pass1234', 101, 'John', 'Doe', 'johndoe@example.com', '5551234567', '2023-01-10', 'Maple Street', 22, 'Riverdale', 'NY', '10001', 'USA', 1, TRUE),
('admin2', 'password', 102, 'Alice', 'Smith', 'alice.smith@example.com', '5552345678', '2022-05-16', 'Oak Avenue', 45, 'Greendale', 'CA', '90210', 'USA', 2, TRUE),
('admin3', 'adminpass', 103, 'Bob', 'Johnson', 'bob.j@example.com', '5553456789', '2021-09-25', 'Elm Drive', 78, 'Westfield', 'TX', '73301', 'USA', 3, TRUE),
('admin4', 'secure123', 104, 'Catherine', 'Brown', 'catherine.b@example.com', '5554567890', '2020-11-30', 'Cedar Road', 101, 'Lakeside', 'FL', '32003', 'USA', 4, TRUE),
('admin5', 'admin789', 105, 'David', 'Taylor', 'david.t@example.com', '5555678901', '2023-06-01', 'Pine Lane', 62, 'Hilltop', 'WA', '98001', 'USA', 5, TRUE),
('admin6', 'admin123', 111, 'Emma', 'Watson', 'emma.w@example.com', '5551122334', '2023-02-14', 'Chestnut Street', 14, 'Woodland', 'NY', '10002', 'USA', 1, TRUE),
('admin7', 'strongpass', 112, 'Oliver', 'Brown', 'oliver.b@example.com', '5552233445', '2023-05-01', 'Maple Drive', 54, 'Greenville', 'CA', '90211', 'USA', 2, TRUE),
('admin8', 'admin567', 113, 'Sophia', 'Taylor', 'sophia.t@example.com', '5553344556', '2022-08-20', 'Walnut Avenue', 23, 'Midtown', 'TX', '73302', 'USA', 3, TRUE),
('admin9', 'secure456', 114, 'Liam', 'Clark', 'liam.c@example.com', '5554455667', '2021-12-18', 'Oak Road', 76, 'Eastfield', 'FL', '32004', 'USA', 4, TRUE),
('admin10', 'adminsecure', 115, 'Isabella', 'Davis', 'isabella.d@example.com', '5555566778', '2023-09-30', 'Cedar Lane', 34, 'Hillcrest', 'WA', '98002', 'USA', 5, TRUE),
('user1', 'userpass1', 106, 'Michael', 'Green', 'michael.green@example.com', '5556789012', '2023-03-15', 'Birch Street', 30, 'Sunnyvale', 'CA', '94086', 'USA', 1, FALSE),
('user2', 'userpass2', 107, 'Laura', 'King', 'laura.king@example.com', '5557890123', '2022-07-22', 'Willow Avenue', 12, 'Mountain View', 'CA', '94043', 'USA', 2, FALSE),
('user3', 'userpass3', 108, 'Daniel', 'Lee', 'daniel.lee@example.com', '5558901234', '2021-10-10', 'Spruce Road', 55, 'Palo Alto', 'CA', '94301', 'USA', 3, FALSE),
('user4', 'userpass4', 109, 'Sarah', 'White', 'sarah.white@example.com', '5559012345', '2020-12-05', 'Fir Lane', 19, 'San Jose', 'CA', '95112', 'USA', 4, FALSE),
('user5', 'userpass5', 110, 'James', 'Wilson', 'james.wilson@example.com', '5550123456', '2023-08-01', 'Ash Boulevard', 88, 'Santa Clara', 'CA', '95050', 'USA', 5, FALSE),
('user6', 'userpass6', 116, 'Ethan', 'Harris', 'ethan.h@example.com', '5556677889', '2022-11-12', 'Birch Avenue', 11, 'Riverfield', 'NY', '10003', 'USA', 1, FALSE),
('user7', 'userpass7', 117, 'Ava', 'Clark', 'ava.c@example.com', '5557788990', '2021-06-18', 'Pine Drive', 27, 'Springfield', 'CA', '90212', 'USA', 2, FALSE),
('user8', 'userpass8', 118, 'Logan', 'Anderson', 'logan.a@example.com', '5558899001', '2023-04-21', 'Ash Street', 40, 'Lakeside', 'TX', '73303', 'USA', 3, FALSE),
('user9', 'userpass9', 119, 'Charlotte', 'Martinez', 'charlotte.m@example.com', '5559900112', '2022-02-25', 'Willow Road', 62, 'Hillview', 'FL', '32005', 'USA', 4, FALSE),
('user10', 'userpass10', 120, 'Henry', 'Thompson', 'henry.t@example.com', '5550011223', '2023-07-19', 'Elm Avenue', 36, 'Meadowfield', 'WA', '98003', 'USA', 5, FALSE),
('user11', 'userpass11', 121, 'Mia', 'Roberts', 'mia.roberts@example.com', '5551122339', '2022-09-01', 'Cypress Avenue', 13, 'Oakville', 'NY', '10004', 'USA', 1, FALSE),
('user12', 'userpass12', 122, 'Benjamin', 'Walker', 'benjamin.walker@example.com', '5552233455', '2023-02-15', 'Poplar Drive', 31, 'Crestfield', 'CA', '90213', 'USA', 2, FALSE),
('user13', 'userpass13', 123, 'Harper', 'Scott', 'harper.scott@example.com', '5553344559', '2021-12-05', 'Magnolia Lane', 67, 'Evergreen', 'TX', '73304', 'USA', 3, FALSE),
('user14', 'userpass14', 124, 'Elijah', 'Adams', 'elijah.adams@example.com', '5554455867', '2023-06-22', 'Palm Boulevard', 42, 'Brookfield', 'FL', '32006', 'USA', 4, FALSE),
('user15', 'userpass15', 125, 'Amelia', 'Baker', 'amelia.baker@example.com', '5555566779', '2022-01-12', 'Maple Avenue', 90, 'Shoreline', 'WA', '98004', 'USA', 5, FALSE);

INSERT IGNORE INTO Brand (brand_name) VALUES
('ErgoFurniture'),
('TechLife'),
('SoundScape'),
('SmartHome'),
('FitGear'),
('CleanAir'),
('LuxLight'),
('ProTools'),
('HealthyLiving'),
('HomeEssentials');

INSERT IGNORE INTO Product_Catalog (item_name, item_description, brand_id) VALUES
('Ultra Chair', 'Ergonomic office chair with adjustable height and lumbar support.', 1),
('Smart Desk', 'Electric adjustable standing desk with memory presets.', 1),
('Echo Laptop', 'Lightweight laptop with high-resolution display and long battery life.', 2),
('Power Bank', 'Portable charger with 20,000mAh capacity and fast-charging support.', 2),
('NoiseBuds', 'Wireless earbuds with active noise cancellation and water resistance.', 3),
('Galaxy Light', 'LED desk lamp with adjustable brightness and color temperature.', 7),
('Pro Backpack', 'Durable backpack with multiple compartments and USB charging port.', 6),
('SoundBar Pro', 'High-quality soundbar with surround sound and Bluetooth connectivity.', 3),
('Fit Tracker', 'Fitness tracker with heart rate monitoring and sleep tracking features.', 5),
('Smart Thermostat', 'WiFi-enabled thermostat with energy-saving features and app control.', 4),
('Air Purifier', 'HEPA air purifier for capturing allergens and improving air quality.', 6),
('Gaming Mouse', 'High-precision gaming mouse with customizable buttons and RGB lighting.', 2),
('Electric Kettle', 'Stainless steel kettle with rapid boiling and auto shut-off features.', 8),
('Wireless Charger', 'Fast wireless charging pad compatible with all Qi-enabled devices.', 2),
('Compact Fridge', 'Mini fridge with adjustable shelves and temperature control.', 9),
('Fitness Mat', 'Non-slip yoga mat with extra padding for comfort and stability.', 5),
('Portable Projector', 'Mini projector with HD display and built-in speakers.', 10),
('Home Blender', 'High-power blender with multiple speed settings and pulse function.', 9),
('Smart Lock', 'Keyless smart lock with remote access and activity monitoring.', 4),
('Water Filter', 'Under-sink water filter for clean and purified drinking water.', 6),
('Digital Frame', 'WiFi digital photo frame with HD display and cloud storage.', 10),
('Sleep Machine', 'Sound machine with various calming sounds and sleep timer.', 9),
('Vacuum Bot', 'Automatic vacuum cleaner with smart navigation and WiFi control.', 6),
('Electric Toothbrush', 'Rechargeable electric toothbrush with multiple brushing modes.', 5),
('Cordless Drill', 'Portable cordless drill with variable speed and battery indicator.', 8);

INSERT IGNORE INTO Customer (customer_user_name, customer_password, customer_id, customer_first_name, customer_last_name, customer_email, customer_phone_no, customer_street_name, customer_street_no, customer_city, customer_state, customer_postal_code, customer_country, company_id)
VALUES 
('cust1', 'custpass1', 201, 'Emma', 'Johnson', 'emma.johnson@example.com', '5551234567', 'Maple Street', 22, 'Riverdale', 'NY', '10001', 'USA', 1),
('cust2', 'custpass2', 202, 'Oliver', 'Williams', 'oliver.williams@example.com', '5552345678', 'Oak Avenue', 45, 'Greendale', 'CA', '90210', 'USA', 2),
('cust3', 'custpass3', 203, 'Sophia', 'Martinez', 'sophia.martinez@example.com', '5553456789', 'Elm Drive', 78, 'Westfield', 'TX', '73301', 'USA', 3),
('cust4', 'custpass4', 204, 'Liam', 'Brown', 'liam.brown@example.com', '5554567890', 'Cedar Road', 101, 'Lakeside', 'FL', '32003', 'USA', 4),
('cust5', 'custpass5', 205, 'Mia', 'Davis', 'mia.davis@example.com', '5555678901', 'Pine Lane', 62, 'Hilltop', 'WA', '98001', 'USA', 5),
('cust6', 'custpass6', 206, 'Noah', 'Miller', 'noah.miller@example.com', '5556789012', 'Birch Street', 30, 'Sunnyvale', 'CA', '94086', 'USA', 1),
('cust7', 'custpass7', 207, 'Ava', 'Taylor', 'ava.taylor@example.com', '5557890123', 'Willow Avenue', 12, 'Mountain View', 'CA', '94043', 'USA', 1),
('cust8', 'custpass8', 208, 'James', 'Anderson', 'james.anderson@example.com', '5558901234', 'Spruce Road', 55, 'Palo Alto', 'CA', '94301', 'USA', 1),
('cust9', 'custpass9', 209, 'Isabella', 'Thomas', 'isabella.thomas@example.com', '5559012345', 'Fir Lane', 19, 'San Jose', 'CA', '95112', 'USA', 1),
('cust10', 'custpass10', 210, 'Lucas', 'Moore', 'lucas.moore@example.com', '5551123456', 'Ash Boulevard', 88, 'Santa Clara', 'CA', '95050', 'USA', 2),
('cust11', 'custpass11', 211, 'Charlotte', 'Clark', 'charlotte.clark@example.com', '5552234567', 'Maple Avenue', 66, 'Oakland', 'CA', '94601', 'USA', 2),
('cust12', 'custpass12', 212, 'Elijah', 'Harris', 'elijah.harris@example.com', '5553345678', 'Cypress Lane', 34, 'Fremont', 'CA', '94536', 'USA', 2),
('cust13', 'custpass13', 213, 'Amelia', 'Martinez', 'amelia.martinez@example.com', '5554456789', 'Palm Road', 52, 'Hayward', 'CA', '94541', 'USA', 2),
('cust14', 'custpass14', 214, 'Ethan', 'Lee', 'ethan.lee@example.com', '5555567890', 'Magnolia Drive', 73, 'Austin', 'TX', '73344', 'USA', 3),
('cust15', 'custpass15', 215, 'Harper', 'King', 'harper.king@example.com', '5556678901', 'Poplar Street', 41, 'Dallas', 'TX', '75201', 'USA', 3),
('cust16', 'custpass16', 216, 'Logan', 'Walker', 'logan.walker@example.com', '5557789012', 'Birch Avenue', 29, 'San Antonio', 'TX', '78201', 'USA', 3),
('cust17', 'custpass17', 217, 'Aria', 'Scott', 'aria.scott@example.com', '5558890123', 'Pine Lane', 82, 'Houston', 'TX', '77001', 'USA', 3),
('cust18', 'custpass18', 218, 'Henry', 'White', 'henry.white@example.com', '5559901234', 'Cedar Boulevard', 57, 'Miami', 'FL', '33101', 'USA', 4),
('cust19', 'custpass19', 219, 'Ella', 'Adams', 'ella.adams@example.com', '5550012345', 'Willow Drive', 15, 'Orlando', 'FL', '32801', 'USA', 4),
('cust20', 'custpass20', 220, 'Samuel', 'Nelson', 'samuel.nelson@example.com', '5551123456', 'Elm Road', 25, 'Tampa', 'FL', '33601', 'USA', 4),
('cust21', 'custpass21', 221, 'Grace', 'Hill', 'grace.hill@example.com', '5552234567', 'Oak Boulevard', 61, 'Jacksonville', 'FL', '32099', 'USA', 4),
('cust22', 'custpass22', 222, 'Levi', 'Perez', 'levi.perez@example.com', '5553345678', 'Maple Street', 18, 'Seattle', 'WA', '98101', 'USA', 5),
('cust23', 'custpass23', 223, 'Scarlett', 'Reed', 'scarlett.reed@example.com', '5554456789', 'Pine Drive', 46, 'Spokane', 'WA', '99201', 'USA', 5),
('cust24', 'custpass24', 224, 'Mason', 'Young', 'mason.young@example.com', '5555567890', 'Cypress Lane', 63, 'Tacoma', 'WA', '98401', 'USA', 5),
('cust25', 'custpass25', 225, 'Luna', 'Evans', 'luna.evans@example.com', '5556678901', 'Willow Avenue', 36, 'Bellevue', 'WA', '98004', 'USA', 5);

INSERT IGNORE INTO Product (product_id, product_price, product_quantity, company_id, item_name, brand_id)
VALUES
(1, 149.99, 100, 1, 'Ultra Chair', 1),
(2, 299.99, 50, 1, 'Smart Desk', 1),
(3, 999.99, 30, 1, 'Echo Laptop', 2),
(4, 49.99, 200, 1, 'Power Bank', 2),
(5, 79.99, 150, 1, 'NoiseBuds', 3),
(1, 59.99, 75, 2, 'Galaxy Light', 7),
(2, 129.99, 40, 2, 'Pro Backpack', 6),
(3, 199.99, 20, 2, 'SoundBar Pro', 3),
(4, 59.99, 100, 2, 'Fit Tracker', 5),
(5, 199.99, 30, 2, 'Smart Thermostat', 4),
(1, 249.99, 50, 3, 'Air Purifier', 6),
(2, 49.99, 120, 3, 'Gaming Mouse', 2),
(3, 39.99, 90, 3, 'Electric Kettle', 8),
(4, 29.99, 60, 3, 'Wireless Charger', 2),
(5, 99.99, 80, 3, 'Compact Fridge', 9),
(1, 19.99, 110, 4, 'Fitness Mat', 5),
(2, 399.99, 10, 4, 'Portable Projector', 10),
(3, 99.99, 25, 4, 'Home Blender', 9),
(4, 249.99, 15, 4, 'Smart Lock', 4),
(5, 199.99, 40, 4, 'Water Filter', 6),
(1, 149.99, 55, 5, 'Digital Frame', 10),
(2, 49.99, 60, 5, 'Sleep Machine', 9),
(3, 299.99, 10, 5, 'Vacuum Bot', 6),
(4, 29.99, 100, 5, 'Electric Toothbrush', 5),
(5, 89.99, 70, 5, 'Cordless Drill', 8);

-- Stored Procedures
DELIMITER //
CREATE PROCEDURE FetchNotSoldProductsByACompany(IN company_id INT)
BEGIN
    SELECT pc.*, b.brand_name
    FROM product_catalog pc
    LEFT JOIN product p
    ON pc.item_name = p.item_name 
    AND pc.brand_id = p.brand_id 
    AND p.company_id = company_id
    JOIN brand b 
    ON pc.brand_id = b.brand_id
    WHERE p.company_id IS NULL;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetInvoicesOfACustomerOfACompany(IN company_id INT, IN customer_id INT)
BEGIN
    SELECT DISTINCT i.invoice_id, i.invoice_date
    FROM invoice i
    JOIN processes p
    ON i.invoice_id = p.invoice_id
    WHERE p.customer_id = customer_id 
    AND p.company_id = company_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateAllFieldsOfACompany(
    IN p_company_id INT,
    IN p_company_name VARCHAR(255),
    IN p_company_street_name VARCHAR(255),
    IN p_company_street_no VARCHAR(50),
    IN p_company_city VARCHAR(100),
    IN p_company_state VARCHAR(100),
    IN p_company_postal_code VARCHAR(20),
    IN p_company_country VARCHAR(100),
    IN p_company_email VARCHAR(255),
    IN p_company_phone_no VARCHAR(50)
)
BEGIN
    UPDATE Company 
    SET 
        company_name = p_company_name, 
        company_street_name = p_company_street_name, 
        company_street_no = p_company_street_no, 
        company_city = p_company_city, 
        company_state = p_company_state, 
        company_postal_code = p_company_postal_code, 
        company_country = p_company_country, 
        company_email = p_company_email, 
        company_phone_no = p_company_phone_no
    WHERE company_id = p_company_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertCustomer(
    IN p_customer_user_name VARCHAR(255),
    IN p_customer_password VARCHAR(255),
    IN p_customer_id INT,
    IN p_customer_first_name VARCHAR(255),
    IN p_customer_last_name VARCHAR(255),
    IN p_customer_email VARCHAR(255),
    IN p_customer_phone_no VARCHAR(50),
    IN p_customer_street_name VARCHAR(255),
    IN p_customer_street_no INT,
    IN p_customer_city VARCHAR(100),
    IN p_customer_state VARCHAR(100),
    IN p_customer_postal_code VARCHAR(20),
    IN p_customer_country VARCHAR(100),
    IN p_company_id INT
)
BEGIN
    INSERT INTO Customer (
        customer_user_name, 
        customer_password, 
        customer_id, 
        customer_first_name, 
        customer_last_name, 
        customer_email, 
        customer_phone_no, 
        customer_street_name, 
        customer_street_no, 
        customer_city, 
        customer_state, 
        customer_postal_code, 
        customer_country, 
        company_id
    ) 
    VALUES (
        p_customer_user_name, 
        p_customer_password, 
        p_customer_id, 
        p_customer_first_name, 
        p_customer_last_name, 
        p_customer_email, 
        p_customer_phone_no, 
        p_customer_street_name, 
        p_customer_street_no, 
        p_customer_city, 
        p_customer_state, 
        p_customer_postal_code, 
        p_customer_country, 
        p_company_id
    );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateAllFieldsOfACustomer(
    IN p_company_id INT,
    IN p_customer_id INT,
    IN p_customer_user_name VARCHAR(255),
    IN p_customer_first_name VARCHAR(255),
    IN p_customer_last_name VARCHAR(255),
    IN p_customer_email VARCHAR(255),
    IN p_customer_phone_no VARCHAR(50),
    IN p_customer_street_name VARCHAR(255),
    IN p_customer_street_no INT,
    IN p_customer_city VARCHAR(100),
    IN p_customer_state VARCHAR(100),
    IN p_customer_postal_code VARCHAR(20),
    IN p_customer_country VARCHAR(100)
)
BEGIN
    UPDATE Customer 
    SET 
        customer_user_name = p_customer_user_name, 
        customer_first_name = p_customer_first_name, 
        customer_last_name = p_customer_last_name, 
        customer_email = p_customer_email, 
        customer_phone_no = p_customer_phone_no, 
        customer_street_name = p_customer_street_name, 
        customer_street_no = p_customer_street_no, 
        customer_city = p_customer_city, 
        customer_state = p_customer_state, 
        customer_postal_code = p_customer_postal_code, 
        customer_country = p_customer_country
    WHERE 
        customer_id = p_customer_id 
        AND company_id = p_company_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertNewEmployee(
    IN p_employee_username VARCHAR(255),
    IN p_employee_password VARCHAR(255),
    IN p_employee_id INT,
    IN p_employee_first_name VARCHAR(255),
    IN p_employee_last_name VARCHAR(255),
    IN p_employee_email VARCHAR(255),
    IN p_employee_phone_no VARCHAR(50),
    IN p_employee_hire_date DATE,
    IN p_employee_street_name VARCHAR(255),
    IN p_employee_street_no INT,
    IN p_employee_city VARCHAR(100),
    IN p_employee_state VARCHAR(100),
    IN p_employee_postal_code VARCHAR(20),
    IN p_employee_country VARCHAR(100),
    IN p_company_id INT,
    IN p_is_admin BOOLEAN
)
BEGIN
    INSERT INTO Employee (
        employee_user_name, 
        employee_password, 
        employee_id, 
        employee_first_name, 
        employee_last_name, 
        employee_email, 
        employee_phone_no, 
        employee_hire_date, 
        employee_street_name, 
        employee_street_no, 
        employee_city, 
        employee_state, 
        employee_postal_code, 
        employee_country, 
        company_id, 
        is_admin
    ) 
    VALUES (
        p_employee_username, 
        p_employee_password, 
        p_employee_id, 
        p_employee_first_name, 
        p_employee_last_name, 
        p_employee_email, 
        p_employee_phone_no, 
        p_employee_hire_date, 
        p_employee_street_name, 
        p_employee_street_no, 
        p_employee_city, 
        p_employee_state, 
        p_employee_postal_code, 
        p_employee_country, 
        p_company_id, 
        p_is_admin
    );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateAllFieldsOfAnEmployee(
    IN p_company_id INT,
    IN p_employee_id INT,
    IN p_employee_user_name VARCHAR(255),
    IN p_employee_password VARCHAR(255),
    IN p_employee_first_name VARCHAR(255),
    IN p_employee_last_name VARCHAR(255),
    IN p_employee_email VARCHAR(255),
    IN p_employee_phone_no VARCHAR(50),
    IN p_employee_street_name VARCHAR(255),
    IN p_employee_street_no INT,
    IN p_employee_city VARCHAR(100),
    IN p_employee_state VARCHAR(100),
    IN p_employee_postal_code VARCHAR(20),
    IN p_employee_country VARCHAR(100),
    IN p_is_admin BOOLEAN,
    IN p_employee_hire_date DATE
)
BEGIN
    UPDATE Employee 
    SET 
        employee_user_name = p_employee_user_name, 
        employee_password = p_employee_password, 
        employee_first_name = p_employee_first_name, 
        employee_last_name = p_employee_last_name, 
        employee_email = p_employee_email, 
        employee_phone_no = p_employee_phone_no, 
        employee_street_name = p_employee_street_name, 
        employee_street_no = p_employee_street_no, 
        employee_city = p_employee_city, 
        employee_state = p_employee_state, 
        employee_postal_code = p_employee_postal_code, 
        employee_country = p_employee_country, 
        is_admin = p_is_admin, 
        employee_hire_date = p_employee_hire_date
    WHERE 
        employee_id = p_employee_id 
        AND company_id = p_company_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertNewProcess(
    IN p_company_id INT,
    IN p_customer_id INT,
    IN p_employee_id INT,
    IN p_invoice_id INT
)
BEGIN
    INSERT INTO Processes (
        company_id, 
        customer_id, 
        employee_id, 
        invoice_id
    ) 
    VALUES (
        p_company_id, 
        p_customer_id, 
        p_employee_id, 
        p_invoice_id
    );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertNewProduct(
    IN p_newProductID INT,
    IN p_product_price DECIMAL(10,2),
    IN p_quantity INT,
    IN p_selected_company_id INT,
    IN p_item_name VARCHAR(255),
    IN p_brand_id INT
)
BEGIN
    INSERT INTO Product (
        product_id, 
        product_price, 
        product_quantity, 
        company_id, 
        item_name, 
        brand_id
    ) 
    VALUES (
        p_newProductID, 
        p_product_price, 
        p_quantity, 
        p_selected_company_id, 
        p_item_name, 
        p_brand_id
    );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateProductQuantityOfACompany(
    IN p_company_id INT,
    IN p_product_id INT,
    IN p_new_quantity INT
)
BEGIN
    UPDATE Product 
    SET product_quantity = p_new_quantity
    WHERE product_id = p_product_id 
    AND company_id = p_company_id;
END //
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetTopSellingProductsOfACompany(
    IN company_id INT, 
    IN max_returned_records_count INT
)
BEGIN
    SELECT p.item_name AS product_name, 
           p.product_price AS unit_price, 
           SUM(ili.invoice_item_quantity) AS total_quantity_sold, 
           SUM(ili.invoice_item_quantity * p.product_price) AS total_revenue
    FROM Product p
    JOIN Invoice_Line_Items ili 
        ON p.company_id = ili.company_id 
        AND p.product_id = ili.product_id
    WHERE p.company_id = company_id
    GROUP BY p.item_name, p.product_price
    ORDER BY total_revenue DESC
    LIMIT max_returned_records_count;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetLowStockProductsInformation(
    IN in_company_id INT,
    IN in_bottom_threshold INT
)
BEGIN
    SELECT p.item_name AS product_name, 
           b.brand_name AS brand,
           p.product_quantity AS current_stock, 
           p.product_price AS unit_price
    FROM Product p
    JOIN Brand b 
      ON p.brand_id = b.brand_id
    WHERE p.product_quantity < in_bottom_threshold 
      AND p.company_id = in_company_id
    ORDER BY p.product_quantity ASC;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetProductCatalogPerformanceAcrossCompanies()
BEGIN
    SELECT 
        b.brand_name AS brand,
        p.item_name AS product_name,
        comp.company_name AS company,
        SUM(ili.invoice_item_quantity) AS total_units_sold,
        SUM(ili.invoice_item_quantity * p.product_price) AS total_revenue
    FROM 
        Brand b
    JOIN 
        Product_Catalog pc ON b.brand_id = pc.brand_id
    JOIN 
        Product p ON pc.item_name = p.item_name AND pc.brand_id = p.brand_id
    JOIN 
        Company comp ON p.company_id = comp.company_id
    JOIN 
        Invoice_Line_Items ili ON p.company_id = ili.company_id AND p.product_id = ili.product_id
    GROUP BY 
        b.brand_name, p.item_name, comp.company_name
    ORDER BY 
        total_revenue DESC;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetBrandRevenueOfCompany(IN input_company_id INT)
BEGIN
    SELECT 
        comp.company_name AS company,
        b.brand_name AS brand,
        SUM(ili.invoice_item_quantity * p.product_price) AS brand_revenue
    FROM 
        Company comp
    JOIN 
        Product p ON comp.company_id = p.company_id
    JOIN 
        Product_Catalog pc ON p.item_name = pc.item_name AND p.brand_id = pc.brand_id
    JOIN 
        Brand b ON pc.brand_id = b.brand_id
    JOIN 
        Invoice_Line_Items ili ON p.company_id = ili.company_id AND p.product_id = ili.product_id
    WHERE 
        p.company_id = input_company_id
    GROUP BY 
        comp.company_name, b.brand_name
    ORDER BY 
        brand_revenue DESC;
END$$
DELIMITER ;