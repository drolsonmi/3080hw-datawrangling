"""
Test file for map_insurance_codes function
"""

import pandas as pd
import sys

def test_1():
    from hw_datawrangling import map_insurance_codes
    
    # Load test data
    patients = pd.read_csv('./data/patients.csv')
    
    # Run the function
    result = map_insurance_codes(patients.copy())
    
    # Test 1: Check if new column exists
    assert 'insurance_full_name' in result.columns, "Column 'insurance_full_name' not found in result"
    print("✓ Test 1 passed: 'insurance_full_name' column exists")
    
    # Test 2: Check if original columns are preserved
    assert all(col in result.columns for col in patients.columns), "Original columns were modified or removed"
    print("✓ Test 2 passed: Original columns preserved")
    
    # Test 3: Check PPO mapping
    ppo_rows = result[result['insurance_type'] == 'PPO']
    assert all(ppo_rows['insurance_full_name'] == 'Preferred Provider Organization'), "PPO not mapped correctly"
    print("✓ Test 3 passed: PPO mapped correctly")
    
    # Test 4: Check HMO mapping
    hmo_rows = result[result['insurance_type'] == 'HMO']
    assert all(hmo_rows['insurance_full_name'] == 'Health Maintenance Organization'), "HMO not mapped correctly"
    print("✓ Test 4 passed: HMO mapped correctly")
    
    # Test 5: Check Medicare mapping
    medicare_rows = result[result['insurance_type'] == 'Medicare']
    assert all(medicare_rows['insurance_full_name'] == 'Medicare'), "Medicare not mapped correctly"
    print("✓ Test 5 passed: Medicare mapped correctly")
    
    # Test 6: Check Medicaid mapping
    medicaid_rows = result[result['insurance_type'] == 'Medicaid']
    assert all(medicaid_rows['insurance_full_name'] == 'Medicaid'), "Medicaid not mapped correctly"
    print("✓ Test 6 passed: Medicaid mapped correctly")
    
    # Test 7: Check that all rows have a mapping
    assert result['insurance_full_name'].notna().all(), "Some insurance types were not mapped"
    print("✓ Test 7 passed: All insurance types mapped")
    
    print("\n✅ All tests passed for map_insurance_codes!")
        
if __name__ == "__main__":
    test_1()