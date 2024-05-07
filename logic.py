from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    """
    This class contains all the logic for the program
    """
    hidden = False
    with open('grades.csv', 'w', newline='') as output_csv_file:

        csv_content = csv.writer(output_csv_file)
        csv_content.writerow(
            ['Assignment Number', 'Student Name', 'Number of Attempts', 'Attempt 1 Score', 'Attempt 2 Score',
             'Attempt 3 Score', 'Attempt 4 Score', 'Attempt 5 Score', 'Average Score'])

    def __init__(self) -> None:
        """
        Method hides UI on program start. Also contains code triggers for calculate and clear buttons being clicked,
        and num_attempts being changed, so that amount of score boxes is dynamic
        """
        super().__init__()
        self.setupUi(self)
        self.show_hide()

        self.button_calculate.clicked.connect(lambda: self.calculate())
        self.input_num_attempts.textChanged.connect(lambda: self.show_hide())
        self.button_clear.clicked.connect(lambda: self.clear())


    def get_letter_grade(self, score: float) -> str:
        """
        Method to return letter grade based on score received
        :param score: Score between 0 and 100 that is to be translated to letter grade
        :return: Letter grade based on score received
        """
        if score <= 100.0 and score >= 93.0:
            return 'A'
        elif score <= 92.9 and score >= 90.0:
            return 'A-'
        elif score <= 89.9 and score >= 87.1:
            return 'B+'
        elif score <= 87.0 and score >= 83.0:
            return 'B'
        elif score <= 82.9 and score >= 80.0:
            return 'B-'
        elif score <= 79.9 and score >= 77.1:
            return 'C+'
        elif score <= 77.0 and score >=73.0:
            return 'C'
        elif score <= 72.9 and score >= 70.0:
            return 'C-'
        elif score <= 69.9 and score >= 67.1:
            return 'D+'
        elif score <= 67.0 and score >= 60.0:
            return 'D'
        else:
            return 'F'

    def calculate(self) -> None:
        """
        This method calculates the grade average based on user-entered attempt scores, displays the results
        and writes the results to an excel file.
        """
        try:
            attempts = int(self.input_num_attempts.text())
            assignment_number = int(self.input_assign_num.text())
            student_name = self.input_student_name.text()
            self.label_confirmation.setText('')

            if attempts == 1:
                score_1 = float(self.input_score_1.text())
                if score_1 > 100.0 or score_1 < 0:
                    self.input_score_1.setText('')
                    raise Exception
                average = score_1/attempts
                letter_grade = self.get_letter_grade(average)
                self.label_result.setText(f'The average of all attempts by {student_name} for assignment '
                                          f'{assignment_number} is {average:.1f} ({letter_grade}). '
                                          f'These scores have been recorded.')

                with open('grades.csv', 'a', newline='') as output_csv_file:

                    csv_content = csv.writer(output_csv_file)
                    csv_content.writerow(
                        [assignment_number, student_name, attempts, score_1, '', '', '', '', "%.1f" % average, letter_grade])

            elif attempts == 2:
                score_1 = float(self.input_score_1.text())
                score_2 = float(self.input_score_2.text())
                if score_1 > 100.0 or score_1 < 0:
                    self.input_score_1.setText('')
                    raise Exception
                if score_2 > 100.0 or score_1 <0:
                    self.input_score_2.setText('')
                    raise Exception
                average = (score_1+ score_2) / attempts
                letter_grade = self.get_letter_grade(average)
                self.label_result.setText(f'The average of all attempts by {student_name} for assignment '
                                          f'{assignment_number} is {average:.1f} ({letter_grade}). '
                                          f'These scores have been recorded.')

                with open('grades.csv', 'a', newline='') as output_csv_file:

                    csv_content = csv.writer(output_csv_file)
                    csv_content.writerow(
                        [assignment_number, student_name, attempts, score_1, score_2, '', '', '', "%.1f" % average, letter_grade])

            elif attempts == 3:
                score_1 = float(self.input_score_1.text())
                score_2 = float(self.input_score_2.text())
                score_3 = float(self.input_score_3.text())
                if score_1 > 100.0 or score_1 < 0:
                    self.input_score_1.setText('')
                    raise Exception
                if score_2 > 100.0 or score_2 < 0:
                    self.input_score_2.setText('')
                    raise Exception
                if score_3 > 100.0 or score_3 < 0:
                    self.input_score_3.setText('')
                    raise Exception
                average = (score_1 + score_2 + score_3) / attempts
                letter_grade = self.get_letter_grade(average)
                self.label_result.setText(f'The average of all attempts by {student_name} for assignment '
                                          f'{assignment_number} is {average:.1f} ({letter_grade}). '
                                          f'These scores have been recorded.')

                with open('grades.csv', 'a', newline='') as output_csv_file:

                    csv_content = csv.writer(output_csv_file)
                    csv_content.writerow(
                        [assignment_number, student_name, attempts, score_1, score_2, score_3, '', '', "%.1f" % average, letter_grade])

            elif attempts == 4:
                score_1 = float(self.input_score_1.text())
                score_2 = float(self.input_score_2.text())
                score_3 = float(self.input_score_3.text())
                score_4 = float(self.input_score_4.text())
                if score_1 > 100.0 or score_1 < 0:
                    self.input_score_1.setText('')
                    raise Exception
                if score_2 > 100.0 or score_2 < 0:
                    self.input_score_2.setText('')
                    raise Exception
                if score_3 > 100.0 or score_3 < 0:
                    self.input_score_3.setText('')
                    raise Exception
                if score_4 > 100.0 or score_4 < 0:
                    self.input_score_4.setText('')
                    raise Exception
                average = (score_1 + score_2 + score_3 + score_4) / attempts
                letter_grade = self.get_letter_grade(average)
                self.label_result.setText(f'The average of all attempts by {student_name} for assignment '
                                          f'{assignment_number} is {average:.1f} ({letter_grade}). '
                                          f'These scores have been recorded.')

                with open('grades.csv', 'a', newline='') as output_csv_file:

                    csv_content = csv.writer(output_csv_file)
                    csv_content.writerow(
                        [assignment_number, student_name, attempts, score_1, score_2, score_3, score_4, '', "%.1f" % average, letter_grade])

            elif attempts == 5:
                score_1 = float(self.input_score_1.text())
                score_2 = float(self.input_score_2.text())
                score_3 = float(self.input_score_3.text())
                score_4 = float(self.input_score_4.text())
                score_5 = float(self.input_score_5.text())
                if score_1 > 100.0 or score_1 < 0:
                    self.input_score_1.setText('')
                    raise Exception
                if score_2 > 100.0 or score_2 < 0:
                    self.input_score_2.setText('')
                    raise Exception
                if score_3 > 100.0 or score_3 < 0:
                    self.input_score_3.setText('')
                    raise Exception
                if score_4 > 100.0 or score_4 < 0:
                    self.input_score_4.setText('')
                    raise Exception
                if score_5 > 100.0 or score_5 < 0:
                    self.input_score_5.setText('')
                    raise Exception
                average = (score_1 + score_2 + score_3 + score_4 + score_5) / attempts
                letter_grade = self.get_letter_grade(average)
                self.label_result.setText(f'The average of all attempts by {student_name} for assignment '
                                          f'{assignment_number} is {average:.1f} ({letter_grade}). '
                                          f'These scores have been recorded.')

                with open('grades.csv', 'a', newline='') as output_csv_file:

                    csv_content = csv.writer(output_csv_file)
                    csv_content.writerow(
                        [assignment_number, student_name, attempts, score_1, score_2, score_3, score_4, score_5, "%.1f" % average, letter_grade])

            elif int(self.input_num_attempts.text()) > 5 or int(self.input_num_attempts.text()) < 1:
                raise Exception





        except Exception:
            self.label_result.setText('')
            self.label_confirmation.setStyleSheet('color : red')
            self.label_confirmation.setText('Please ensure the following fields are valid:\n a number for assignment number\n'
                                            ' a number between 1 and 5 for number of attempts\n '
                                        'a score between 0 and 100 for all attempt scores.')



    def clear(self) -> None:
        """
        This method resets the UI to the starting status
        :return:
        """
        self.input_assign_num.setText('')
        self.input_num_attempts.setText('')
        self.input_student_name.setText('')
        self.label_attempt_1.hide()
        self.label_attempt_2.hide()
        self.label_attempt_3.hide()
        self.label_attempt_4.hide()
        self.label_attempt_5.hide()
        self.input_score_1.setText('')
        self.input_score_1.hide()
        self.input_score_2.setText('')
        self.input_score_2.hide()
        self.input_score_3.setText('')
        self.input_score_3.hide()
        self.input_score_4.setText('')
        self.input_score_4.hide()
        self.input_score_5.setText('')
        self.input_score_5.hide()
        self.label_confirmation.setText('')
        self.label_result.setText('')



    def show_hide(self) -> None:
        """
        This method dynamically hides and shows attempt scores, labels and error messages
        """
        try:
            self.label_confirmation.setText('')
            if not self.hidden:
                self.label_attempt_1.hide()
                self.input_score_1.hide()
                self.label_attempt_2.hide()
                self.input_score_2.hide()
                self.label_attempt_3.hide()
                self.input_score_3.hide()
                self.label_attempt_4.hide()
                self.input_score_4.hide()
                self.label_attempt_5.hide()
                self.input_score_5.hide()
                self.hidden = True
            else:
                #this first if statement resets the UI
                if  self.input_num_attempts.text() == '':
                    self.label_confirmation.setStyleSheet('color : black')
                    self.label_confirmation.setText('')
                    self.input_score_1.setText('')
                    self.input_score_2.setText('')
                    self.input_score_3.setText('')
                    self.input_score_4.setText('')
                    self.input_score_5.setText('')

                    self.label_attempt_1.hide()
                    self.input_score_1.hide()
                    self.label_attempt_2.hide()
                    self.input_score_2.hide()
                    self.label_attempt_3.hide()
                    self.input_score_3.hide()
                    self.label_attempt_4.hide()
                    self.input_score_4.hide()
                    self.label_attempt_5.hide()
                    self.input_score_5.hide()
                elif self.input_num_attempts.text() == '1':
                    self.label_attempt_1.show()
                    self.input_score_1.show()
                    self.label_attempt_2.hide()
                    self.input_score_2.hide()
                    self.label_attempt_3.hide()
                    self.input_score_3.hide()
                    self.label_attempt_4.hide()
                    self.input_score_4.hide()
                    self.label_attempt_5.hide()
                    self.input_score_5.hide()
                elif self.input_num_attempts.text() == '2':
                    self.label_attempt_1.show()
                    self.input_score_1.show()
                    self.label_attempt_2.show()
                    self.input_score_2.show()
                    self.label_attempt_3.hide()
                    self.input_score_3.hide()
                    self.label_attempt_4.hide()
                    self.input_score_4.hide()
                    self.label_attempt_5.hide()
                    self.input_score_5.hide()
                elif self.input_num_attempts.text() == '3':
                    self.label_attempt_1.show()
                    self.input_score_1.show()
                    self.label_attempt_2.show()
                    self.input_score_2.show()
                    self.label_attempt_3.show()
                    self.input_score_3.show()
                    self.label_attempt_4.hide()
                    self.input_score_4.hide()
                    self.label_attempt_5.hide()
                    self.input_score_5.hide()
                elif self.input_num_attempts.text() == '4':
                    self.label_attempt_1.show()
                    self.input_score_1.show()
                    self.label_attempt_2.show()
                    self.input_score_2.show()
                    self.label_attempt_3.show()
                    self.input_score_3.show()
                    self.label_attempt_4.show()
                    self.input_score_4.show()
                    self.label_attempt_5.hide()
                    self.input_score_5.hide()
                elif self.input_num_attempts.text() =='5':
                    self.label_attempt_1.show()
                    self.input_score_1.show()
                    self.label_attempt_2.show()
                    self.input_score_2.show()
                    self.label_attempt_3.show()
                    self.input_score_3.show()
                    self.label_attempt_4.show()
                    self.input_score_4.show()
                    self.label_attempt_5.show()
                    self.input_score_5.show()


                elif int(self.input_num_attempts.text()) > 5 or int(self.input_num_attempts.text()) < 1:
                    raise Exception


        except Exception:
            self.input_num_attempts.setText('')
            self.label_confirmation.setStyleSheet('color : red')
            self.label_confirmation.setText('Please enter a number between 1 and 5\n for number of attempts.')







