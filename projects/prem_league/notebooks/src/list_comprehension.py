
class ListComprehension():
    """
    A class of static methods that deal with list comprehension of the
    goal times.
    """

    ILLEGAL_CHARS: list = [",", "'"]

    def comma_separated_strings_to_list(a_list: list) -> list:
        """
        Returns a list of strings, where each string represents the
        match time a goal was scored.

        @param, a_list: list(str)
            a list of strings, where each string contains a comma
            separated string of goal times.
            Example: ["3,10,85", "5, 64", "23"]

        @returns, list(list(str))
            a list of lists of strings
            Example: [["3", "10", "85"], ["5", "64"], ["23"]]
        """

        lists: list = list()
        k: int = 0  # counter variable

        for a_str in a_list:
            a_str_list: list = list()

            if (a_str != "NaN"):
                k = 0  # initiate the counter
                a_time_str = ""

                while (k < len(a_str)):
                    a_char = a_str[k]

                    if a_char not in ListComprehension.ILLEGAL_CHARS:
                        a_time_str = a_time_str + a_char
                    else:
                        a_str_list.append(a_time_str)
                        a_time_str = ""  # reset the time

                    k += 1

                a_str_list.append(a_time_str)  # add the final goal

            lists.append(a_str_list)

        return lists

    def comma_separated_str_to_lst_uniform_dist(a_list: list) -> list:
        """
        Returns a list of strings, where each string represents the
        match time a goal was scored.

        @param, a_list: list(str)
            a list of strings, where each string contains a comma
            separated string of goal times.
            Example: ["3,10,85", "5, 64", "23"]

        @returns, list(list(str))
            a list of lists of strings
            Example: [["3", "10", "85"], ["5", "64"], ["23"]]
        """

        lists: list = list()
        k: int = 0  # counter variable

        for a_str in a_list:
            a_str_list: list = list()

            if (a_str != "NaN"):
                k = 0  # initiate the counter
                a_time_str = ""

                while (k < len(a_str)):
                    a_char = a_str[k]

                    if a_char != ",":
                        a_time_str = a_time_str + a_char
                    else:
                        a_str_list.append(a_time_str)
                        a_time_str = ""  # reset the time

                    k += 1

                a_str_list.append(a_time_str)  # add the final goal

            lists.append(a_str_list)

        return lists

    def list_str_to_list_int(lists: list) -> list:
        """
        Returns a list of integers, where each string represents the
        match time a goal was scored.

        @param, list_strings, list(list(str))
            list of lists(str), where each element of the sub-list is
            a string representing the match time when a goal was
            scored.
            Example: [["3", "10", "85"], ["5", "64"], ["23"]]

        @returns, list(list(int))
            list of lists of ints.
            Example: [[3, 10, 85], [5, 64], [23]]
        """

        ret_list: list = list()

        for a_str_list in lists:
            an_int_list: list = list()

            for a_str in a_str_list:
                an_int_list.append(int(a_str))

            ret_list.append(an_int_list)

        return ListComprehension._clean_goal_time_list(ret_list)

    def _clean_goal_time_list(lists: list) -> list:
        """
        Output from method list_str_to_list_int contains error.

        Times that were scored in injury time take the format "45'2".
        Method list_str_to_list_int split the str on "'", so
        they now appear as two goals.

        This method fixes that by only keeping goals that were scored
        at a time greater than the previous goal.

        @param, lists, list(list(int))
            list of lists(int), where each element of the sub-list is
            an int representing the match time when a goal was scored.
            Example: [[3, 10, 85], [5, 64], [23]]

        @returns, list(list(int))
            list of lists(int)
            Example: [[3, 10, 85], [5, 64], [23]]
        """

        ret_list: list = list()

        for a_list in lists:
            a_tidied_list = list()

            if (len(a_list) > 0):
                # add the first goal
                a_tidied_list.append(a_list[0])

            k: int = 1  # start the counter
            while (k < len(a_list)):
                if (a_list[k] >= a_list[k-1]):
                    a_tidied_list.append(a_list[k])

                k += 1

            ret_list.append(a_tidied_list)

        return ret_list

    def merge_lists(first_lists: list, second_lists: list) -> list:
        """
        Merges the elements of lists1 and lists2.

        @param, first_lists, list(list(int))
            Each element of list is a list of ints, where each elem is
            an int representing the match time when a goal was scored.
            Example: [[3, 10, 85], [5, 64]]

        @param, second_lists, list(list(int))
            Same description.
            Example: [[25], [79]]

        @returns, list(list(int))
            a list of lists of ints
            Example: [[3, 10, 85, 25], [5, 64, 79]]
        """

        ret_list: list = list()
        k: int = 0

        while (k < len(first_lists)):
            a_merged_list: list = list()
            a_first_list = first_lists[k]
            a_second_list = second_lists[k]

            for an_int in a_first_list:
                a_merged_list.append(an_int)

            for an_int in a_second_list:
                a_merged_list.append(an_int)

            ret_list.append(a_merged_list)
            k += 1

        return ret_list

    def sort_lists(lists: list) -> list:
        """
        Orders each sub-list of a list of lists in ascending order.

        @param, lists, list(list(int))
            a list of lists of unsorted ints
            Example: [[85, 25], [5, 64, 35]]

        @returns, list(list(int))
            a list of lists of sorted ints
            Example: [[25, 85], [5, 35, 64]]
        """

        for a_list in lists:
            if (len(a_list) > 0):
                a_list = a_list.sort()

        return lists

    def create_linked_lists(lists: list) -> tuple:
        """
        Returns a tuple of linked lists. They are linked in the sense
        that elem `i` in both lists
        are related.

        @param, lists, list(list(int))
            a list of lists of sorted ints
            Example: [[25, 85], [5, 35, 64]]

        @returns, (list(int), list(int))
            tuple of lists of ints
        """

        first_list: list = list()
        second_list: list = list()
        k: int = 0

        while (k < len(lists)):
            for a_list in lists:
                for an_int in a_list:
                    first_list.append(k)
                    second_list.append(an_int)
                k += 1

        return first_list, second_list
