import os

paths = [
    "src/contexts/{{cookiecutter.context_name}}/domain/entities",
    "src/contexts/{{cookiecutter.context_name}}/application/usecases",
]

for path in paths:
    os.makedirs(path, exist_ok=True)
