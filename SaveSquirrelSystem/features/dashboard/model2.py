class SavingsDashboard:
    def __init__(self, income: float, expense: float, savings: float):
        self.__income = float(income)
        self.__expense = float(expense)
        self.__savings = float(savings)

    def get_income(self) -> float:
        return self.__income

    def get_expense(self) -> float:
        return self.__expense

    def get_savings(self) -> float:
        return self.__savings

