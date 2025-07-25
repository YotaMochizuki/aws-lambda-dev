from mylib.util import hello  # Layer で提供される関数


def lambda_handler(event, context):
    """AWS Lambda のエントリポイント関数.

    Parameters:
        event (dict): イベントデータ（API Gateway やテスト入力など）
        context (LambdaContext): 実行コンテキスト情報.

    Returns:
        dict: HTTP ステータスコードとレスポンスボディを含む辞書.
    """
    name = event.get("name", "World")
    return {"statusCode": 200, "body": hello(name)}
