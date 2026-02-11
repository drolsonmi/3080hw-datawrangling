[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/F9JWatEK)
# Homework: Hospital Data Wrangling

In this assignment, you will practice essential data wrangling techniques using real-world hospital data. You'll work with patient records, billing information, and resource allocation data to perform mapping, encoding, joining, and reshaping operations—core skills for any data scientist or analyst.

## Learning Objectives

By completing this assignment, you will demonstrate your ability to:

- **Map categorical values** to create more readable data representations
- **Encode categorical variables** into binary/numeric formats for analysis
- **Join multiple datasets** on common keys to create comprehensive views
- **Reshape data** using pivot tables to summarize information
- **Group and aggregate data** to calculate meaningful statistics

## Dataset Description

You will work with four CSV files in the ./data/ folder:

1. patients.csv
2. billing.csv
3. resources.csv
4. Reference Files

Additional documentation on these files is in the data_documentation.md file of the assignment repository.

## Instructions

Complete the five functions in `hw_datawrangling.py`. Each function has a detailed docstring explaining what it should do. Make sure to:

1. Read the docstring carefully for each function
2. Understand the input parameters and expected output
3. Test your function using the provided test files
4. Keep all docstrings intact

### Function 1: `map_insurance_codes(df)`

**Objective:** Create more readable insurance type names using dictionary mapping.

**What you need to do:**
- Create a new column called `insurance_full_name`
- Map the insurance codes to their full names:
  - `'PPO'` → `'Preferred Provider Organization'`
  - `'HMO'` → `'Health Maintenance Organization'`
  - `'Medicare'` → `'Medicare'`
  - `'Medicaid'` → `'Medicaid'`
- Return the DataFrame with the new column added
- Make sure to preserve all original columns

**Example output:**
```
  patient_id insurance_type              insurance_full_name
0       P001            PPO  Preferred Provider Organization
1       P002            HMO  Health Maintenance Organization
```

---

### Function 2: `encode_gender(df)`

**Objective:** Convert categorical gender data into binary numeric columns using one-hot encoding functions within pandas.

**What you need to do:**
- Create two new columns: `gender_M` and `gender_F`
- For Male patients: `gender_M` = 1, `gender_F` = 0
- For Female patients: `gender_F` = 1, `gender_M` = 0
- Return the DataFrame with the new columns added
- Ensure values are integers (0 or 1), not True/False

**Example output:**
```
  patient_id gender  gender_M  gender_F
0       P001      M         1         0
1       P002      F         0         1
```

---

### Function 3: `join_patient_billing(patients_df, billing_df)`

**Objective:** Combine patient and billing data to analyze charges by patient.

**What you need to do:**
- Perform an **INNER JOIN** between the two DataFrames
- Join on the `patient_id` column
- Return a single DataFrame with all columns from both datasets
- The result should have one row for each billing record with patient info attached

**Example output:**
```
  patient_id first_name last_name  ... bill_id procedure_code charge_amount
0       P001       John     Smith  ...   B1001        PROC123       2500.00
1       P001       John     Smith  ...   B1002        PROC456        450.00
```

---

### Function 4: `pivot_bed_type_costs(resources_df)`

**Objective:** Summarize resource costs by bed type using pivot operations.

**What you need to do:**
- Create a summary showing total daily rates for each bed type
- Group by `bed_type` and sum the `daily_rate`
- Sort the results in descending order (highest total first)
- Return a pandas Series with bed types as the index
- Return just the Series of totals, not a full DataFrame

**Example output:**
```
bed_type
ICU        3600
Private    3000
Shared     1800
Name: daily_rate, dtype: int64
```

---

### Function 5: `group_by_department(billing_df)`

**Objective:** Analyze billing patterns by department using groupby and aggregation.

**What you need to do:**
- Group the data by `dept_code`
- Calculate three metrics for each department:
  - `procedure_count`: Count of procedures
  - `total_charges`: Sum of all charges
  - `avg_charge`: Mean charge amount
- Sort by `total_charges` in descending order
- Return a DataFrame with these columns

**Hints:**
- Use `.groupby('dept_code')`
- Use `.agg()` with multiple aggregation functions
- Rename columns appropriately
- Use `.sort_values()` to sort by total_charges

**Example output:**
```
          procedure_count  total_charges  avg_charge
dept_code                                           
SURG                    3       25500.00     8500.00
EMER                    3        9600.00     3200.00
CARD                    3        7500.00     2500.00
```

---

## Testing Your Code

Test each function individually by running the corresponding test file:

```bash
python test_1.py  # Test map_insurance_codes
python test_2.py  # Test encode_gender
python test_3.py  # Test join_patient_billing
python test_4.py  # Test pivot_bed_type_costs
python test_5.py  # Test group_by_department
```

Each test file will show which tests passed (✓) and which failed (✗). All tests must pass for full credit.

You can also run the main file to see sample outputs:

```bash
python hw_datawrangling.py
```

## Rubric

| Criterion                        | Points | Description                                      |
| :------------------------------- | :----: | :----------------------------------------------: |
| Function 1: map_insurance_codes  | 4      | Correctly maps insurance codes to full names     |
| Function 2: encode_gender        | 4      | Correctly creates binary encoded gender columns  |
| Function 3: join_patient_billing | 4      | Correctly performs inner join on patient_id      |
| Function 4: pivot_bed_type_costs | 4      | Correctly creates pivot table and sorts by total |
| Function 5: group_by_department  | 4      | Correctly groups and aggregates billing data     |

**Total: 24 points**

## Common Pitfalls to Avoid

1. **Modifying the original DataFrame**: Always work on a copy or return a new DataFrame
2. **Wrong column names**: Match the exact column names specified in the docstrings
3. **Data types**: Ensure numeric columns are numeric (not strings) and binary encodings are integers
4. **Sorting**: Remember to sort in the correct direction (ascending vs descending)
5. **Missing values**: Check if your operations introduce or handle NaN values appropriately

## Tips for Success

- **Read the docstrings carefully** - they contain all the requirements
- **Test incrementally** - don't wait to test all functions at once
- **Check the data** - use `.head()`, `.info()`, and `.describe()` to understand the data
- **Use pandas documentation** - it's comprehensive and has great examples
- **Print intermediate results** - helps debug what's going wrong

## Submission

1. Complete all five functions in `hw_datawrangling.py`
2. Ensure all docstrings remain intact
3. Test that all test files pass
4. Commit and push your `hw_datawrangling.py` file to your GitHub repository
5. The autograder will run automatically when you push your code

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Data Wrangling with Pandas](https://pandas.pydata.org/docs/user_guide/index.html)
- Specific methods you'll need:
  - [map()](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html)
  - [get_dummies()](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
  - [merge()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
  - [groupby()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
  - [pivot_table()](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)

## Extension Challenges (Optional)

If you finish early and want extra practice:

1. Create a function that merges all three datasets (patients, billing, resources) into one comprehensive DataFrame
2. Add analysis that uses the mapping files (`procedure_codes.csv` and `department_codes.csv`) to add full procedure names and department names
3. Calculate length of stay for each patient and analyze costs by length of stay
4. Create visualizations of your findings using matplotlib or seaborn

---

**Good luck! Remember: data wrangling is a core skill that you'll use in almost every data science project.**

*This assignment was created with AI assistance to provide realistic healthcare data scenarios while maintaining patient privacy through synthetic data.*
