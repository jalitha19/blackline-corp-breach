CREATE DATABASE IF NOT EXISTS blackline_portal;

USE blackline_portal;


CREATE TABLE IF NOT EXISTS users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    employee_id VARCHAR(30) NOT NULL,

    username VARCHAR(50) NOT NULL UNIQUE,

    password VARCHAR(100) NOT NULL,

    full_name VARCHAR(100) NOT NULL,

    department VARCHAR(100) NOT NULL,

    role VARCHAR(100) NOT NULL,

    status VARCHAR(30) NOT NULL DEFAULT 'active'

);


INSERT INTO users
(
    employee_id,
    username,
    password,
    full_name,
    department,
    role,
    status
)
VALUES

(
    'BL-0427',
    'mreed',
    'archived-access-2026',
    'Maya Reed',
    'Infrastructure & Operations',
    'Infrastructure Analyst',
    'archived'
),

(
    'BL-0119',
    'dpark',
    'infra-ops-1182',
    'Daniel Park',
    'Infrastructure & Operations',
    'Head of Infrastructure',
    'active'
),

(
    'BL-0214',
    'snguyen',
    'soc-monitor-2941',
    'Sofia Nguyen',
    'Cyber Defence',
    'Security Operations Lead',
    'active'
);