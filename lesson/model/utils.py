import lesson


def resources(path):
    from pathlib import Path
    return str(
        Path(lesson.__file__)
        .parent
        .parent
        .joinpath(f'resources/{path}')
    )
