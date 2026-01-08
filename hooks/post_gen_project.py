import os

paths = [
    "{{cookiecutter.project_slug}}/{{cookiecutter.context_name}}/domain/entities",
    "{{cookiecutter.project_slug}}/{{cookiecutter.context_name}}/application/usecases",
]

for path in paths:
    os.makedirs(path, exist_ok=True)
