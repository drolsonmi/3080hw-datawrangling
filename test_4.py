"""
Test file for pivot_bed_type_costs function
"""

import pandas as pd
import sys

def test_4():
    try:
        from hw_datawrangling import pivot_bed_type_costs
        
        # Load test data
        resources = pd.read_csv('./data/resources.csv')
        
        # Run the function
        result = pivot_bed_type_costs(resources)
        
        # Test 1: Check if result is a Series
        assert isinstance(result, pd.Series), "Result should be a pandas Series"
        print("✓ Test 1 passed: Result is a Series")
        
        # Test 2: Check if bed types are in the index
        expected_bed_types = {'Private', 'Shared', 'ICU'}
        assert set(result.index) == expected_bed_types, f"Expected bed types {expected_bed_types}, got {set(result.index)}"
        print("✓ Test 2 passed: All bed types present in index")
        
        # Test 3: Check ICU total (should be 1200 * 3 = 3600)
        icu_total = resources[resources['bed_type'] == 'ICU']['daily_rate'].sum()
        assert result['ICU'] == icu_total, f"ICU total should be {icu_total}, got {result['ICU']}"
        print("✓ Test 3 passed: ICU total calculated correctly")
        
        # Test 4: Check Private total (should be 500 * 6 = 3000)
        private_total = resources[resources['bed_type'] == 'Private']['daily_rate'].sum()
        assert result['Private'] == private_total, f"Private total should be {private_total}, got {result['Private']}"
        print("✓ Test 4 passed: Private total calculated correctly")
        
        # Test 5: Check Shared total (should be 300 * 6 = 1800)
        shared_total = resources[resources['bed_type'] == 'Shared']['daily_rate'].sum()
        assert result['Shared'] == shared_total, f"Shared total should be {shared_total}, got {result['Shared']}"
        print("✓ Test 5 passed: Shared total calculated correctly")
        
        # Test 6: Check if sorted in descending order
        assert list(result.values) == sorted(result.values, reverse=True), "Result should be sorted in descending order"
        print("✓ Test 6 passed: Results sorted in descending order")
        
        # Test 7: Verify the order (ICU should be first)
        assert result.index[0] == 'ICU', "ICU should be first (highest total)"
        print("✓ Test 7 passed: Highest value (ICU) is first")
        
        print("\n✅ All tests passed for pivot_bed_type_costs!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error running tests: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_4()