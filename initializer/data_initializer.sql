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
('admin5', 'admin789', 105, 'David', 'Taylor', 'david.t@example.com', '5555678901', '2023-06-01', 'Pine Lane', 62, 'Hilltop', 'WA', '98001', 'USA', 5, TRUE);

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