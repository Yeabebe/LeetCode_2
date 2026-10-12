class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            slow = fast = i
            direction = nums[i] > 0

            while True:
                # Move slow one step
                if (nums[slow] > 0) != direction:
                    break
                slow = next_index(slow)

                # Move fast one step
                if (nums[fast] > 0) != direction:
                    break
                fast = next_index(fast)

                # Move fast a second step
                if (nums[fast] > 0) != direction:
                    break
                fast = next_index(fast)

                # A cycle must contain more than one index
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

        return False