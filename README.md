# PyJen004

Simple addition program in Python with automated build, test and deploy by Jenkins
(832208/632218 DevOps and System Integration - Jenkins #4).

- `calculator.py` - `add(a, b)` and a command line program: `python calculator.py 10 20`
- `test_calculator.py` - unit tests (pytest)
- `Jenkinsfile` - pipeline: Checkout -> Setup Python -> Lint -> Test -> Build -> Deploy (Poll SCM every ~2 minutes)

Author: สนธยา สายวรรณะ (6752410004)
