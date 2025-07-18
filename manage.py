
import os
import sys
from dotenv import load_dotenv


def main():
    load_dotenv()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что он установлен и "
            "доступен в вашем виртуальном окружении."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()