"""
Test file for group_by_department function
"""

import pandas as pd
import sys

def test_5():
    from hw_datawrangling import group_by_department
    
    # Load test data
    billing = pd.read_csv('./data/billing.csv')
    
    # Run the function
    result = group_by_department(billing)
    
    # Test 1: Check if result is a DataFrame
    assert isinstance(result, pd.DataFrame), "Result should be a pandas DataFrame"
    print("✓ Test 1 passed: Result is a DataFrame")
    
    # Test 2: Check if required columns exist
    required_cols = ['procedure_count', 'total_charges', 'avg_charge']
    for col in required_cols:
        assert col in result.columns, f"Column '{col}' not found in result"
    print("✓ Test 2 passed: All required columns present")
    
    # Test 3: Check if dept_code is the index
    assert result.index.name == 'dept_code' or 'dept_code' in result.index.names or all(result.index.isin(billing['dept_code'].unique())), "dept_code should be the index"
    print("✓ Test 3 passed: dept_code is the index")
    
    # Test 4: Check procedure counts
    # SURG should have 3 procedures
    surg_count = billing[billing['dept_code'] == 'SURG'].shape[0]
    assert result.loc['SURG', 'procedure_count'] == surg_count, f"SURG procedure count should be {surg_count}"
    print("✓ Test 4 passed: Procedure counts calculated correctly")
    
    # Test 5: Check total charges for CARD
    card_total = billing[billing['dept_code'] == 'CARD']['charge_amount'].sum()
    assert result.loc['CARD', 'total_charges'] == card_total, f"CARD total charges should be {card_total}"
    print("✓ Test 5 passed: Total charges calculated correctly")
    
    # Test 6: Check average charge for RAD
    rad_avg = billing[billing['dept_code'] == 'RAD']['charge_amount'].mean()
    assert abs(result.loc['RAD', 'avg_charge'] - rad_avg) < 0.01, f"RAD average charge should be {rad_avg}"
    print("✓ Test 6 passed: Average charges calculated correctly")
    
    # Test 7: Check if sorted by total_charges in descending order
    assert list(result['total_charges']) == sorted(result['total_charges'], reverse=True), "Result should be sorted by total_charges in descending order"
    print("✓ Test 7 passed: Results sorted by total_charges descending")
    
    # Test 8: Verify SURG has highest total (3 surgeries at 8500 each)
    assert result.iloc[0].name == 'SURG' or result.index[0] == 'SURG', "SURG should have the highest total charges"
    print("✓ Test 8 passed: Department with highest charges is first")
    
    print("\n✅ All tests passed for group_by_department!")
   
if __name__ == "__main__":
    test_5()