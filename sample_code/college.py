class College:
    """This class contains basic details about the College."""
    def __init__(self, college_name: str, location: str, has_pg: bool = False) -> None:
        """This method is a constructor which accepts college details from the user.

        Parameters
        ----------
        college_name : str
            Name of College
        location : str
            Location of College
        has_pg : bool, optional
            _description_, by default False
        """
        self.college_name = college_name
        self.location = location
        self.has_pg = has_pg

    def details(self) -> None:
        """Returns College details.
        """
        print(f"College: {self.college_name}\nLocation: {self.location}\nHas PG: {self.has_pg}")

abhinav = College("Abhinav Junior College", "Ambegaon")
abhinav.details()