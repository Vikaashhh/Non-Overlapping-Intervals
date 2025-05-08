class Solution:
    def minRemoval(self, intervals):
        # Pehle intervals ko unke end time ke basis pe sort karo
        intervals.sort(key=lambda x: x[1])
        
        # Count kareinge non-overlapping intervals ko
        count = 0
        prev_end = float('-inf')  # Shuru mein koi previous end nahi hai
        
        # Har interval ke liye check karo
        for interval in intervals:
            start, end = interval
            if start >= prev_end:
                # Agar overlap nahi ho raha toh count badhao
                count += 1
                prev_end = end  # Ab ye current interval ka end next ke liye prev_end banega
        
        # Total remove karne ke liye = total intervals - non-overlapping intervals
        return len(intervals) - count
