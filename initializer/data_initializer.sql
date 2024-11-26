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
('user1', 'userpass1', 106, 'Michael', 'Green', 'michael.green@example.com', '5556789012', '2023-03-15', 'Birch Street', 30, 'Sunnyvale', 'CA', '94086', 'USA', 1, FALSE),
('user2', 'userpass2', 107, 'Laura', 'King', 'laura.king@example.com', '5557890123', '2022-07-22', 'Willow Avenue', 12, 'Mountain View', 'CA', '94043', 'USA', 2, FALSE),
('user3', 'userpass3', 108, 'Daniel', 'Lee', 'daniel.lee@example.com', '5558901234', '2021-10-10', 'Spruce Road', 55, 'Palo Alto', 'CA', '94301', 'USA', 3, FALSE),
('user4', 'userpass4', 109, 'Sarah', 'White', 'sarah.white@example.com', '5559012345', '2020-12-05', 'Fir Lane', 19, 'San Jose', 'CA', '95112', 'USA', 4, FALSE),
('user5', 'userpass5', 110, 'James', 'Wilson', 'james.wilson@example.com', '5550123456', '2023-08-01', 'Ash Boulevard', 88, 'Santa Clara', 'CA', '95050', 'USA', 5, FALSE);

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
('cust5', 'custpass5', 205, 'Mia', 'Davis', 'mia.davis@example.com', '5555678901', 'Pine Lane', 62, 'Hilltop', 'WA', '98001', 'USA', 5);

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