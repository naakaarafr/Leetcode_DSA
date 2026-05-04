class Solution:
    def divide(self, dividend, divisor):
        # Handle overflow case
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with positives
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Double until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        return sign * quotient