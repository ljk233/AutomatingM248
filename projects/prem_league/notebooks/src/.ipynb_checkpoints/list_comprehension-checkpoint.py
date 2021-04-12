
class ListComprehension():
    """
    A class of static methods that deal with list comprehension of the
    goal times.
    """

    ILLEGAL_CHARS: list = [",", "'"]
    
    def str_to_lst_str(goal_timings: str) -> list:
        """
        Returns a list of strings, where each string represents the
        match time a goal was scored.

        @param, goal_timings,   a comma-separated string of goal times.

        @returns, list,         list of strings, where each string is a
                                match time when a goal was scored.
        """

        lst_goal_times: list = list()
            
        
        