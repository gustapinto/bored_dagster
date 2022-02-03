from src.jobs.boredapi import ingest_boredapi


from src.jobs.boredapi import ingest_boredapi


def main() -> None:
    ingest_boredapi.execute_in_process()

if __name__ == "__main__":
    main()
