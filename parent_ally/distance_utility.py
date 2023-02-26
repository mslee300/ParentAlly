"""
This module stores utility functions for calculating distances
between locations.
"""

import math


def distance(lat1, lon1, lat2, lon2):
    """
    Use the Haversine formula to mathematically calculate 
    the distance between two coordinates. Negative coordinates
    indicate West and South, and positive coordinates indicate
    North and East.
    """
    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Calculate the differences between the latitudes and longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Calculate the Haversine formula
    a = math.sin(dlat/2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    radius = 6371  # Earth's radius in kilometers
    distance = radius * c  # Distance in kilometers

    return distance
