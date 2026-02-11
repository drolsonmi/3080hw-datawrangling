"""
Test file for encode_gender function
"""

import pandas as pd
import sys

def test_2():
    try:
        from hw_datawrangling import encode_gender
        
        # Load test data
        patients = pd.read_csv('./data/patients.csv')
        
        # Run the function
        result = encode_gender(patients.copy())
        
        # Test 1: Check if new columns exist
        assert 'gender_M' in result.columns, "Column 'gender_M' not found in result"
        assert 'gender_F' in result.columns, "Column 'gender_F' not found in result"
        print("✓ Test 1 passed: Gender encoding columns exist")
        
        # Test 2: Check if original columns are preserved
        assert all(col in result.columns for col in patients.columns), "Original columns were modified or removed"
        print("✓ Test 2 passed: Original columns preserved")
        
        # Test 3: Check Male encoding
        male_rows = result[result['gender'] == 'M']
        assert all(male_rows['gender_M'] == 1), "Male rows should have gender_M = 1"
        assert all(male_rows['gender_F'] == 0), "Male rows should have gender_F = 0"
        print("✓ Test 3 passed: Male gender encoded correctly")
        
        # Test 4: Check Female encoding
        female_rows = result[result['gender'] == 'F']
        assert all(female_rows['gender_F'] == 1), "Female rows should have gender_F = 1"
        assert all(female_rows['gender_M'] == 0), "Female rows should have gender_M = 0"
        print("✓ Test 4 passed: Female gender encoded correctly")
        
        # Test 5: Check that values are only 0 or 1
        assert result['gender_M'].isin([0, 1]).all(), "gender_M should only contain 0 or 1"
        assert result['gender_F'].isin([0, 1]).all(), "gender_F should only contain 0 or 1"
        print("✓ Test 5 passed: Encoded values are binary (0 or 1)")
        
        # Test 6: Check that each row has exactly one gender
        assert all(result['gender_M'] + result['gender_F'] == 1), "Each row should have exactly one gender encoded"
        print("✓ Test 6 passed: Each row has exactly one gender")
        
        print("\n✅ All tests passed for encode_gender!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error running tests: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_2()
