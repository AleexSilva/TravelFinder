"""
Test script for TravelFinder Pro scraper
Run this to verify the scraper is working correctly
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from travel_scraper import TravelScraper
from datetime import datetime, timedelta

def test_basic_scraper():
    """Test basic scraper functionality"""
    print("ðŸ§ª Testing TravelFinder Pro Scraper")
    print("=" * 50)

    # Initialize scraper
    scraper = TravelScraper()
    print("âœ… Scraper initialized successfully")

    # Test search parameters
    origin = "JFK"
    destination = "LAX"
    departure_date = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
    return_date = (datetime.now() + timedelta(days=37)).strftime('%Y-%m-%d')

    print(f"ðŸ” Testing search: {origin} â†’ {destination}")
    print(f"ðŸ“… Departure: {departure_date}")
    print(f"ðŸ“… Return: {return_date}")
    print(f"ðŸ’° Max Price: $1000")
    print()

    # Perform search
    try:
        results = scraper.search_flights(
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            return_date=return_date,
            trip_type="Round Trip",
            max_price=1000.0
        )

        print(f"âœ… Search completed successfully!")
        print(f"ðŸ“Š Found {len(results)} flight options")
        print()

        if results:
            print("ðŸŽ¯ Sample Results:")
            print("-" * 50)
            for i, trip in enumerate(results[:3]):  # Show first 3 results
                print(f"{i+1}. {trip.airline}")
                print(f"   ðŸ’° Price: ${trip.price:.2f}")
                print(f"   â±ï¸  Duration: {trip.duration}")
                print(f"   ðŸ”„ Stops: {trip.stops}")
                print(f"   ðŸŒ Source: {trip.source_website}")
                print()

        return True

    except Exception as e:
        print(f"âŒ Error during search: {e}")
        return False

def test_price_trends():
    """Test price trend functionality"""
    print("ðŸ“ˆ Testing Price Trends")
    print("=" * 50)

    scraper = TravelScraper()

    try:
        trends = scraper.get_price_trends("JFK", "LAX", days=30)

        if trends:
            print("âœ… Price trends generated successfully!")
            print(f"ðŸ“Š Data points: {len(trends.get('dates', []))}")
            print(f"ðŸ’° Average price: ${trends.get('average_price', 0):.2f}")
            print(f"ðŸ’² Price range: ${trends.get('min_price', 0):.2f} - ${trends.get('max_price', 0):.2f}")
            print(f"ðŸŽ¯ Best day: {trends.get('best_day', 'N/A')}")
            return True
        else:
            print("âŒ No price trend data generated")
            return False

    except Exception as e:
        print(f"âŒ Error getting price trends: {e}")
        return False

def main():
    """Run all tests"""
    print("ðŸš€ TravelFinder Pro - Test Suite")
    print("=" * 50)
    print()

    tests = [
        ("Basic Scraper", test_basic_scraper),
        ("Price Trends", test_price_trends),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"ðŸ§ª Running {test_name} test...")
        try:
            if test_func():
                print(f"âœ… {test_name} test PASSED")
                passed += 1
            else:
                print(f"âŒ {test_name} test FAILED")
        except Exception as e:
            print(f"âŒ {test_name} test ERROR: {e}")

        print()

    print("=" * 50)
    print(f"ðŸ“Š Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("ðŸŽ‰ All tests passed! TravelFinder Pro is ready to use.")
        print("ðŸ“ Run 'streamlit run app.py' to start the web interface.")
    else:
        print("âš ï¸  Some tests failed. Check the output above for details.")

    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)