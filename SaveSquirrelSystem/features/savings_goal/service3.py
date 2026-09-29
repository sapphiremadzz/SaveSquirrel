from features.savings_goal.repository3 import GoalRepository
from features.savings_goal.model3 import SavingsGoal
from features.savings_management.service import SavingsService  # Import validation logic[cite: 6]

class ServiceGoal:
    def __init__(self, repository: GoalRepository):
        self.repository = repository



    def add_goal(self, goal: SavingsGoal) -> SavingsGoal:
        goal.target_amount = SavingsService.validate_amount(goal.target_amount)
        return self.repository.add_goal(goal)

    def get_goals(self) -> list[SavingsGoal]:
        return self.repository.get_all_goals()

    def delete(self, trans_id: int) -> SavingsGoal:
        delete_goals = SavingsGoal(
            id=trans_id,
            title="",
            target_amount=0.0,
            target_date=""
        )
        return self.repository.delete_goal(delete_goals)

    def update(self, goal: SavingsGoal) -> SavingsGoal:
        goal.target_amount = SavingsService.validate_amount(goal.target_amount)
        return self.repository.update_goal(goal)