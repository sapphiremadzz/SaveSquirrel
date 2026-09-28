from dataclasses import dataclass

@dataclass
class SavingsGoal:
    title: str
    target_amount: float
    target_date: str
    id: int | None

    def __post_init__(self) -> None:
        self.id = self.id
        self.title = self.title.strip()
        self.target_amount = float(self.target_amount)
        self.target_date = self.target_date.strip()

        if not self.title:
            raise ValueError ("Title cannot be empty")
        if not self.target_amount:
            raise ValueError ("Target amount cannot be empty")
        if not self.target_date:
            raise ValueError ("Target date cannot be empty")
