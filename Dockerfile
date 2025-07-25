FROM public.ecr.aws/lambda/python:3.13

# 必要パッケージインストール
RUN pip install debugpy

# Lambda 関数ファイル追加
COPY app.py .

# Lambda ハンドラーを debugpy 経由で起動
CMD ["debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m", "awslambdaric", "app.lambda_handler"]