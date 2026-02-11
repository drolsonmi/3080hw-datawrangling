"""
Test file for join_patient_billing function
"""

import pandas as pd
import sys

def test_3():
    try:
        from hw_datawrangling import join_patient_billing
        
        # Load test data
        patients = pd.read_csv('./data/patients.csv')
        billing = pd.read_csv('./data/billing.csv')
        
        # Run the function
        result = join_patient_billing(patients, billing)
        
        # Test 1: Check if result is a DataFrame
        assert isinstance(result, pd.DataFrame), "Result should be a pandas DataFrame"
        print("✓ Test 1 passed: Result is a DataFrame")
        
        # Test 2: Check that patient columns are present
        patient_cols = ['patient_id', 'first_name', 'last_name', 'gender', 'insurance_type']
        for col in patient_cols:
            assert col in result.columns, f"Patient column '{col}' not found in result"
        print("✓ Test 2 passed: Patient columns present")
        
        # Test 3: Check that billing columns are present
        billing_cols = ['bill_id', 'procedure_code', 'dept_code', 'charge_amount']
        for col in billing_cols:
            assert col in result.columns, f"Billing column '{col}' not found in result"
        print("✓ Test 3 passed: Billing columns present")
        
        # Test 4: Check number of rows (should match billing since it's inner join)
        assert len(result) == len(billing), f"Expected {len(billing)} rows, got {len(result)}"
        print("✓ Test 4 passed: Correct number of rows after join")
        
        # Test 5: Check that join was done correctly on patient_id
        # Every bill should have corresponding patient info
        assert result['patient_id'].notna().all(), "Some patient_ids are missing after join"
        print("✓ Test 5 passed: All patient_ids present after join")
        
        # Test 6: Verify specific patient-billing match
        p001_bills = result[result['patient_id'] == 'P001']
        assert len(p001_bills) == 2, "Patient P001 should have 2 bills"
        assert all(p001_bills['first_name'] == 'John'), "Patient P001 should have first_name 'John'"
        print("✓ Test 6 passed: Specific patient-billing matches correct")
        
        # Test 7: Check that no duplicate patient_id columns exist
        assert result.columns.tolist().count('patient_id') == 1, "Duplicate patient_id columns found"
        print("✓ Test 7 passed: No duplicate columns")
        
        print("\n✅ All tests passed for join_patient_billing!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error running tests: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_3()