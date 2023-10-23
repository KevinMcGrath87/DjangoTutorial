from django.test import TestCase
# Create your tests here.
import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question, Choice


def create_question(question_text, days):
    time = timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date = time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):

        time = timezone.now()+datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds = 1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(),False)
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now(0 - datetime.timedelta(hours = 23, minutes = 59, seconds = 59))
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(),True)



class ChoiceHasQuestion(TestCase):
    def test_choice_has_question(self):
        test_flag = False
        testChoice = Choice(choice_text = "Im a stupid choice")
        if(hasattr(testChoice, 'question')):
            test_flag = True

        try:
            if(testChoice.question):
                test_flag = True
                print(testChoice.question)
        except AttributeError as a: 
            print(a, "doesnt have a question!")
            test_flag = False
        finally:
            self.assertIs(test_flag, True)


