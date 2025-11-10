#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from coder.crew import Coder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

assignment = "Write a program that will find the closest prime number given any value of any given number by the user"

def run():
    """
    Run the crew.
    """
    inputs = {
        "assignment": assignment
    }

    result = Coder().crew().kickoff(inputs=inputs)
    print(result.raw)

if __name__ == "__main__":
    run()