# استخدم الصورة الرسمية لـ Python من Docker Hub
FROM python:3.8-slim-buster

# قم بتعيين الدليل العامل في الحاوية
WORKDIR /app

# نسخ ملفات المتطلبات وتثبيت الحزم المطلوبة
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# نسخ باقي الملفات
COPY . .

# تعيين الأمر الافتراضي لتشغيل التطبيق
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
