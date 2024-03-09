CREATE TABLE traffic_accidents (
    crash_record_id VARCHAR(255) NOT NULL,
    crash_date TIMESTAMP,
    posted_speed_limit INTEGER,
    traffic_control_device VARCHAR(50),
    device_condition VARCHAR(50),
    weather_condition VARCHAR(50),
    lighting_condition VARCHAR(50),
    first_crash_type VARCHAR(50),
    trafficway_type VARCHAR(50),
    injuries_total INTEGER,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    PRIMARY KEY(crash_record_id)
);
