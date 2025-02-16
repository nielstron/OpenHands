import json

import sys
import os
from unidiff import PatchSet
import logging

_LOGGER = logging.getLogger(__name__)

prediction_dir = sys.argv[1]
# prediction_dir = "evaluation/evaluation_outputs/outputs/princeton-nlp__SWE-bench_Lite-test/CodeActAgent/claude-3-5-sonnet-20241022_maxiter_30_N_v0.23.0-no-hint-run_1/llm_completions/astropy__astropy-6938"
predictions = []

# extract everything under "2025-02-12 17:11:03,241 - INFO - Got git diff for instance astropy__astropy-6938:"

instance = sorted(os.listdir(prediction_dir))[-1]
with open(os.path.join(prediction_dir, instance)) as f:
    res = json.load(f)
for message in res["messages"]:
    print("------------")
    print(message["role"], ":")
    print("------------")
    for content in message["content"]:
        if content["type"] == "text":
            print(content["text"])
        else:
            print("unknown content type")
            print(content)
    for content in message.get("tool_calls",[]):
        print(content)
    input()
