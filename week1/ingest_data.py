#!/usr/bin/env python
# coding: utf-8

import subprocess
import argparse
from time import time
from os import system

import pandas as pd
from sqlalchemy import create_engine

def run_cmd(cmd: str, timeout=None):
    """Run a bash command.
    Args:
        cmd (str): Command to run in bash
        timeout (int): Timeout in seconds. Defaults to None.
    """
    try:
        if isinstance(cmd, list):
            proc = subprocess.run(cmd, timeout=timeout)
        else:
            proc = subprocess.run(cmd, shell=True, timeout=timeout)
        if proc.returncode != 0:
            print(
                f"Command <<{proc.args}>> failed.\nReturn Code: {proc.returncode}.\nError Message: {proc.stderr}\n")
            exit()
        else:
            pass
    except Exception as e:
        print(f"Command {cmd} failed with error: ", e)
        exit()

def main(args):

    # downloading the data 
    output_name = args.url.split('/')[-1]
    cmd = f"wget {args.url} -O {output_name}"
    engine = create_engine(f'postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}')
    run_cmd(cmd)
    # system(cmd)
    if args.url.endswith('.parquet'):
        df = pd.read_parquet(output_name)
    else:
        df = pd.read_csv(output_name)


    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest parquet file to Postgre Server")

    parser.add_argument('--user', required=True, help='Username for Postgres')
    parser.add_argument('--password', required=True, help='Password for Postgres')
    parser.add_argument('--port', required=True, help='Port for Postgres', type=str)
    parser.add_argument('--host', required=True, help='host for Postgres')
    parser.add_argument('--db', required=True, help='database name for Postgres')
    parser.add_argument('--table_name', required=True, help='Table name for Postgres')
    parser.add_argument('--url', required=True, help='Url of the parquet file')

    args = parser.parse_args()

    main(args)





