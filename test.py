class Solution:
    def my_atoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit signed integer (atoi implementation).
        
        Args:
            s (str): Input string.
        
        Returns:
            int: Converted integer with clamping to 32-bit range if necessary.
        """
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        i, n = 0, len(s)
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check for optional sign
        sign = 1
        if i < n and s[i] in ('-', '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Convert digits to integer
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before updating result
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
