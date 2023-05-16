class Solution (object):
    def countStudents(self, students, sandwiches):
        """
            :type students: List[int]
            :type sandwiches: List[int]
            :rtype: int
        """
        queue = collections.deque(students)
        
        for sandwich in sandwiches:
            if sandwich in queue:
                while queue[0] != sandwich:
                    x = queue.popleft(x)
                    queue.append (x)
                queue.popleft()
            else:
                return len(queue)
        return 0