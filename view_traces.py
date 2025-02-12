import json

import sys
import os
from unidiff import PatchSet
import logging

_LOGGER = logging.getLogger(__name__)

#prediction_dir = sys.argv[1] # "evaluation/evaluation_outputs/outputs/princeton-nlp__SWE-bench_Lite-test/CodeActAgent/claude-3-5-sonnet-20241022_maxiter_30_N_v0.23.0-no-hint-testrun1/infer_logs"
prediction_dir = "evaluation/evaluation_outputs/outputs/princeton-nlp__SWE-bench_Lite-test/CodeActAgent/claude-3-5-sonnet-20241022_maxiter_30_N_v0.23.0-no-hint-testrun1/llm_completions/astropy__astropy-6938"
predictions = []

# extract everything under "2025-02-12 17:11:03,241 - INFO - Got git diff for instance astropy__astropy-6938:"

instance = sorted(os.listdir(prediction_dir))[-1]
with open(os.path.join(prediction_dir, instance)) as f:
    res = json.load(f)
for message in res["messages"]:
    print(res)
    input()
