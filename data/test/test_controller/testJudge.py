from django.test import TestCase

from data.models import Judge
from data.test import generate_objects
from data.views import DeleteJudgeView


class JudgeTestCase(TestCase):
    def testDeletesJudge(self):
        judge = generate_objects.valid_judge()
        judge.save()
        judge_id = judge.id

        view = DeleteJudgeView()
        view.post(None, judge_id)
        num_judges = Judge.objects.filter(id=judge_id).count()
        self.assertEqual(0, num_judges, "Judge did not delete")
