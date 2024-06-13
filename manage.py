#!/usr/bin/env python

import argparse
import subprocess
import time
import logging
import os
import sys
import getpass


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)


def cli(command, check=True):
    logging.info(f"Running command: {command}")
    try:
        r = subprocess.run(
            command,
            check=check,
            shell=True,
            capture_output=True,
            text=True
        )
        logging.info(r.stdout.strip())
        return r
    except subprocess.CalledProcessError as e:
        logging.error(f"Failing command: {command}")
        logging.error(e.stderr.strip())
        raise


def renew_cert():
    cli("docker compose start certbot")
    for i in range(12):
        res = cli("docker compose ps --services --status=exited", check=False)
        if res.returncode == 0 and "certbot" in res.stdout.strip():
            break
        else:
            time.sleep(5)
    cli("docker compose restart nginx")


def renew_cert_cron():
    cron_job = f"@daily {sys.executable} {os.path.abspath(__file__)} renew-cert"
    res = cli("crontab -l", check=False)
    if res.returncode == 0:
        if cron_job not in res.stdout.strip():
            cron_job = f"{res.stdout.strip()}\n{cron_job}\n"
        else:
            return
    cli(f"echo '{cron_job}' | crontab -u {getpass.getuser()} -")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="A script to manage the SSL/TLS certificates."
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Available commands:"
    )
    subparsers.add_parser(
        "renew-cert",
        help="Renew SSL/TLS certificates"
    )
    subparsers.add_parser(
        "renew-cert-cron",
        help="Set up a daily cron job to renew SSL/TLS certificates"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.command == "renew-cert":
        renew_cert()
    elif args.command == "renew-cert-cron":
        renew_cert_cron()


if __name__ == "__main__":
    main()
