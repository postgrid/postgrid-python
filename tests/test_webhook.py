import postgrid
import os

TEST_PAYLOAD = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoicG9zdGNhcmQudXBkYXRlZCIsImRhdGEiOnsiaWQiOiJwb3N0Y2FyZF9pQjNMbVp4MVF2bXFvUmYyc3BrUVR4IiwibGl2ZSI6ZmFsc2UsImJhY2tIVE1MIjoiR29vZGJ5ZSwge3t0by5maXJzdE5hbWV9fSIsImZyb20iOnsiaWQiOiJjb250YWN0X3M4Z3I1eHVSTnllcHVNRkpHcUVBaEciLCJhZGRyZXNzTGluZTEiOiIyMCBCQVkgU1QiLCJhZGRyZXNzTGluZTIiOiIiLCJhZGRyZXNzU3RhdHVzIjoidmVyaWZpZWQiLCJjaXR5IjoiVE9ST05UTyIsImNvbXBhbnlOYW1lIjoiUG9zdEdyaWQiLCJjb3VudHJ5Q29kZSI6IkNBIiwicG9zdGFsT3JaaXAiOiJNOVYgNFYxIiwicHJvdmluY2VPclN0YXRlIjoiT04ifSwiZnJvbnRIVE1MIjoiSGVsbG8sIHt7dG8uZmlyc3ROYW1lfX0iLCJwYWdlQ291bnQiOjIsInJlbmRlcmVkUERGUzNLZXkiOiJ0ZXN0L3Bvc3RjYXJkX2lCM0xtWngxUXZtcW9SZjJzcGtRVHgucGRmIiwic2VuZERhdGUiOiIyMDIyLTAzLTI0VDE1OjQwOjM3LjYzMVoiLCJzaXplIjoiNng0Iiwic3RhdHVzIjoiY2FuY2VsbGVkIiwidG8iOnsiaWQiOiJjb250YWN0X2duNG1YRms4c3B4Wmt1U1JLV3dYeW4iLCJhZGRyZXNzTGluZTEiOiIyMCBCQVkgU1QiLCJhZGRyZXNzTGluZTIiOiIiLCJhZGRyZXNzU3RhdHVzIjoidmVyaWZpZWQiLCJjaXR5IjoiVE9ST05UTyIsImNvbXBhbnlOYW1lIjoiVGVzdCBDb21wYW55IiwiY291bnRyeUNvZGUiOiJDQSIsImZpcnN0TmFtZSI6IlRlc3QiLCJqb2JUaXRsZSI6IlRlc3QiLCJsYXN0TmFtZSI6IkNvbnRhY3QiLCJtZXRhZGF0YSI6eyJ0ZXN0IjpbIjEwIiwiMjAiXX0sInBvc3RhbE9yWmlwIjoiTTlWIDRWMSIsInByb3ZpbmNlT3JTdGF0ZSI6Ik9OIn0sInVzZXIiOiJ1c2VyX2NWWWZKRnpFejQ3YkRnaHVUakJXaXMiLCJjcmVhdGVkQXQiOiIyMDIyLTAzLTI0VDE1OjQwOjM3LjYzNFoiLCJ1cGRhdGVkQXQiOiIyMDIyLTAzLTI0VDE1OjQwOjQwLjIwNFoifSwiaWF0IjoxNjQ4MTM2NDQwfQ.O4O499k17BzPJ1X69ULT9ZIlWi2EnCNgR7P_JNpZzyI'
TEST_SECRET = 'webhook_secret_7UPMB4r2Dkwa5KfnrUNrrv'
TEST_PAYLOAD_EVENT_TYPE = 'postcard.updated'


def setup_module():
    postgrid.pm_key = os.environ.get('PM_API_KEY')


def test_construct_event():
    event = postgrid.Webhook.construct_event(TEST_PAYLOAD, TEST_SECRET)

    assert isinstance(event, postgrid.WebhookEvent)
    assert event.type == TEST_PAYLOAD_EVENT_TYPE
    assert isinstance(event.data, postgrid.Postcard)

def create_test_webhook():
    return postgrid.Webhook.create(
        enabled_events=['letter.created', 'postcard.updated'],
        url='https://path-to-your-webhook-listener.com'
    )

def test_create():
    webhook=create_test_webhook()
    assert isinstance(webhook, postgrid.Webhook)
