def main():
    BASE = 208
    COEFFICIENT = 0.7
    ROUNDING_FACTOR = 2
    ZONE_1_LOWER_DECIMAL = 0.5
    ZONE_1_UPPER_DECIMAL = 0.6
    ZONE_2_UPPER_DECIMAL = 0.7
    ZONE_3_UPPER_DECIMAL = 0.8
    ZONE_4_UPPER_DECIMAL = 0.93
    INCREMENT = 0.01

    age = int(input("Please enter your age: "))
    resting_rate = int(input("Please enter your resting heart rate: "))
    print("=======================================")
    MAX_HEART_RATE = BASE - COEFFICIENT * age
    RESERVE = MAX_HEART_RATE - resting_rate

    print("Your heart rate reserve is: {} bpm".format(round(RESERVE,
                                                            ROUNDING_FACTOR)))
    zone_1_lower = resting_rate + RESERVE * ZONE_1_LOWER_DECIMAL
    zone_1_upper = resting_rate + RESERVE * ZONE_1_UPPER_DECIMAL
    zone_2_lower = zone_1_upper + INCREMENT
    zone_2_upper = resting_rate + RESERVE * ZONE_2_UPPER_DECIMAL
    zone_3_lower = zone_2_upper + INCREMENT
    zone_3_upper = resting_rate + RESERVE * ZONE_3_UPPER_DECIMAL
    zone_4_lower = zone_3_upper + INCREMENT
    zone_4_upper = resting_rate + RESERVE * ZONE_4_UPPER_DECIMAL
    zone_5_lower = zone_4_upper + INCREMENT
    zone_5_upper = resting_rate + RESERVE

    print("Here is a breakdown of your training zones:")
    # 50%
    print("zone 1: {} to {} bpm".format(round(zone_1_lower, ROUNDING_FACTOR),
                                        round(zone_1_upper, ROUNDING_FACTOR)))
    # 60%
    print("zone 2: {} to {} bpm".format(round(zone_2_lower, ROUNDING_FACTOR),
                                        round(zone_2_upper, ROUNDING_FACTOR)))
    # 70%
    print("zone 3: {} to {} bpm".format(round(zone_3_lower, ROUNDING_FACTOR),
                                        round(zone_3_upper, ROUNDING_FACTOR)))
    # 80%
    print("zone 4: {} to {} bpm".format(round(zone_4_lower, ROUNDING_FACTOR),
                                        round(zone_4_upper, ROUNDING_FACTOR)))
    # 93%
    print("zone 5: {} to {} bpm".format(round(zone_5_lower, ROUNDING_FACTOR),
                                        round(zone_5_upper, ROUNDING_FACTOR)))
    print("=======================================")


main()
