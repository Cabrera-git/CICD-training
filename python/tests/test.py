from functions.app import AWS_LAMBDA

def test_lambda_handler():
    event = None
    context = None
    expected_result = 75

    result = AWS_LAMBDA(event, context)

    assert result == expected_result