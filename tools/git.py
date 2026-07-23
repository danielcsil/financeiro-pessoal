"""
Ferramentas auxiliares para utilização do Git.

Projeto: Sistema Financeiro Pessoal
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


def _run(*args: str) -> str:
    result = subprocess.run(
        list(args),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr.strip()

    return result.stdout.strip()


def current_branch() -> str:
    return _run("git", "branch", "--show-current")


def remote_url() -> str:
    """
    Retorna a URL do remote origin sem expor credenciais.
    """

    remote = _run("git", "remote", "get-url", "origin")

    if not remote or remote.startswith("fatal:"):
        return "Não configurado"

    # Remove usuário/token da URL HTTPS
    remote = re.sub(
        r"^(https://)[^@]+@",
        r"\1",
        remote,
    )

    return remote


def setup_git(
    user_name: str | None = None,
    user_email: str | None = None,
) -> None:

    print("=" * 60)
    print("GIT")
    print("=" * 60)

    if not Path(".git").exists():
        print("Este diretório não é um repositório Git.")
        return

    if user_name:
        subprocess.run(
            ["git", "config", "user.name", user_name],
            capture_output=True
        )

    if user_email:
        subprocess.run(
            ["git", "config", "user.email", user_email],
            capture_output=True
        )

    print(f"Branch : {current_branch()}")
    print(f"Remote : {remote_url()}")

    print("\nStatus")
    print("-" * 60)

    status()

    print("=" * 60)


def status() -> None:

    result = _run(
        "git",
        "status",
        "--short"
    )

    if result:
        print(result)
    else:
        print("Working tree limpa.")


def diff() -> None:
    print(
        _run(
            "git",
            "diff"
        )
    )


def log(limit: int = 10) -> None:

    print(
        _run(
            "git",
            "log",
            "--oneline",
            f"-{limit}"
        )
    )


def commit(
    version: str,
    message: str,
    add_all: bool = True,
) -> None:

    if add_all:
        subprocess.run(["git", "add", "."])

    result = _run(
        "git",
        "status",
        "--short"
    )

    if not result:
        print("Nenhuma alteração encontrada.")
        return

    commit_message = f"{version} - {message}"

    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            commit_message
        ]
    )


def push() -> None:

    subprocess.run(
        [
            "git",
            "push",
            "origin",
            current_branch()
        ]
    )


def pull() -> None:

    subprocess.run(
        [
            "git",
            "pull",
            "origin",
            current_branch()
        ]
    )


def release(
    version: str,
    message: str,
) -> None:

    commit(version, message)
    push()