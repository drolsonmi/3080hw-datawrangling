## Dataset Description

You will work with four CSV files in the `./data/` folder:

### 1. `patients.csv`
Contains patient demographic and admission information:
- `patient_id`: Unique patient identifier
- `first_name`, `last_name`: Patient name
- `dob`: Date of birth
- `gender`: M or F
- `admission_date`, `discharge_date`: Hospital stay dates
- `insurance_type`: Insurance provider code (PPO, HMO, Medicare, Medicaid)

### 2. `billing.csv`
Contains billing records for procedures:
- `bill_id`: Unique billing identifier
- `patient_id`: Links to patients.csv
- `procedure_code`: Code for the medical procedure
- `dept_code`: Department code where procedure was performed
- `charge_amount`: Cost of the procedure
- `billing_date`: Date of billing

### 3. `resources.csv`
Contains hospital resource allocation:
- `resource_id`: Unique resource identifier
- `patient_id`: Links to patients.csv
- `room_number`: Assigned room
- `bed_type`: Private, Shared, or ICU
- `daily_rate`: Daily cost for the bed type
- `staff_assigned`: Number of staff members assigned

### 4. Reference Files
- `procedure_codes.csv`: Maps procedure codes to procedure names and categories
- `department_codes.csv`: Maps department codes to full names and floor numbers
