import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skeleton.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402

# Expose as `app` for Vercel's Python runtime
app = get_wsgi_application()
