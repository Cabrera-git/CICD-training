FROM public.ecr.aws/lamda/python:3.10

COPY requirements.txt
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY functions/app.py ${LAMBDA_TASK_ROOT}

CMD [ "app.handler" ]