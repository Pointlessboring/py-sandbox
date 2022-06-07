import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single reponse is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses('English')
        self.assertIn('English', my_survey.responses)
    
    def test_store_three_responses(self):
        """Tests that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']

        for response in responses:
            my_survey.store_responses(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
    
if __name__ == '__main__':
    unittest.main()