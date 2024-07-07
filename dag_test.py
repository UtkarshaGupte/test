from prefect import flow, task


@flow
def main_flow():
    wait = task1()
    task2(wait_for=wait)


@task
def task1():
    print(1)


@task
def task2():
    print(2)


if __name__ == "__main__":
    main_flow()
