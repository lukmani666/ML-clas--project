location_list = sorted([
    'Ikeja', 'Idu Industrial', 'Alimosho', 'Ogba', 'Apapa', 'Ibadan', 'Agege', 'Ifako-Ijaiye',
    'Amuwo-Odofin', 'Gudu', 'Ajah', 'Ikoyi', 'Katampe', 'Central Business District', 'Lekki',
    'Gbagada', 'Ojodu', 'Sagamu', 'Owerri', 'Port-Harcourt', 'Ado Ekiti', 'Karu', 'Gwarinpa',
    'Oluyole', 'Isolo', 'Abule Egba', 'Uyo', 'Epe', 'Ijebu Ode', 'Ojo', 'Kubwa', 'Ikorodu',
    'Jahi', 'Yaba', 'Magodo', 'Victoria Island', 'Benin City', 'Surulere', 'Gwagwalada',
    'Ewekoro', 'Warri', 'Lugbe District', 'Ilupeju', 'Abeokuta North', 'Kosofe', 'Mushin',
    'Mabushi', 'Ilorin South', 'Ejigbo', 'Kachia', 'Ogudu', 'Jabi', 'Ikotun/Igando',
    'Aba North', 'Wuse', 'Obio-Akpor', 'Garki 2', 'Mpape', 'Akure', 'Oshimili South', 'Enugu',
    'Gwale', 'Onitsha', 'Kurudu', 'Zuba', 'Nyanya', 'Ipaja', 'Asokoro', 'Muya', 'Umuahia',
    'Osogbo', 'Kaduna / Kaduna State', 'Badagry', 'Lokogoma', 'Shomolu', 'Abeokuta South',
    'Calabar', 'Maryland', 'Ife', 'Ifo', 'Gaduwa', 'Zaria', 'Durumi', 'Lokoja', 'Wuse 2',
    'Oshodi', 'Apo District', 'Owan', 'Kuje', 'Egbe/Idimu', 'Lagos Island (Eko)', 'Orile',
    'Ojota', 'Ibeju', 'Mararaba', 'Awka'
])

make_list = sorted([
    'Honda', 'Land', 'Lexus', 'Chrysler', 'Toyota', 'Kia', 'Mazda', 'Acura', 'Nissan',
    'Volkswagen', 'Ford', 'Peugeot', 'Hyundai', 'Jeep', 'BMW', 'GMC'
    'Chevrolet', 'JMC', 'Mitsubishi', 'Volvo', 'Infiniti', 'Audi', 'Rover',
    'International', 'Bentley', 'Dodge', 'Pontiac', 'ZX', 'Jetour', 'Opel',
    'Brilliance', 'Daihatsu', 'Buick', 'Subaru', 'Lincoln', 'Changan', 'GAC', 'Mini',
    'Jaguar', 'Cadillac', 'Scion', 'Gonow'
])

model_list = sorted([
    'Odyssey', 'Rover', 'ES', '200', 'Venza', 'Sportage', 'Highlander', 'Sienna',
    'Demio', 'MDX', 'Camry', 'Frontier', 'GX', 'Passat', 'Accord', 'Matrix',
    'Edge', 'RX', '206', 'CR-V', 'Corolla', 'Elantra', 'Civic', 'Yaris', 'ZDX', 'RAV4',
    'Sonata', 'Explorer', 'Land', 'Taurus', 'Grand', 'Ridgeline', 'Sport', 'Avalon',
    '406', 'Freestar', 'X3', 'Escape', 'X5', '307', 'Focus', 'Pilot', 'Terrain',
    'Jetta', 'Tacoma', 'Malibu', 'Boarding', 'Rogue', 'L200', 'V70', 'Liberty',
    '4-Runner', 'Golf', 'Sorento', 'Element', 'Cerato', 'Crossfire', 'Beetle',
    'Palisade', 'FX35', 'F-150', 'XC90', 'Santa', '207', 'Accent', 'QX50',
    '407', 'A6', 'Rondo', 'NX', 'Avanza', 'Tiguan', '508', 'Commander',
    'Cruze', 'Continental', 'Pajero', 'Excursion', 'X-Trail', 'Caliber','316Ti',
    'Azera', 'Versa', 'MPV', 'Pathfinder', 'Genesis', 'S60', 'Borrego',
    'Vibe', '300C', 'Fortuner', '740', 'Ceed', 'Auto', 'RL', 'NP300', 'Dyna', 'S80',
    'X1', '7', 'Soul', 'Rio', 'Dashing', 'City', '807', 'Tundra', 'QX56', 'Sedona',
    '301', 'A4', 'Forte', 'Sequoia', 'Outlander', 'Solara', 'Avensis', '328i',
    'Veracruz', 'GS', 'G', 'Mohave', 'A5', 'CX-9', 'IS', 'TT', 'G35', '3', 'Freestyle',
    'Optima', 'CX-7', 'HiAce', 'Meriva', 'Picanto', 'Carnival', 'RC', 'Crosstour',
    'Bora', 'Armada', 'Nubira', 'Splendor', 'A3', 'Bestune', 'X6', 'Vanette', 'Spark',
    'Almera', 'Mercedes-Benz', 'LX', 'Touareg', 'Canter', 'Tucson', 'Kona', 'C-HR',
    'Maverick', 'Suburban', 'HIJET', 'Picnic', 'Q5', 'Xterra', 'Q7', 'Primera',
    'Encore', 'Tribeca', 'Ix35', 'QX60', 'Q60', 'MKX', 'Altima', 'Hilux', 'Ecosport',
    '535d', 'Prius', 'Mustang', 'RDX', '335i,' 'B-series', 'Eado', 'GA6', '3500',
    '323', 'Sharan', 'Fusion', 'Cooper', '121', 'Transit', 'Paseo', 'Express',
    'Caravan', '535i', 'Camaro', 'Sonic', '308', 'Zafira', 'Estima', 'XE', 'Escalade',
    'XF', 'Ranger', 'iM', 'Traverse', 'Fiesta', 'Huawei', 'F-Type', 'Troy',
    'FJ', 'Challenger', 'Agila', 'Avatr', 'TL', 'TLX', 'Morning', 'Sentra', 'Murano',
    '325i', 'BMW', 'HR-V', 'Transporter', 'GS3', 'Juke', 'Wrangler', 'Aygo'
])

year_list = sorted([
    2007, 2015, 2002, 2008, 2001, 2013, 2016, 2003, 2012, 2004, 2009,
    2005, 2006, 2010, 2019, 2014, 2011, 2018, 2000, 1999, 2020, 1998, 1968,
    2022, 1997, 1995, 1996, 2017, 2021, 2023, 1794, 2024, 1994, 2025
])