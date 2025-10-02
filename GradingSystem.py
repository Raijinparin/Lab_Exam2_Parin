class GradingSystem:
    """Handles the grading system logic, including grade input, calculation, and display of results."""
    
    def __init__(self, min_grade=0, max_grade=100):
        self.valid_grades = []
        self.min_grade = min_grade
        self.max_grade = max_grade
        
    def _get_remarks(self, final_grade_value):
        """Helper method to determine letter grade and remarks."""
        if final_grade_value >= 95:
            return "Passed - Very Good", "Very Good"
        elif final_grade_value >= 90:
            return "Passed - Good", "Good"
        elif final_grade_value >= 85:
            return "Passed - Satisfactory", "Satisfactory"
        elif final_grade_value >= 80:
            return "Passed - Fair", "Fair"
        elif final_grade_value >= 75:
            return "Passed", "Passed"
        elif final_grade_value >= 70:
            return "Failed", "Failed"
        elif final_grade_value >= 65:
            return "Failed - Poor", "Poor"
        elif final_grade_value >= 60:
            return "Failed - Very Poor", "Very Poor"
        else:
            return "No such grade", "No such grade"

    def input_grades(self):
        """Method to collect grades interactively."""
        print(f"\nEnter grades ({self.min_grade}-{self.max_grade}). Enter -1 to stop.")
        while True:
            try:
                grade_input = input("Input Grade: ")
                grade = int(grade_input)
                
                if grade == -1:
                    break
                
                if self.min_grade <= grade <= self.max_grade:
                    self.valid_grades.append(grade)
                    print(f"Grade {grade} added.")
                else:
                    print(f"Grade {grade} is out of range and ignored.")
                    
            except ValueError:
                print("Invalid input. Please enter a number or -1.")

    def calculate_results(self):
        """Method to calculate and return grading results."""
        if not self.valid_grades:
            return None
        
        average = sum(self.valid_grades) / len(self.valid_grades)
        
        # Formula: ((100 - Average Grade) + 10) / 10
        point_grade = ((self.max_grade - average) + 10) / 10.0
        
        letter_grade, remarks = self._get_remarks(average)
        
        return {
            "average": average,
            "point_grade": point_grade,
            "letter_grade": letter_grade,
            "remarks": remarks
        }

    def display_results(self):
        """Method to display the calculated results."""
        results = self.calculate_results()
        
        if results is None:
            print("\nNo valid grades were entered.")
            return

        print("\n--- Grading Results ---")
        print(f"Average: {results['average']:.2f}")
        print(f"Point Grade: {results['point_grade']:.2f}")
        print(f"Letter Grade: {results['letter_grade']}")
        print(f"Remarks: {results['remarks']}")